import streamlit as st
import os
import sys

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from assets.config import PRIMARY_DARK, PRIMARY_LIGHT

st.set_page_config(page_title="Your Workout", page_icon="💪", layout="wide")

# Load custom CSS
def load_css():
    css_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "styles.css")
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

st.title("Your Workout")



c1, c2 = st.columns(2)
with c1:

    st.header("Machines")
    st.image("assets/machine.jpg", use_container_width=True)
    st.write("Build strength with gym equipment")
    st.button("Select", key="machines", use_container_width=True)

    st.header("Body weights")
    st.image("assets/body.jpg", use_container_width=True)
    st.write("Use your body weight for exercises")
    st.button("Select", key="body_weights", use_container_width=True)

with c2:
    st.header("Free weights")
    st.image("assets/free_weights.jpg", use_container_width=True)
    st.write("Dumbbells and barbells for resistance")
    st.button("Select", key="free_weights", use_container_width=True)

    st.header("Cables")
    st.image("assets/cables.jpg", use_container_width=True)
    st.write("Cable machines for isolation exercises")
    st.button("Select", key="cables", use_container_width=True)



