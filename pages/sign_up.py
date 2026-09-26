import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="Register", page_icon="📝", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

header("📝 Register", "Create your fitness account")
st.divider()

col1, col2 = st.columns(2)
with col1:
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    phone = st.text_input("Phone")
with col2:
    dob = st.date_input("Date of Birth")
    height = st.number_input("Height (cm)", min_value=0, max_value=300)
    weight = st.number_input("Weight (kg)", min_value=0, max_value=500)
    ssn = st.text_input("SSN")

st.divider()

if st.button("Register", use_container_width=True):
    if not all([username, password, email, dob, height, weight, phone, ssn]):
        st.error("Please fill in all fields")
    else:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        try:
            cursor.execute("insert into users (username, password, email, DOB, height, weight, phone, ssn) values (?,?,?,?,?,?,?,?)",
                           (username, password, email, dob, height, weight, phone, ssn))
            conn.commit()
            conn.close()
            st.success("Registered successfully!")
            st.balloons()
        except sqlite3.IntegrityError:
            conn.close()
            st.error("Email already exists")