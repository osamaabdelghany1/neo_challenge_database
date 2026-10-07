import datetime
import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

# How many recent exercises and quiz rounds to list.
RECENT_COUNT = 5

st.title("⭐ My challenges")
st.caption(f"Hi {st.session_state.username}! Here is how you are doing.")

user_id = st.session_state.user_id
# "This week" means today and the 6 days before it.
week_start = (datetime.date.today() - datetime.timedelta(days=6)).isoformat()

conn = sqlite3.connect(DATABASE_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
# Each joined challenge with how many activities it has and how many you ticked Done.
challenges = conn.execute("""
    select challenges.id, challenges.name, challenges.category,
           (select count(*) from activities where activities.challenge_id = challenges.id) as total,
           (select count(*) from user_activities
              join activities on activities.id = user_activities.activity_id
              where activities.challenge_id = challenges.id and user_activities.user_id = ?) as done
    from user_challenges
    join challenges on challenges.id = user_challenges.challenge_id
    where user_challenges.user_id = ?
    order by challenges.name
""", (user_id, user_id)).fetchall()
workouts_this_week = conn.execute(
    "select count(*) from exercise_logs where user_id = ? and done_on >= ?", (user_id, week_start)
).fetchone()[0]
recent_exercises = conn.execute("""
    select exercises.name, exercise_logs.done_on
    from exercise_logs join exercises on exercises.id = exercise_logs.exercise_id
    where exercise_logs.user_id = ?
    order by exercise_logs.done_on desc
    limit ?
""", (user_id, RECENT_COUNT)).fetchall()
best_scores = conn.execute(
    "select level, max(score) as best, total from quiz_results where user_id = ? group by level", (user_id,)
).fetchall()
recent_rounds = conn.execute(
    "select level, score, total, played_at from quiz_results where user_id = ? order by id desc limit ?",
    (user_id, RECENT_COUNT),
).fetchall()
plan = conn.execute("""
    select nutrition_plans.*
    from user_nutrition_plans
    join nutrition_plans on nutrition_plans.id = user_nutrition_plans.nutrition_plan_id
    where user_nutrition_plans.user_id = ?
""", (user_id,)).fetchone()
conn.close()

st.subheader("🏆 Challenges")
if len(challenges) == 0:
    st.info("You have not joined a challenge yet. Open one and press Start challenge.")
for challenge in challenges:
    with st.container(border=True):
        st.markdown(f"**{challenge['name']}** · {challenge['category']}")
        if challenge["total"] > 0:
            st.progress(challenge["done"] / challenge["total"], text=f"{challenge['done']} of {challenge['total']} activities done")
        else:
            st.caption("This challenge has no activities yet.")
        if st.button("Open", key=f"open_{challenge['id']}", type="primary", width="stretch"):
            st.session_state.selected_challenge_id = challenge["id"]
            st.switch_page("app_pages/challenge_details.py")

st.subheader("💪 Workouts")
st.metric("Exercises done this week", workouts_this_week)
if len(recent_exercises) == 0:
    st.info("Open an exercise video and press 'I did this today' to see it here.")
for exercise in recent_exercises:
    st.write(f"{exercise['done_on']} · {exercise['name']}")

st.subheader("🧠 Quiz scores")
if len(recent_rounds) == 0:
    st.info("Finish a general knowledge quiz to see your scores here.")
else:
    # Best score for each level, side by side.
    cols = st.columns(3)
    number = 0
    for level in ["Easy", "Medium", "Hard"]:
        best_text = "not played yet"
        for row in best_scores:
            if row["level"] == level:
                best_text = f"{row['best']} / {row['total']}"
        cols[number].metric(f"Best {level}", best_text)
        number = number + 1
    st.caption("Your last rounds")
    for quiz_round in recent_rounds:
        # played_at looks like "2026-10-07 14:03:21"; the first 10 letters are the date.
        st.write(f"{quiz_round['played_at'][:10]} · {quiz_round['level']} · {quiz_round['score']} / {quiz_round['total']}")

st.subheader("🥗 My nutrition plan")
if plan is None:
    st.info("You have not chosen a nutrition plan yet.")
else:
    with st.container(border=True):
        st.markdown(f"**BMI {plan['bmi']}** · {plan['category']} · Goal: {plan['goal']}")
        st.write(f"**Calories:** {plan['calories']} kcal · **Water:** {plan['water_intake']}")
        st.write(f"**Breakfast:** {plan['breakfast']}")
        st.write(f"**Lunch:** {plan['lunch']}")
        st.write(f"**Dinner:** {plan['dinner']}")
