import streamlit as st
import sqlite3
import os
import sys

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from assets.config import PAGE_CONFIG, PRIMARY_GREEN, PRIMARY_BLUE, DIFFICULTY_COLORS

# Page configuration
st.set_page_config(**PAGE_CONFIG)

# Load custom CSS
def load_css():
    css_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "styles.css")
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Custom theme
st.markdown(f"""
<style>
    .stApp {{
        background-color: #f7fafc;
    }}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(f"""
<div style='text-align: center; padding: 2rem 0;'>
    <h1 style='color: {PRIMARY_BLUE}; font-size: 3rem; margin-bottom: 0.5rem;'>💪 Fitness Challenge Hub</h1>
    <p style='color: #718096; font-size: 1.2rem;'>Your Complete Fitness & Nutrition Management System</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Database connection
conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

# Get statistics
cursor.execute("SELECT COUNT(*) FROM users")
user_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM challenges")
challenge_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM activities")
activity_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM Nutrition_Plans")
nutrition_count = cursor.fetchone()[0]

# Statistics section
st.markdown("### 📊 Dashboard Statistics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Total Users", user_count)
with col2:
    st.metric("🏆 Challenges", challenge_count)
with col3:
    st.metric("🏃 Activities", activity_count)
with col4:
    st.metric("🥗 Nutrition Plans", nutrition_count)

st.markdown("---")

# Featured challenges
st.markdown("### 🏆 Featured Challenges")
cursor.execute("""
SELECT id, name, number_of_levels, number_of_activities, category, description 
FROM challenges 
ORDER BY RANDOM() 
LIMIT 3
""")
featured_challenges = cursor.fetchall()

if featured_challenges:
    cols = st.columns(3)
    for i, challenge in enumerate(featured_challenges):
        with cols[i]:
            st.markdown(f"""
            <div style='background: white; padding: 1.5rem; border-radius: 12px; 
                     border: 1px solid #e2e8f0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <h3 style='color: {PRIMARY_BLUE}; margin-top: 0;'>{challenge[1]}</h3>
                <p style='color: #718096; font-size: 0.9rem;'>{challenge[5][:100]}...</p>
                <div style='margin-top: 1rem;'>
                    <span style='background: #ebf8ff; color: {PRIMARY_BLUE}; padding: 0.25rem 0.75rem; 
                             border-radius: 9999px; font-size: 0.8rem;'>{challenge[4]}</span>
                </div>
                <div style='margin-top: 0.5rem; color: #4a5568; font-size: 0.85rem;'>
                    📊 {challenge[2]} Levels | 🎯 {challenge[3]} Activities
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("View Details", key=f"featured_{i}", use_container_width=True):
                st.session_state.selected_challenge_id = challenge[0]
                st.switch_page("pages/challenge_details.py")

conn.close()

st.markdown("---")

# Quick navigation cards
st.markdown("### 🚀 Quick Navigation")

nav_col1, nav_col2, nav_col3 = st.columns(3)

with nav_col1:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, {PRIMARY_GREEN} 0%, {PRIMARY_BLUE} 100%); 
             padding: 2rem; border-radius: 12px; color: white; text-align: center;'>
        <h3 style='margin-top: 0;'>🏆 Challenges</h3>
        <p>View and manage fitness challenges</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Challenges", key="nav_challenges", use_container_width=True):
        st.switch_page("pages/view_challenges.py")

with nav_col2:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, {PRIMARY_BLUE} 0%, {PRIMARY_GREEN} 100%); 
             padding: 2rem; border-radius: 12px; color: white; text-align: center;'>
        <h3 style='margin-top: 0;'>🏃 Activities</h3>
        <p>Browse workout activities</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Activities", key="nav_activities", use_container_width=True):
        st.switch_page("pages/view_activities.py")

with nav_col3:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, {PRIMARY_GREEN} 0%, #00C9FF 100%); 
             padding: 2rem; border-radius: 12px; color: white; text-align: center;'>
        <h3 style='margin-top: 0;'>🥗 Nutrition</h3>
        <p>Plan your nutrition</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Nutrition", key="nav_nutrition", use_container_width=True):
        st.switch_page("pages/view_nutrition_plan.py")

st.markdown("---")

# Recent activity section
st.markdown("### 📋 Quick Actions")

action_col1, action_col2, action_col3, action_col4 = st.columns(4)

with action_col1:
    if st.button("➕ New Challenge", use_container_width=True):
        st.switch_page("pages/create_challenges.py")

with action_col2:
    if st.button("➕ New Activity", use_container_width=True):
        st.switch_page("pages/create_activities.py")

with action_col3:
    if st.button("➕ Nutrition Plan", use_container_width=True):
        st.switch_page("pages/create_nutration_plan.py")

with action_col4:
    if st.button("👤 View Users", use_container_width=True):
        st.switch_page("pages/view_users.py")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #718096; padding: 1rem;'>
    <p>💪 Fitness Challenge Hub © 2024 | Your Journey to Better Health Starts Here</p>
</div>
""", unsafe_allow_html=True)