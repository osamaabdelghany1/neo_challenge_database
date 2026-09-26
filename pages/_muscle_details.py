import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="Muscle Details", page_icon="💪", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

if "selected_muscle_id" not in st.session_state:
    st.switch_page("pages/view_muscles.py")

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
m = cursor.execute("select * from muscles where id=?", (st.session_state.selected_muscle_id,)).fetchone()
conn.close()

if not m:
    st.error("Muscle not found")
    st.stop()

header(f"💪 {m[1]}")
st.divider()

if m[11]:
    st.image(m[11], use_container_width=True)

c1, c2 = st.columns(2)
with c1:
    st.write(f"**Latin Name:** {m[2] or 'N/A'}")
    st.write(f"**Group:** {m[4]}")
    st.write(f"**Location:** {m[5]}")
    st.write(f"**Type:** {m[9] or 'N/A'}")
with c2:
    st.write(f"**Difficulty:** {m[10] or 'N/A'}")
    st.write(f"**Origin:** {m[6] or 'N/A'}")
    st.write(f"**Insertion:** {m[7] or 'N/A'}")

st.write(f"**Function:** {m[6]}")

st.divider()
if m[12]:
    st.subheader("Video")
    st.video(m[12])
else:
    st.info("No video available")

st.subheader("Exercises for this Muscle")
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
cursor.execute("select id, name, difficulty from exercises where muscle_id=? order by name", (m[0],))
exercises = cursor.fetchall()
conn.close()

if exercises:
    for ex in exercises:
        dc = {"Easy": "#77ABB7", "Medium": "#476D7C", "Hard": "#1D3E53"}.get(ex[2], "#77ABB7")
        with st.container(border=True):
            st.markdown(f"<div style='display:flex;justify-content:space-between'><strong>{ex[1]}</strong><span style='background:{dc};color:white;padding:0.2rem 0.5rem;border-radius:9999px;font-size:0.7rem'>{ex[2]}</span></div>", unsafe_allow_html=True)
            if st.button("View Exercise", key=f"mex_{ex[0]}", use_container_width=True):
                st.session_state.selected_exercise_id = ex[0]
                st.switch_page("pages/_exercise_details.py")
else:
    st.info("No exercises for this muscle yet")

if st.button("Back to Muscles", use_container_width=True):
    st.switch_page("pages/view_muscles.py")