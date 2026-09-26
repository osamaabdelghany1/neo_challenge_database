import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="Create Activity", page_icon="➕", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

header("➕ Create Activity", "Add a new workout activity")
st.divider()

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Activity Name")
    category = st.selectbox("Category", ["Sports", "Language", "General Knowledge"])
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
with col2:
    challenge_id = st.number_input("Challenge ID", min_value=1)

description = st.text_area("Description", height=150)
st.divider()

if st.button("Create Activity", use_container_width=True):
    if not name or not description or not category or not difficulty or not challenge_id:
        st.error("Please enter all fields")
    else:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("insert into activities (name, description, category, difficulty, challenge_id) values (?,?,?,?,?)",
                       (name, description, category, difficulty, challenge_id))
        conn.commit()
        conn.close()
        st.success("Activity created!")
        st.balloons()