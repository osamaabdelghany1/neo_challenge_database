import streamlit as st
import sqlite3


st.title("Add Nutrition Plan")

bmi = st.number_input("BMI")
category = st.text_input("Category")
goal = st.text_input("Goal")
calories = st.number_input("Calories")
breakfast = st.text_input("Breakfast")
lunch = st.text_input("Lunch")
dinner = st.text_input("Dinner")
water_intake = st.text_input("Water Intake")

if st.button("Create Nutrition Plan", use_container_width=True):
    if not bmi or not category or not goal or not calories or not breakfast or not lunch or not dinner or not water_intake:
        st.error("Please enter a valid info")
    else:
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        cursor.execute("""
        insert into Nutrition_Plans (bmi, category, goal, calories, breakfast, lunch, dinner, water_intake)
        values( ?, ?, ?, ?, ?, ?, ?, ?)
        """, (bmi, category, goal, calories, breakfast, lunch, dinner, water_intake))
        conn.commit()
        conn.close()
        st.success("Nutrition Plan created successfully")
