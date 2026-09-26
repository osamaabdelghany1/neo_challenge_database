import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="View Users", page_icon="👥", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

header("👥 View Users", "Manage and view all registered users")
st.divider()

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
cursor.execute("select username, email, DOB, height, weight, phone from users order by created_at desc")
users = cursor.fetchall()
conn.close()

if not users:
    st.info("No users found")
else:
    cols = st.columns(3)
    for i, u in enumerate(users):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"<h3 style='color:{PRIMARY_DARK};margin:0'>{u[0]}</h3>", unsafe_allow_html=True)
                st.caption(f"Email: {u[1]}")
                st.write(f"📅 DOB: {u[2]}")
                st.write(f"📏 Height: {u[3]} cm")
                st.write(f"⚖️ Weight: {u[4]} kg")
                st.write(f"📱 Phone: {u[5]}")