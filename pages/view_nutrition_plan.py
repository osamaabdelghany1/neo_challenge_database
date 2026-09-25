import streamlit as st 
import sqlite3
import os
import sys

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from assets.config import PAGE_CONFIG, PRIMARY_LIGHT, PRIMARY_DARK

st.set_page_config(page_title="View Nutrition Plan", page_icon="🥗", layout="wide")

# Load custom CSS
def load_css():
    css_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "styles.css")
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Header
st.markdown(f"""
<div style='padding: 1rem 0;'>
    <h1 style='color: {PRIMARY_DARK}; margin-bottom: 0.5rem;'> View Nutrition Plans</h1>
    <p style='color: #718096;'>Browse and explore nutrition plans for different fitness goals</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

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
    
        goal_color = "#77ABB7" if nutrition_plan[3] == "Lose Weight" else "#476D7C" if nutrition_plan[3] == "Gain Weight" else PRIMARY_DARK
        category_bg = "#E8F4F6" if nutrition_plan[2] == "Normal" else "#F0F8FA" if nutrition_plan[2] == "Underweight" else "#FED7D7"
        
        st.markdown(f"""
        <div style='background: white; padding: 1.5rem; border-radius: 12px; 
                 border: 1px solid #e2e8f0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); height: 100%;'>
            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
                <h3 style='color: {PRIMARY_DARK}; margin: 0;'>BMI: {nutrition_plan[1]}</h3>
                <span style='background: {goal_color}; color: white; padding: 0.25rem 0.75rem; 
                             border-radius: 9999px; font-size: 0.8rem;'>{nutrition_plan[3]}</span>
            </div>
            <div style='background: {category_bg}; color: {PRIMARY_DARK}; padding: 0.5rem; 
                     border-radius: 8px; margin-bottom: 1rem; font-size: 0.9rem;'>
                <strong>Category:</strong> {nutrition_plan[2]}
            </div>
            <div style='color: #4a5568; font-size: 0.9rem; line-height: 1.6;'>
                <div>🔥 <strong>Calories:</strong> {nutrition_plan[4]} kcal</div>
                <div>💧 <strong>Water:</strong> {nutrition_plan[8]}</div>
                <div style='margin-top: 0.5rem;'>🍳 <strong>Breakfast:</strong> {nutrition_plan[5][:30]}...</div>
                <div>🍽️ <strong>Lunch:</strong> {nutrition_plan[6][:30]}...</div>
                <div>🌙 <strong>Dinner:</strong> {nutrition_plan[7][:30]}...</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("View Details", use_container_width=True, key=f"view_details_{i}"):
            st.session_state.selected_nutrition_plans_id = nutrition_plan[0]
            st.switch_page("pages/nutrition_plan_details.py")







