import streamlit as st
import sqlite3
import os
import sys

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from assets.config import PRIMARY_LIGHT, PRIMARY_DARK

# Load custom CSS
def load_css():
    css_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "styles.css")
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Header
st.markdown(f"""
<div style='text-align: center; padding: 2rem 0;'>
    <h1 style='color: {PRIMARY_DARK}; margin-bottom: 0.5rem;'>➕ Create Nutrition Plan</h1>
    <p style='color: #718096;'>Design a personalized nutrition plan</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Form
st.markdown(f"""
<div style='background: white; padding: 2rem; border-radius: 12px; 
         border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
    <h2 style='color: {PRIMARY_DARK}; margin-top: 0;'>Nutrition Plan Details</h2>
</div>
""", unsafe_allow_html=True)

# Form fields in two columns
col1, col2 = st.columns(2)

with col1:
    bmi = st.number_input("⚖️ BMI", min_value=10.0, max_value=50.0, step=0.1)
    category = st.selectbox("📂 Category", ["Underweight", "Normal", "Overweight", "Obese"])
    goal = st.selectbox("🎯 Goal", ["Lose Weight", "Gain Weight", "Maintain Weight", "Build Muscle"])
    calories = st.number_input("🔥 Calories", min_value=1000, max_value=5000)

with col2:
    water_intake = st.text_input("💧 Water Intake")

breakfast = st.text_area("🍳 Breakfast", height=80)
lunch = st.text_area("🍽️ Lunch", height=80)
dinner = st.text_area("🌙 Dinner", height=80)

st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Create Nutrition Plan", use_container_width=True):
        if not bmi or not category or not goal or not calories or not breakfast or not lunch or not dinner or not water_intake:
            st.error("❌ Please enter all fields")
        else:
            conn = sqlite3.connect("database/database.db")
            cursor = conn.cursor()
            cursor.execute("""
            insert into Nutrition_Plans (bmi, category, goal, calories, breakfast, lunch, dinner, water_intake)
            values( ?, ?, ?, ?, ?, ?, ?, ?)
            """, (bmi, category, goal, calories, breakfast, lunch, dinner, water_intake))
            conn.commit()
            conn.close()
            st.success("✅ Nutrition Plan created successfully")
            st.balloons()
