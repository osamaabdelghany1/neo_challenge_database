import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH, CATEGORY_IMAGES, CHALLENGE_IMAGES


def get_challenge_image(name, category):
    # A language challenge shows its country's flag; anything else shows its category picture.
    for language in CHALLENGE_IMAGES:
        if language.lower() in name.lower():
            return CHALLENGE_IMAGES[language]
    return CATEGORY_IMAGES[category]


st.title("🗣️ Language challenges")
st.caption("Learn languages through levelled challenges")

conn = sqlite3.connect(DATABASE_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
challenges = conn.execute("""
    select challenges.id, challenges.name, challenges.category,
           count(activities.id) as activity_count
    from challenges
    left join activities on activities.challenge_id = challenges.id
    where challenges.category = 'Language'
    group by challenges.id
    order by challenges.name
""").fetchall()
conn.close()

if len(challenges) == 0:
    st.info("No language challenges yet.")

cols = st.columns(3)
number = 0


for challenge in challenges:
    with cols[number % 3]:

        st.image(get_challenge_image(challenge["name"], challenge["category"]), width="stretch")

        st.subheader(challenge["name"])
        
        st.caption(f"{challenge['activity_count']} activities")
        
        if st.button("Open", key=f"open_{challenge['id']}", type="primary", width="stretch"):
            st.session_state.selected_challenge_id = challenge["id"]
        
            st.switch_page("app_pages/challenge_details.py")
    number = number + 1
