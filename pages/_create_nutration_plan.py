import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="Create Nutrition Plan", page_icon="➕", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

header("➕ Create Nutrition Plan", "Design a personalized nutrition plan")
st.divider()

col1, col2 = st.columns(2)
with col1:
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1)
    category = st.selectbox("Category", ["Underweight", "Normal", "Overweight", "Obese"])
    goal = st.selectbox("Goal", ["Lose Weight", "Gain Weight", "Maintain Weight", "Build Muscle"])
    calories = st.number_input("Calories", min_value=1000, max_value=5000)
with col2:
    water = st.text_input("Water Intake")

breakfast = st.text_area("Breakfast", height=80)
lunch = st.text_area("Lunch", height=80)
dinner = st.text_area("Dinner", height=80)

st.divider()

if st.button("Create Nutrition Plan", use_container_width=True):
    if not bmi or not category or not goal or not calories or not breakfast or not lunch or not dinner or not water:
        st.error("Please enter all fields")
    else:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("insert into Nutrition_Plans (bmi, category, goal, calories, breakfast, lunch, dinner, water_intake) values (?,?,?,?,?,?,?,?)",
                       (bmi, category, goal, calories, breakfast, lunch, dinner, water))
        conn.commit()
        conn.close()
        st.success("Nutrition Plan created!")
        st.balloons()