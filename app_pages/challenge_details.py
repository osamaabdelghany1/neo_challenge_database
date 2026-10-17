import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH, CATEGORY_IMAGES, CHALLENGE_IMAGES, LEVEL_ICONS

# How wide the challenge picture is, in pixels. Our flag pictures are about 550 pixels wide,
# so 400 keeps them sharp instead of stretching them across the whole page.
IMAGE_WIDTH = 400


def get_challenge_image(name, category):
    # A language challenge shows its country's flag; anything else shows its category picture.
    for language in CHALLENGE_IMAGES:
        if language.lower() in name.lower():
            return CHALLENGE_IMAGES[language]
    return CATEGORY_IMAGES[category]


# This page needs a challenge picked on another page first.
if "selected_challenge_id" not in st.session_state:
    st.switch_page("app_pages/view_challenges.py")

challenge_id = st.session_state.selected_challenge_id

conn = sqlite3.connect(DATABASE_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
challenge = conn.execute("select * from challenges where id = ?", (challenge_id,)).fetchone()
activities = conn.execute("select * from activities where challenge_id = ? order by name", (challenge_id,)).fetchall()
conn.close()

if challenge is None:
    st.error("That challenge does not exist anymore.")
    st.stop()

st.image(get_challenge_image(challenge["name"], challenge["category"]), width=IMAGE_WIDTH)
st.title(challenge["name"])

col1, col2, col3 = st.columns(3)
col1.metric("Category", challenge["category"])
col2.metric("Activities", len(activities))
col3.metric("Duration", f"{challenge['duration']} days")
st.write(challenge["description"])
       
       
# Joining saves the challenge to your account, so you need to be logged in.
joined = False
done_ids = []
if "user_id" in st.session_state:
    conn = sqlite3.connect(DATABASE_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    joined = conn.execute(
        "select 1 from user_challenges where user_id = ? and challenge_id = ?",
        (st.session_state.user_id, challenge_id),
    ).fetchone() is not None
    # The activities of this challenge you already ticked Done.
    rows = conn.execute("""
        select user_activities.activity_id
        from user_activities join activities on activities.id = user_activities.activity_id
        where user_activities.user_id = ? and activities.challenge_id = ?
    """, (st.session_state.user_id, challenge_id)).fetchall()
    for row in rows:
        done_ids.append(row[0])
    conn.close()

    if joined:
        st.success("You joined this challenge. You can find it in My challenges.")
        # Balloons only right after joining, not every time you open the page.
        if st.session_state.get("just_joined"):
            st.balloons()
            st.session_state.just_joined = False
    elif st.button("Start challenge", type="primary", width="stretch"):
        conn = sqlite3.connect(DATABASE_PATH)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute(
            "insert into user_challenges (user_id, challenge_id) values (?, ?)",
            (st.session_state.user_id, challenge_id),
        )
        conn.commit()
        conn.close()
        # Reload the page so the button disappears and the "you joined" message shows.
        st.session_state.just_joined = True
        st.rerun()
else:
    st.info("Log in to join this challenge.")

if challenge["category"] == "General Knowledge":
    if st.button("🧠 Play the quiz", type="primary", width="stretch"):
        st.switch_page("app_pages/general_knowledge.py")

st.divider()
st.subheader("Activities")

if len(activities) == 0:
    st.info("This challenge has no activities yet.")
    st.stop()

if joined:
    st.progress(len(done_ids) / len(activities), text=f"{len(done_ids)} of {len(activities)} done")
    # Balloons once, right after the last activity is ticked.
    if st.session_state.get("challenge_finished"):
        st.balloons()
        st.success("You finished every activity in this challenge!")
        st.session_state.challenge_finished = False
elif "user_id" in st.session_state:
    st.info("Start the challenge to track your progress.")

level = st.pills("Show level", ["All", "Easy", "Medium", "Hard"], default="All", required=True)
shown = 0
for activity in activities:
    if level != "All" and activity["difficulty"] != level:
        continue
    shown = shown + 1
    with st.container(border=True):
        st.markdown(f"**{activity['name']}** · {LEVEL_ICONS[activity['difficulty']]} {activity['difficulty']}")
        st.caption(activity["description"])

        if joined:
            was_done = activity["id"] in done_ids
            ticked = st.checkbox("Done", value=was_done, key=f"done_{activity['id']}")
            # Save the change only when the tick is different from what we stored.
            if ticked != was_done:
                conn = sqlite3.connect(DATABASE_PATH)
                conn.execute("PRAGMA foreign_keys = ON")
                if ticked:
                    conn.execute(
                        "insert into user_activities (user_id, activity_id) values (?, ?)",
                        (st.session_state.user_id, activity["id"]),
                    )
                    if len(done_ids) + 1 == len(activities):
                        st.session_state.challenge_finished = True
                else:
                    conn.execute(
                        "delete from user_activities where user_id = ? and activity_id = ?",
                        (st.session_state.user_id, activity["id"]),
                    )
                conn.commit()
                conn.close()
                st.rerun()

        # Some activities use one of our video exercises.
        if activity["exercise_id"]:
            if st.button("▶ Watch the video", key=f"video_{activity['id']}", type="primary", width="stretch"):
                st.session_state.selected_exercise_id = activity["exercise_id"]
                st.switch_page("app_pages/exercise_details.py")

if shown == 0:
    st.info(f"No {level} activities in this challenge.")
