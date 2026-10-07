import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

st.title("⭐ My challenges")
st.caption(f"Hi {st.session_state.username}! Here is everything you joined.")

conn = sqlite3.connect(DATABASE_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
challenges = conn.execute("""
    select challenges.*
    from user_challenges
    join challenges on challenges.id = user_challenges.challenge_id
    where user_challenges.user_id = ?
    order by challenges.name
""", (st.session_state.user_id,)).fetchall()
plan = conn.execute("""
    select nutrition_plans.*
    from user_nutrition_plans
    join nutrition_plans on nutrition_plans.id = user_nutrition_plans.nutrition_plan_id
    where user_nutrition_plans.user_id = ?
""", (st.session_state.user_id,)).fetchone()
conn.close()

st.subheader("Challenges")
if len(challenges) == 0:
    st.info("You have not joined a challenge yet. Open one and press Start challenge.")
for challenge in challenges:
    with st.container(border=True):
        st.markdown(f"**{challenge['name']}** · {challenge['category']} · {challenge['duration']} days")
        if st.button("Open", key=f"open_{challenge['id']}", type="primary", width="stretch"):
            st.session_state.selected_challenge_id = challenge["id"]
            st.switch_page("app_pages/challenge_details.py")

st.subheader("My nutrition plan")
if plan is None:
    st.info("You have not chosen a nutrition plan yet.")
else:
    with st.container(border=True):
        st.markdown(f"**BMI {plan['bmi']}** · {plan['category']} · Goal: {plan['goal']}")
        st.write(f"**Calories:** {plan['calories']} kcal · **Water:** {plan['water_intake']}")
        st.write(f"**Breakfast:** {plan['breakfast']}")
        st.write(f"**Lunch:** {plan['lunch']}")
        st.write(f"**Dinner:** {plan['dinner']}")
