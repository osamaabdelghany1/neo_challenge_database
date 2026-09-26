import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DIFFICULTY_COLORS, DATABASE_PATH

st.set_page_config(page_title="View Exercises", page_icon="💪", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

header("💪 View Exercises", "Browse all exercises")

if st.session_state.get("equipment_filter"):
    ef = st.session_state.equipment_filter
    st.markdown(f"<div style='background:#E8F4F6;padding:1rem;border-radius:8px;margin-bottom:1rem'><strong>Filter:</strong> {ef.title()} Exercises</div>", unsafe_allow_html=True)
    if st.button("Clear Filter", use_container_width=True):
        st.session_state.equipment_filter = None
        st.rerun()

st.divider()

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
ef = st.session_state.get("equipment_filter")
if ef:
    cursor.execute("select id, name, equipment_needed, difficulty from exercises where lower(equipment_needed) like ? order by name", (f"%{ef.lower()}%",))
else:
    cursor.execute("select id, name, equipment_needed, difficulty from exercises order by name")
exercises = cursor.fetchall()
conn.close()

if not exercises:
    st.info("No exercises found" + (f" for {ef}" if ef else ""))
else:
    cols = st.columns(3)
    for i, ex in enumerate(exercises):
        with cols[i % 3]:
            dc = DIFFICULTY_COLORS.get(ex[3], "#77ABB7")
            with st.container(border=True):
                st.markdown(f"<h3 style='color:{PRIMARY_DARK};margin:0'>{ex[1]}</h3>", unsafe_allow_html=True)
                st.caption(f"Equipment: {ex[2] or 'N/A'} · {ex[3]}")
                if st.button("View Details", key=f"ve_{i}", use_container_width=True):
                    st.session_state.selected_exercise_id = ex[0]
                    st.switch_page("pages/_exercise_details.py")