import streamlit as st
import sqlite3
import os
import sys

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from assets.config import DIFFICULTY_COLORS, PRIMARY_GREEN, PRIMARY_BLUE

# Load custom CSS
def load_css():
    css_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "styles.css")
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Header
st.markdown(f"""
<div style='padding: 1rem 0;'>
    <h1 style='color: {PRIMARY_BLUE}; margin-bottom: 0.5rem;'>🏃 View Activities</h1>
    <p style='color: #718096;'>Browse all workout activities and exercises</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

cursor.execute("""
select id, name, description, category, difficulty from activities order by name
""")

activities = cursor.fetchall()

conn.close()



cols = st.columns(3)
for i, activity in enumerate(activities):

    with cols[i % 3]:
    
        difficulty_color = DIFFICULTY_COLORS.get(activity[4], PRIMARY_GREEN)
        st.markdown(f"""
        <div style='background: white; padding: 1.5rem; border-radius: 12px; 
                 border: 1px solid #e2e8f0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); height: 100%;'>
            <h3 style='color: {PRIMARY_BLUE}; margin-top: 0;'>{activity[1]}</h3>
            <div style='margin: 0.75rem 0;'>
                <span style='background: {difficulty_color}; color: white; padding: 0.25rem 0.75rem; 
                             border-radius: 9999px; font-size: 0.8rem;'>{activity[4]}</span>
                <span style='background: #E6F7FF; color: {PRIMARY_BLUE}; padding: 0.25rem 0.75rem; 
                             border-radius: 9999px; font-size: 0.8rem; margin-left: 0.5rem;'>{activity[3]}</span>
            </div>
            <div style='color: #4a5568; font-size: 0.9rem; line-height: 1.6;'>
                <div>📝 <strong>Description:</strong> {activity[2]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("View Details", use_container_width=True, key=f"view_details_{i}"):
            st.session_state.selected_activities_id = activity[0]
            st.switch_page("pages/activites_details.py")



