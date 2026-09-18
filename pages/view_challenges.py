import streamlit as st
import sqlite3
import os
import sys

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from assets.config import PAGE_CONFIG, DIFFICULTY_COLORS, CATEGORY_COLORS, PRIMARY_LIGHT, PRIMARY_DARK

st.set_page_config(page_title="View Challenges", page_icon="🏆", layout="wide")

# Load custom CSS
def load_css():
    css_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "styles.css")
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Header
st.markdown(f"""
<div style='padding: 1rem 0;'>
    <h1 style='color: {PRIMARY_DARK}; margin-bottom: 0.5rem;'>🏆 View Challenges</h1>
    <p style='color: #718096;'>Browse and explore all available fitness challenges</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

cursor.execute("""
select id, name, number_of_levels, number_of_activities, category from challenges order by name
""")

challenges = cursor.fetchall()
columns = [description[0] for description in cursor.description]

conn.close()



cols = st.columns(3)
for i, challenge in enumerate(challenges):

    with cols[i % 3]:
    
        category_color = CATEGORY_COLORS.get(challenge[4], PRIMARY_DARK)
        st.markdown(f"""
        <div style='background: white; padding: 1.5rem; border-radius: 12px; 
                 border: 1px solid #e2e8f0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); height: 100%;'>
            <h3 style='color: {PRIMARY_DARK}; margin-top: 0;'>{challenge[1]}</h3>
            <div style='margin: 0.75rem 0;'>
                <span style='background: {category_color}; color: white; padding: 0.25rem 0.75rem; 
                             border-radius: 9999px; font-size: 0.8rem;'>{challenge[4]}</span>
            </div>
            <div style='color: #4a5568; font-size: 0.9rem; line-height: 1.6;'>
                <div>📊 <strong>Levels:</strong> {challenge[2]}</div>
                <div>🎯 <strong>Activities:</strong> {challenge[3]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("View Details", use_container_width=True, key=f"view_details_{i}"):
            st.session_state.selected_challenge_id = challenge[0]
            st.switch_page("pages/challenge_details.py")






