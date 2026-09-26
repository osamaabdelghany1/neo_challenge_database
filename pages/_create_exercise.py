import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="Create Exercise", page_icon="➕", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

header("➕ Create Exercise", "Add a new exercise")
st.divider()

col1, col2 = st.columns(2)
with col1:
    muscle_id = st.number_input("Muscle ID", min_value=1)
    name = st.text_input("Exercise Name")
    equipment = st.text_input("Equipment Needed")
with col2:
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    video_url = st.text_input("Video URL")

description = st.text_area("Description", height=150)
st.divider()

if st.button("Create Exercise", use_container_width=True):
    if not muscle_id or not name:
        st.error("Muscle ID and Name are required")
    else:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("insert into exercises (muscle_id, name, description, equipment_needed, difficulty, video_url) values (?,?,?,?,?,?)",
                       (muscle_id, name, description, equipment, difficulty, video_url))
        conn.commit()
        conn.close()
        st.success("Exercise created!")
        st.balloons()