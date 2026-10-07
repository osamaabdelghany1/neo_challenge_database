import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

st.title("🏆 All challenges")
st.caption("Browse every challenge")

conn = sqlite3.connect(DATABASE_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
# Count each challenge's activities instead of storing the number, so it is always right.
challenges = conn.execute("""
    select challenges.id, challenges.name, challenges.category, challenges.duration,
           count(activities.id) as activity_count
    from challenges
    left join activities on activities.challenge_id = challenges.id
    group by challenges.id
    order by challenges.category, challenges.name
""").fetchall()
conn.close()

if len(challenges) == 0:
    st.info("No challenges yet.")

cols = st.columns(3)
number = 0
for challenge in challenges:
    with cols[number % 3]:
        with st.container(border=True):
            st.subheader(challenge["name"])
            st.caption(f"{challenge['category']} · {challenge['duration']} days · {challenge['activity_count']} activities")
            if st.button("Open", key=f"open_{challenge['id']}", type="primary", width="stretch"):
                st.session_state.selected_challenge_id = challenge["id"]
                st.switch_page("app_pages/challenge_details.py")
    number = number + 1
