import streamlit as st



st.set_page_config(page_title="Sport Tracker", layout="wide")




col1, col2, col3 = st.columns([1,2.5,1])

with col2:
    st.image("assets/sport_challenge.png", use_container_width=True)



selected_level = create_level_buttons("sports")
if selected_level:
    if selected_level == "beginner":
        challenge_data = BEGINNER_CHALLENGES[0]
    elif selected_level == "intermediate":
        challenge_data = INTERMEDIATE_CHALLENGES[0]
    else:
        challenge_data = ADVANCED_CHALLENGES[0]

    st.subheader(
        f"Day {challenge_data['day']} - {selected_level.capitalize()} Challenge"
    )
    display_sports_challenges(challenge_data["exercises"], selected_level)



st.title("Fitness Level Calculator")


st.write("Enter the number of reps or duration you can do:")

pushups = st.number_input("Push-ups (reps)", min_value=0, max_value=100, step=1)
squats = st.number_input("Squats (reps)", min_value=0, max_value=200, step=1)
plank = st.number_input("Plank hold (seconds)", min_value=0, max_value=600, step=5)

if st.button("Calculate Fitness Level"):

    
    score = pushups + squats + (plank // 10)

    if score < 50:
        level = "Beginner"
        st.warning(f"Your Fitness Level: {level}")
    elif 50 <= score < 120:
        level = "Intermediate"
        st.success(f"Your Fitness Level: {level}")
    else:
        level = "Advanced"
        st.success(f"Your Fitness Level: {level}")