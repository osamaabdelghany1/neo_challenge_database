import streamlit as st
import sqlite3
import os
import sys

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from assets.config import PRIMARY_GREEN, PRIMARY_BLUE

# Load custom CSS
def load_css():
    css_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "styles.css")
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Header
st.markdown(f"""
<div style='text-align: center; padding: 2rem 0;'>
    <h1 style='color: {PRIMARY_BLUE}; margin-bottom: 0.5rem;'>📝 Register</h1>
    <p style='color: #718096;'>Create your fitness account</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Registration form
st.markdown(f"""
<div style='background: white; padding: 2rem; border-radius: 12px; 
         border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
    <h2 style='color: {PRIMARY_BLUE}; margin-top: 0;'>Create Account</h2>
</div>
""", unsafe_allow_html=True)

# Form fields in two columns
col1, col2 = st.columns(2)

with col1:
    username = st.text_input("👤 Username")
    email = st.text_input("📧 Email")
    password = st.text_input("🔒 Password", type="password")
    phone = st.text_input("📱 Phone")

with col2:
    dob = st.date_input("🎂 Date of Birth")
    height = st.number_input("📏 Height (cm)", min_value=0, max_value=300)
    weight = st.number_input("⚖️ Weight (kg)", min_value=0, max_value=500)
    ssn = st.text_input("🆔 SSN")


st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Register", use_container_width=True):
        if not username or not password or not email or not dob or not height or not weight or not phone or not ssn:
            st.error("❌ Please fill in all fields")
        else:
            conn = sqlite3.connect("database/database.db")
            cursor = conn.cursor()
            try:
                cursor.execute("""
                insert into users (username, password, email, DOB, height, weight, phone, ssn)
                values(?, ?, ?, ?, ?, ?, ?, ?)
                """, (username, password, email, dob, height, weight, phone, ssn))
                conn.commit()
                conn.close()
                st.success("✅ User registered successfully")
                st.balloons()
            except sqlite3.IntegrityError:
                conn.close()
                st.error("❌ Email already exists")

