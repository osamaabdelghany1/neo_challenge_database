import datetime
import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH, LEVEL_ICONS

# This page needs an exercise picked on the Exercises page first.
if "selected_exercise_id" not in st.session_state:
    st.switch_page("app_pages/view_exercise.py")

conn = sqlite3.connect(DATABASE_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
exercise = conn.execute("""
    select exercises.*, muscles.name as muscle_name
    from exercises join muscles on muscles.id = exercises.muscle_id
    where exercises.id = ?
""", (st.session_state.selected_exercise_id,)).fetchone()
conn.close()

if exercise is None:
    st.error("That exercise does not exist anymore.")
    st.stop()

st.title("💪 " + exercise["name"])

# Our videos were filmed on a phone held upright, so they are tall and narrow.
# A narrow column (1 part of 3) keeps the whole video on one screen, with the facts beside it.
# On a phone the two columns stack.
video_column, facts_column = st.columns([1, 2])
with video_column:
    if exercise["video_url"]:
        st.video(exercise["video_url"])
    else:
        st.info("This exercise has no video yet.")
with facts_column:
    st.metric("Muscle", exercise["muscle_name"])
    st.metric("Equipment", exercise["equipment"])
    st.metric("Difficulty", LEVEL_ICONS[exercise["difficulty"]] + " " + exercise["difficulty"])
    if exercise["description"]:
        st.write(exercise["description"])

    # Logged-in users can note that they did this exercise, once per day.
    if "user_id" in st.session_state:
        today = datetime.date.today().isoformat()
        conn = sqlite3.connect(DATABASE_PATH)
        conn.execute("PRAGMA foreign_keys = ON")
        done_today = conn.execute(
            "select 1 from exercise_logs where user_id = ? and exercise_id = ? and done_on = ?",
            (st.session_state.user_id, exercise["id"], today),
        ).fetchone()
        conn.close()
        if done_today:
            st.success("✅ Done today")
        elif st.button("I did this today", type="primary", width="stretch"):
            conn = sqlite3.connect(DATABASE_PATH)
            conn.execute("PRAGMA foreign_keys = ON")
            conn.execute(
                "insert into exercise_logs (user_id, exercise_id, done_on) values (?, ?, ?)",
                (st.session_state.user_id, exercise["id"], today),
            )
            conn.commit()
            conn.close()
            st.rerun()
    else:
        st.info("Log in to keep track of your workouts.")

if st.button("Back to exercises", type="primary", width="stretch"):
    st.switch_page("app_pages/view_exercise.py")
