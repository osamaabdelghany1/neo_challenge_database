import streamlit as st
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="Your Workout", page_icon="💪", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

header("Your Workout", "Choose equipment type to see exercises")

c1, c2 = st.columns(2)
with c1:
    with st.container(border=True):
        st.image("assets/machine.jpg", use_container_width=True)
        st.markdown(f"<h3 style='color:{PRIMARY_DARK};margin:0.5rem 0'>🏭 Machines</h3>", unsafe_allow_html=True)
        st.caption("Build strength with gym equipment")
        if st.button("View Machine Exercises", use_container_width=True):
            st.session_state.equipment_filter = "machine"
            st.switch_page("pages/view_exercise.py")

    with st.container(border=True):
        st.image("assets/body.jpg", use_container_width=True)
        st.markdown(f"<h3 style='color:{PRIMARY_DARK};margin:0.5rem 0'>🧘 Bodyweight</h3>", unsafe_allow_html=True)
        st.caption("Use your body weight for exercises")
        if st.button("View Bodyweight Exercises", use_container_width=True):
            st.session_state.equipment_filter = "bodyweight"
            st.switch_page("pages/view_exercise.py")

with c2:
    with st.container(border=True):
        st.image("assets/free_weights.jpg", use_container_width=True)
        st.markdown(f"<h3 style='color:{PRIMARY_DARK};margin:0.5rem 0'>🏋️ Free Weights</h3>", unsafe_allow_html=True)
        st.caption("Dumbbells and barbells for resistance")
        if st.button("View Free Weight Exercises", use_container_width=True):
            st.session_state.equipment_filter = "free weights"
            st.switch_page("pages/view_exercise.py")

    with st.container(border=True):
        st.image("assets/cables.jpg", use_container_width=True)
        st.markdown(f"<h3 style='color:{PRIMARY_DARK};margin:0.5rem 0'>🔗 Cables</h3>", unsafe_allow_html=True)
        st.caption("Cable machines for isolation exercises")
        if st.button("View Cable Exercises", use_container_width=True):
            st.session_state.equipment_filter = "cable"
            st.switch_page("pages/view_exercise.py")