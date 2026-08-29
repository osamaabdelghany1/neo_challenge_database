import streamlit as st 
import sqlite3




st.set_page_config(page_title="View Nutrition Plan", page_icon="📊", layout="wide")

st.title("View Nutrition Plan")

conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

cursor.execute("""
select id, bmi, category, goal, calories, breakfast, lunch, dinner, water_intake, created_at from Nutrition_Plans order by created_at
""")

nutrition_plans = cursor.fetchall()
columns = [description[0] for description in cursor.description]

conn.close()


cols = st.columns(3)
for i, nutrition_plan in enumerate(nutrition_plans):

    with cols[i % 3]:
    
        with st.container():
            
            st.text(f"BMI: {nutrition_plan[1]}")
            st.text(f"Category: {nutrition_plan[2]}")
            st.text(f"Goal: {nutrition_plan[3]}")
            st.text(f"Calories: {nutrition_plan[4]}")
            st.text(f"Breakfast: {nutrition_plan[5]}")
            st.text(f"Lunch: {nutrition_plan[6]}")
            st.text(f"Dinner: {nutrition_plan[7]}")
            st.text(f"Water Intake: {nutrition_plan[8]}")
            
            if st.button("view details", use_container_width=True, key=f"view_details_{i}"):
                st.session_state.selected_nutrition_plans_id = nutrition_plan[0]
                st.switch_page("pages/nutrition_plan_details.py")







