import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH, LEVEL_ICONS

# This page needs an exercise picked on the Exercises page first.
if "selected_exercise_id" not in st.session_state:
    st.switch_page("pages/view_exercise.py")

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

col1, col2, col3 = st.columns(3)
col1.metric("Muscle", exercise["muscle_name"])
col2.metric("Equipment", exercise["equipment"])
col3.metric("Difficulty", LEVEL_ICONS[exercise["difficulty"]] + " " + exercise["difficulty"])

if exercise["description"]:
    st.write(exercise["description"])

if exercise["video_url"]:
    st.video(exercise["video_url"])
else:
    st.info("This exercise has no video yet.")

if st.button("Back to exercises", width="stretch"):
    st.switch_page("pages/view_exercise.py")
