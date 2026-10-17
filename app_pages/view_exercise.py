import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH, LEVEL_ICONS

EQUIPMENT_CHOICES = ["All", "Machine", "Free Weights", "Bodyweight", "Cable"]
LEVEL_CHOICES = ["All", "Easy", "Medium", "Hard"]




st.title("Fitness Level Calculator")


st.write("Enter the number of reps or duration you can do:")

pushups = st.number_input("Push-ups (reps)", min_value=0, max_value=100, step=1)
squats = st.number_input("Squats (reps)", min_value=0, max_value=200, step=1)
plank = st.number_input("Plank hold (seconds)", min_value=0, max_value=600, step=5)

if st.button("Calculate my fitness level", type="primary", width="stretch"):

    
    score = pushups + squats + (plank // 10)

    if score < 50:
        level = "Easy"
        st.warning(f"Your Fitness Level: {level}")
    elif 50 <= score < 120:
        level = "Medium"
        st.success(f"Your Fitness Level: {level}")
    else:
        level = "Hard"
        st.success(f"Your Fitness Level: {level}")





st.title("🎥 Exercises")
st.caption("Every exercise has a demonstration video")

conn = sqlite3.connect(DATABASE_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
exercises = conn.execute("""
    select exercises.*, muscles.name as muscle_name
    from exercises join muscles on muscles.id = exercises.muscle_id
    order by exercises.name
""").fetchall()
muscles = conn.execute("select name from muscles order by name").fetchall()
conn.close()

# The Workout page may have picked an equipment type already (it sets "equipment_filter").
if "equipment_filter" not in st.session_state:
    st.session_state.equipment_filter = "All"
equipment = st.pills("Equipment", EQUIPMENT_CHOICES, required=True, key="equipment_filter")
level = st.pills("Level", LEVEL_CHOICES, default="All", required=True)

muscle_choices = ["All muscles"]
for muscle in muscles:
    muscle_choices.append(muscle["name"])
muscle_name = st.selectbox("Muscle", muscle_choices)

# Keep only the exercises that match every filter.
shown = []
for exercise in exercises:
    if equipment != "All" and exercise["equipment"] != equipment:
        continue
    if level != "All" and exercise["difficulty"] != level:
        continue
    if muscle_name != "All muscles" and exercise["muscle_name"] != muscle_name:
        continue
    shown.append(exercise)

st.caption(f"Showing {len(shown)} exercises")
if len(shown) == 0:
    st.info("No exercises match these filters. Try picking All.")

cols = st.columns(4)
number = 0
for exercise in shown:
    with cols[number % 4]:
        with st.container(border=True):
            if exercise["thumbnail_url"]:
                st.image(exercise["thumbnail_url"], width="stretch")
            else:
                st.caption("No picture yet")
            st.markdown(f"**{exercise['name']}**")
            st.caption(f"{exercise['muscle_name']} · {exercise['equipment']} · {LEVEL_ICONS[exercise['difficulty']]} {exercise['difficulty']}")
            if st.button("Watch", key=f"watch_{exercise['id']}", type="primary", width="stretch"):
                st.session_state.selected_exercise_id = exercise["id"]
                st.switch_page("app_pages/exercise_details.py")
    number = number + 1
