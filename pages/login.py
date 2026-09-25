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
    <h1 style='color: {PRIMARY_DARK}; margin-bottom: 0.5rem;'>🔐 Login</h1>
    <p style='color: #718096;'>Access your fitness account</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Login form
st.markdown(f"""
<div style='background: white; padding: 2rem; border-radius: 12px; 
         border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
    <h2 style='color: {PRIMARY_DARK}; margin-top: 0;'>Sign In</h2>
</div>
""", unsafe_allow_html=True)

email = st.text_input("📧 Email")
password = st.text_input("🔒 Password", type="password")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Login", use_container_width=True):
        if not email or not password:
            st.error("Please enter both email and password")
        else:
            conn = sqlite3.connect("database/database.db")
            cursor = conn.cursor()
            cursor.execute("""
            select * from users where email = ? and password = ?
            """, (email, password))
            user = cursor.fetchone()
            conn.close()
            if user:
                st.session_state.userId = user[0]
                st.success("✅ User logged in successfully")
                st.balloons()
            else:
                st.error("❌ Invalid email or password")
