import streamlit as st
import sqlite3


if "selected_nutrition_plans_id" not in st.session_state:
    st.switch_page("pages/view_nutrition_plan.py")




conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()
nutrition_plan = cursor.execute("SELECT * FROM Nutrition_Plans WHERE id = ?", (st.session_state.selected_nutrition_plans_id,)).fetchone()

conn.close()

st.title(f"Nutrition Plan Details")

with st.container():
    st.subheader("Nutrition Plan Information")
    st.text(f"BMI: {nutrition_plan[1]}")
    st.text(f"Category: {nutrition_plan[2]}")
    st.text(f"Goal: {nutrition_plan[3]}")
    st.text(f"Calories: {nutrition_plan[4]}")
    st.text(f"Breakfast: {nutrition_plan[5]}")
    st.text(f"Lunch: {nutrition_plan[6]}")
    st.text(f"Dinner: {nutrition_plan[7]}")
    st.text(f"Water Intake: {nutrition_plan[8]}")



    if st.button("Follow Plan"):
        st.success("Plan activated!")
        st.balloons()


