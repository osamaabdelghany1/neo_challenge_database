import streamlit as st 
import sqlite3




st.set_page_config(page_title="View Nutration Plan", page_icon="📊", layout="wide")

st.title("View Nutration Plan")

conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

cursor.execute("""
select bmi, category, goal, calories, breakfast, lunch, dinner, water_intake, created_at from Nutrition_Plans order by created_at
""")

challenges = cursor.fetchall()
columns = [description[0] for description in cursor.description]

conn.close()


cols = st.columns(3)
for i, challenge in enumerate(challenges):

    with cols[i % 3]:
    
        with st.container():
            
            st.text("BMI: {challenge[0]}")
            st.text(f"Category: {challenge[1]}")
            st.text(f"Goal: {challenge[2]}")
            st.text(f"Calories: {challenge[3]}")
            st.text(f"Breakfast: {challenge[4]}")
            st.text(f"Lunch: {challenge[5]}")
            st.text(f"Dinner: {challenge[6]}")
            st.text(f"Water Intake: {challenge[7]}")
            
            st.button("view details", use_container_width=True, key=f"view_details_{challenge[0]}")






