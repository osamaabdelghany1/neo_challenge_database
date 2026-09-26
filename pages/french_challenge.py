import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH, DIFFICULTY_COLORS

st.set_page_config(page_title="French Challenge", page_icon="🇫🇷", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

def show_activities(challenge_id, difficulty):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("select id, name, description, difficulty from activities where challenge_id=? and difficulty=? order by name", (challenge_id, difficulty))
    acts = cursor.fetchall()
    conn.close()
    if acts:
        dc = DIFFICULTY_COLORS.get(difficulty, "#77ABB7")
        st.markdown(f"### {difficulty}")
        for act in acts:
            with st.container(border=True):
                st.markdown(f"<div style='display:flex;justify-content:space-between'><strong>{act[1]}</strong><span style='background:{dc};color:white;padding:0.2rem 0.5rem;border-radius:9999px;font-size:0.7rem'>{act[3]}</span></div>", unsafe_allow_html=True)
                st.caption(act[2][:100] + "...")
                if st.button("Start Activity", key=f"act_{act[0]}", use_container_width=True):
                    st.session_state.selected_activities_id = act[0]
                    st.switch_page("pages/_activites_details.py")
    else:
        st.info(f"No {difficulty} activities yet.")

header("🇫🇷 French Challenge", "Select difficulty level")
st.divider()

if "selected_challenge_id" in st.session_state:
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("select name from challenges where id=?", (st.session_state.selected_challenge_id,))
    ch = cursor.fetchone()
    conn.close()
    if ch:
        st.subheader(f"Challenge: {ch[0]}")
        for diff in ["Easy", "Medium", "Hard"]:
            show_activities(st.session_state.selected_challenge_id, diff)
    else:
        st.error("Challenge not found")
else:
    st.info("Select a challenge first from the Language Challenges page.")
    if st.button("Browse Language Challenges"):
        st.switch_page("pages/language_challenge.py")