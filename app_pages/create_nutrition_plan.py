import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

st.title("➕ Create nutrition plan")
st.caption("Add a meal plan for a BMI category")

col1, col2 = st.columns(2)
with col1:
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1)
    category = st.selectbox("Category", ["Underweight", "Normal", "Overweight", "Obese"])
    goal = st.selectbox("Goal", ["Lose Weight", "Gain Weight", "Maintain Weight", "Build Muscle"])
with col2:
    calories = st.number_input("Calories", min_value=1000, max_value=5000)
    water = st.text_input("Water intake", placeholder="2.5 Liters")
breakfast = st.text_area("Breakfast", height=80)
lunch = st.text_area("Lunch", height=80)
dinner = st.text_area("Dinner", height=80)

if st.button("Create nutrition plan", type="primary", width="stretch"):
    if water == "" or breakfast == "" or lunch == "" or dinner == "":
        st.error("Please fill in every field.")
    else:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute(
            "insert into nutrition_plans (bmi, category, goal, calories, breakfast, lunch, dinner, water_intake) values (?, ?, ?, ?, ?, ?, ?, ?)",
            (bmi, category, goal, calories, breakfast, lunch, dinner, water),
        )
        conn.commit()
        conn.close()
        st.success("Nutrition plan created!")
