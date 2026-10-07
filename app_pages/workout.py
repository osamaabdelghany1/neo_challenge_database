import streamlit as st

# Each equipment type: its name in the database, its picture, its title and a short line.
EQUIPMENT_TYPES = [
    ["Machine", "assets/machine.jpg", "🏭 Machines", "Build strength with gym equipment"],
    ["Free Weights", "assets/free_weights.jpg", "🏋️ Free weights", "Dumbbells and barbells for resistance"],
    ["Bodyweight", "assets/body.jpg", "🧘 Bodyweight", "Use your own body, no equipment needed"],
    ["Cable", "assets/cables.jpg", "🔗 Cables", "Cable machines for isolation exercises"],
]

st.title("💪 Your workout")
st.caption("Choose what you have to train with")

cols = st.columns(4)
number = 0
for equipment in EQUIPMENT_TYPES:
    with cols[number % 4]:
        with st.container(border=True):
            st.image(equipment[1], width="stretch")
            st.subheader(equipment[2])
            st.caption(equipment[3])
            if st.button("Show exercises", key=f"show_{equipment[0]}", type="primary", width="stretch"):
                # The Exercises page reads this to show only this equipment.
                st.session_state.equipment_filter = equipment[0]
                st.switch_page("app_pages/view_exercise.py")
    number = number + 1
