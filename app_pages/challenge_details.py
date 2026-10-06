import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH, CATEGORY_IMAGES, CHALLENGE_IMAGES, LEVEL_ICONS


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

st.image(get_challenge_image(challenge["name"], challenge["category"]), width="stretch")
st.title(challenge["name"])

col1, col2, col3 = st.columns(3)
col1.metric("Category", challenge["category"])
col2.metric("Activities", len(activities))
col3.metric("Duration", f"{challenge['duration']} days")
st.write(challenge["description"])

# Joining saves the challenge to your account, so you need to be logged in.
if "user_id" in st.session_state:
    conn = sqlite3.connect(DATABASE_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    joined = conn.execute(
        "select 1 from user_challenges where user_id = ? and challenge_id = ?",
        (st.session_state.user_id, challenge_id),
    ).fetchone()
    conn.close()

    if joined:
        st.success("You joined this challenge. You can find it in My challenges.")
    elif st.button("Start challenge", type="primary", width="stretch"):
        conn = sqlite3.connect(DATABASE_PATH)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute(
            "insert into user_challenges (user_id, challenge_id) values (?, ?)",
            (st.session_state.user_id, challenge_id),
        )
        conn.commit()
        conn.close()
        st.success("You joined this challenge!")
        st.balloons()
else:
    st.info("Log in to join this challenge.")

if challenge["category"] == "General Knowledge":
    if st.button("🧠 Play the quiz", width="stretch"):
        st.switch_page("app_pages/general_knowledge.py")

st.divider()
st.subheader("Activities")

if len(activities) == 0:
    st.info("This challenge has no activities yet.")
else:
    level = st.radio("Show level", ["All", "Easy", "Medium", "Hard"], horizontal=True)
    shown = 0
    for activity in activities:
        if level == "All" or activity["difficulty"] == level:
            with st.container(border=True):
                st.markdown(f"**{activity['name']}** · {LEVEL_ICONS[activity['difficulty']]} {activity['difficulty']}")
                st.caption(activity["description"])
            shown = shown + 1
    if shown == 0:
        st.info(f"No {level} activities in this challenge.")
