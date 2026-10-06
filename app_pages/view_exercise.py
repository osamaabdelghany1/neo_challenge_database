import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH, LEVEL_ICONS

EQUIPMENT_CHOICES = ["All", "Machine", "Free Weights", "Bodyweight", "Cable"]

st.title("🎥 Exercises")
st.caption("Every exercise has a demonstration video")

# The Workout page may have picked an equipment type already (it sets "equipment_filter").
equipment = st.selectbox("Equipment", EQUIPMENT_CHOICES, key="equipment_filter")

conn = sqlite3.connect(DATABASE_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
if equipment == "All":
    exercises = conn.execute("""
        select exercises.*, muscles.name as muscle_name
        from exercises join muscles on muscles.id = exercises.muscle_id
        order by exercises.name
    """).fetchall()
else:
    exercises = conn.execute("""
        select exercises.*, muscles.name as muscle_name
        from exercises join muscles on muscles.id = exercises.muscle_id
        where exercises.equipment = ?
        order by exercises.name
    """, (equipment,)).fetchall()
conn.close()

if len(exercises) == 0:
    st.info("No exercises for this equipment yet.")

cols = st.columns(3)
number = 0
for exercise in exercises:
    with cols[number % 3]:
        with st.container(border=True):
            st.subheader(exercise["name"])
            st.caption(f"{exercise['muscle_name']} · {exercise['equipment']} · {LEVEL_ICONS[exercise['difficulty']]} {exercise['difficulty']}")
            if st.button("Watch", key=f"watch_{exercise['id']}", width="stretch"):
                st.session_state.selected_exercise_id = exercise["id"]
                st.switch_page("app_pages/exercise_details.py")
    number = number + 1
