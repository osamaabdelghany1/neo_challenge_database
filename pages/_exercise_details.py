import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="Exercise Details", page_icon="💪", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

if "selected_exercise_id" not in st.session_state:
    st.switch_page("pages/view_exercise.py")

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
ex = cursor.execute("select * from exercises where id=?", (st.session_state.selected_exercise_id,)).fetchone()
conn.close()

if not ex:
    st.error("Exercise not found")
    st.stop()

header(f"💪 {ex[2]}")
st.divider()

c1, c2 = st.columns(2)
with c1:
    st.metric("Muscle ID", ex[1])
    st.metric("Equipment", ex[4] or "None")
with c2:
    st.metric("Difficulty", ex[5])

st.write(f"**Description:** {ex[3] or 'No description'}")

st.divider()
if ex[6]:
    st.subheader("Video")
    st.video(ex[6])
else:
    st.info("No video available")

if st.button("Back to Exercises", use_container_width=True):
    st.switch_page("pages/view_exercise.py")