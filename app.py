import streamlit as st

pg = st.navigation({
    "Home": [
        st.Page("pages/home.py", title="Home", icon="✨", default=True),
    ],
    "Challenges": [
        st.Page("pages/view_challenges.py", title="All Challenges", icon="🏆"),
        st.Page("pages/sport-challenge.py", title="Sports by Level", icon="🏋️"),
        st.Page("pages/language_challenge.py", title="Language Challenges", icon="🗣️"),
        st.Page("pages/general_knowledge.py", title="General Knowledge Quiz", icon="🧠"),
        st.Page("pages/view_activities.py", title="Activities", icon="🏃"),
        st.Page("pages/challenge_details.py", title="Challenge Details", visibility="hidden"),
        st.Page("pages/_activites_details.py", title="Activity Details", visibility="hidden"),
    ],
    "Train": [
        st.Page("pages/workout.py", title="Workout", icon="💪"),
        st.Page("pages/view_exercise.py", title="Exercises", icon="🎥"),
        st.Page("pages/view_muscles.py", title="Muscles", icon="🦵"),
        st.Page("pages/_exercise_details.py", title="Exercise Details", visibility="hidden"),
        st.Page("pages/_muscle_details.py", title="Muscle Details", visibility="hidden"),
    ],
    "Nutrition": [
        st.Page("pages/view_nutrition_plan.py", title="Nutrition Plans", icon="🥗"),
        st.Page("pages/_nutrition_plan_details.py", title="Nutrition Plan Details", visibility="hidden"),
    ],
    "Account": [
        st.Page("pages/login.py", title="Log In", icon="🔐"),
        st.Page("pages/sign_up.py", title="Sign Up", icon="📝"),
    ],
    "Admin": [
        st.Page("pages/view_users.py", title="Users", icon="👥"),
        st.Page("pages/_create_challenges.py", title="Create Challenge", icon="➕"),
        st.Page("pages/_create_activities.py", title="Create Activity", icon="➕"),
        st.Page("pages/_create_exercise.py", title="Create Exercise", icon="➕"),
        st.Page("pages/_create_muscles.py", title="Create Muscle", icon="➕"),
        st.Page("pages/_create_nutration_plan.py", title="Create Nutrition Plan", icon="➕"),
    ],
})
pg.run()