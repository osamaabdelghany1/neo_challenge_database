import streamlit as st
import os
import sys

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from assets.config import PRIMARY_LIGHT, PRIMARY_MEDIUM, PRIMARY_DARK

# Load custom CSS
def load_css():
    css_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "styles.css")
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()



st.set_page_config(page_title="Sport Tracker", layout="wide")




col1, col2, col3 = st.columns([1,2.5,1])

with col2:
    st.image("assets/sport_challenge.png", use_container_width=True)


st.title("choose your level") 
  
# Add custom CSS for specific button colors
st.markdown(f"""
<style>
div[data-testid="stHorizontalBlock"] > div:nth-child(1) > div > div > button {{
    background: {PRIMARY_LIGHT} !important;
}}
div[data-testid="stHorizontalBlock"] > div:nth-child(2) > div > div > button {{
    background: {PRIMARY_MEDIUM} !important;
}}
div[data-testid="stHorizontalBlock"] > div:nth-child(3) > div > div > button {{
    background: {PRIMARY_DARK} !important;
}}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Beginner", use_container_width=True):
        st.session_state.selected_level = "beginner"
with col2:
    if st.button("Intermediate", use_container_width=True):
        st.session_state.selected_level = "intermediate"
with col3:
    if st.button("Advanced", use_container_width=True):
        st.session_state.selected_level = "advanced"




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