import streamlit as st
import sqlite3
import os
import sys

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from assets.config import PAGE_CONFIG, PRIMARY_BLUE

st.set_page_config(page_title="View Users", page_icon="👥", layout="wide")

# Load custom CSS
def load_css():
    css_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "styles.css")
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Header
st.markdown(f"""
<div style='padding: 1rem 0;'>
    <h1 style='color: {PRIMARY_BLUE}; margin-bottom: 0.5rem;'>👥 View Users</h1>
    <p style='color: #718096;'>Manage and view all registered users</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

conn = sqlite3.connect("database/database.db")

cursor = conn.cursor()


cursor.execute("""
select 
    username, 
    email, 
    DOB, 
    height, 
    weight, 
    phone, 
    ssn 
from users 
order by created_at 
desc
""")

users = cursor.fetchall()

conn.close()


cols = st.columns(3)
for i, user in enumerate(users):

    with cols[i % 3]:
    
        st.markdown(f"""
        <div style='background: white; padding: 1.5rem; border-radius: 12px; 
                 border: 1px solid #e2e8f0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); height: 100%;'>
            <h3 style='color: {PRIMARY_BLUE}; margin-top: 0;'>👤 {user[0]}</h3>
            <div style='color: #4a5568; font-size: 0.9rem; line-height: 1.6;'>
                <div>📧 <strong>Email:</strong> {user[1]}</div>
                <div>🎂 <strong>DOB:</strong> {user[2]}</div>
                <div>📏 <strong>Height:</strong> {user[3]} cm</div>
                <div>⚖️ <strong>Weight:</strong> {user[4]} kg</div>
                <div>📱 <strong>Phone:</strong> {user[5]}</div>
                <div>🆔 <strong>SSN:</strong> {user[6]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
