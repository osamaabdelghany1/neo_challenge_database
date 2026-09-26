import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="Login", page_icon="🔐", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

header("🔐 Login", "Access your fitness account")
st.divider()

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login", use_container_width=True):
    if not email or not password:
        st.error("Please enter both email and password")
    else:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        user = cursor.execute("select * from users where email=? and password=?", (email, password)).fetchone()
        conn.close()
        if user:
            st.session_state.userId = user[0]
            st.success("Logged in successfully!")
            st.balloons()
        else:
            st.error("Invalid email or password")