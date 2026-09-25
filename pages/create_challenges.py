import streamlit as st
import sqlite3
import os
import sys

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from assets.config import PRIMARY_LIGHT, PRIMARY_DARK

# Load custom CSS
def load_css():
    css_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "styles.css")
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Header
st.markdown(f"""
<div style='text-align: center; padding: 2rem 0;'>
    <h1 style='color: {PRIMARY_DARK}; margin-bottom: 0.5rem;'>➕ Create Challenge</h1>
    <p style='color: #718096;'>Design a new fitness challenge</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Form
st.markdown(f"""
<div style='background: white; padding: 2rem; border-radius: 12px; 
         border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
    <h2 style='color: {PRIMARY_DARK}; margin-top: 0;'>Challenge Details</h2>
</div>
""", unsafe_allow_html=True)

# Form fields in two columns
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("🏆 Challenge Name")
    category = st.selectbox("📂 Category", ["Sports", "Language", "General Knowledge"])
    duration = st.number_input("⏱️ Duration (days)", min_value=1, max_value=365)

with col2:
    number_of_levels = st.number_input("📊 Number of Levels", min_value=1, max_value=10)
    number_of_activities = st.number_input("🎯 Number of Activities", min_value=1, max_value=100)

description = st.text_area("📝 Description", height=150)

st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Create Challenge", use_container_width=True):
        if not name or not number_of_levels or not number_of_activities or not category or not duration or not description:
            st.error("❌ Please enter all fields")
        else:
            conn = sqlite3.connect("database/database.db")
            cursor = conn.cursor()
            cursor.execute("""
            insert into challenges (name, number_of_levels, number_of_activities, category, duration, description)
            values(?, ?, ?, ?, ?, ?)
            """, (name, number_of_levels, number_of_activities, category, duration, description))
            conn.commit()
            conn.close()
            st.success("✅ Challenge created successfully")
            st.balloons()