import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

# The files that fill an empty database.
# The order matters: activities and questions need their challenges to exist first,
# and exercises need their muscles.
SEED_FILES = [
    "database/insert_challenges.sql",
    "database/insert_activities.sql",
    "database/insert_general_knowledge.sql",
    "database/insert_muscles.sql",
    "database/insert_exercise.sql",
    "database/insert_nutrition_plan.sql",
]


def create_tables():
    conn = sqlite3.connect(DATABASE_PATH)
    # Make SQLite check that every link (like an activity's challenge) points at a real row.
    conn.execute("PRAGMA foreign_keys = ON")
    with open("database/schema.sql") as file:
        conn.executescript(file.read())

    # A brand-new database has no challenges yet, so fill it with our starting content.
    challenge_count = conn.execute("select count(*) from challenges").fetchone()[0]
    if challenge_count == 0:
        for path in SEED_FILES:
            with open(path) as file:
                conn.executescript(file.read())
    conn.close()


st.set_page_config(page_title="NEO Challenge", page_icon="✨", layout="wide")
create_tables()

home = st.Page("pages/home.py", title="Home", icon="🏠", default=True)
all_challenges = st.Page("pages/view_challenges.py", title="All challenges", icon="🏆")
language_challenges = st.Page("pages/language_challenge.py", title="Language challenges", icon="🗣️")
quiz = st.Page("pages/general_knowledge.py", title="General knowledge quiz", icon="🧠")
workout = st.Page("pages/workout.py", title="Workout", icon="💪")
exercises = st.Page("pages/view_exercise.py", title="Exercises", icon="🎥")
muscles = st.Page("pages/view_muscles.py", title="Muscles", icon="🦵")
nutrition = st.Page("pages/view_nutrition_plan.py", title="Nutrition plans", icon="🥗")

# Detail pages are opened by buttons, so they are hidden from the menu.
challenge_details = st.Page("pages/challenge_details.py", title="Challenge", visibility="hidden")
exercise_details = st.Page("pages/exercise_details.py", title="Exercise", visibility="hidden")

menu = {
    "Home": [home],
    "Challenges": [all_challenges, language_challenges, quiz, challenge_details],
    "Train": [workout, exercises, muscles, exercise_details],
    "Nutrition": [nutrition],
}

# The menu only shows what you can open right now.
if "user_id" in st.session_state:
    menu["My account"] = [
        st.Page("pages/my_challenges.py", title="My challenges", icon="⭐"),
        st.Page("pages/logout.py", title="Log out", icon="🚪"),
    ]
else:
    menu["Account"] = [
        st.Page("pages/login.py", title="Log in", icon="🔐"),
        st.Page("pages/sign_up.py", title="Sign up", icon="📝"),
    ]

if st.session_state.get("is_admin"):
    menu["Admin"] = [
        st.Page("pages/view_users.py", title="Users", icon="👥"),
        st.Page("pages/create_challenge.py", title="Create challenge", icon="➕"),
        st.Page("pages/create_activity.py", title="Create activity", icon="➕"),
        st.Page("pages/create_exercise.py", title="Create exercise", icon="➕"),
        st.Page("pages/create_muscle.py", title="Create muscle", icon="➕"),
        st.Page("pages/create_nutrition_plan.py", title="Create nutrition plan", icon="➕"),
    ]

page = st.navigation(menu)
page.run()
