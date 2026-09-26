import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, PRIMARY_LIGHT, DIFFICULTY_COLORS, CATEGORY_COLORS, DATABASE_PATH

st.set_page_config(page_title="Sport Tracker", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

col1, col2, col3 = st.columns([1, 2.5, 1])
with col2:
    st.image("assets/sport_challenge.png", use_container_width=True)

header("Choose Your Level")

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("Beginner", use_container_width=True):
        st.session_state.selected_level = "Beginner"
with c2:
    if st.button("Intermediate", use_container_width=True):
        st.session_state.selected_level = "Intermediate"
with c3:
    if st.button("Advanced", use_container_width=True):
        st.session_state.selected_level = "Advanced"

level_to_diff = {"Beginner": "Easy", "Intermediate": "Medium", "Advanced": "Hard"}

if "selected_level" in st.session_state:
    diff = level_to_diff[st.session_state.selected_level]
    dc = DIFFICULTY_COLORS.get(diff, PRIMARY_LIGHT)
    st.markdown(f"<div style='background:{dc};color:white;padding:1rem;border-radius:8px;margin:1rem 0;text-align:center'><strong>Selected:</strong> {st.session_state.selected_level} → Showing <strong>{diff}</strong> challenges</div>", unsafe_allow_html=True)

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("select id, name from challenges where category='Sports' order by name")
    challenges = cursor.fetchall()
    conn.close()

    if challenges:
        challenge_ids = [c[0] for c in challenges]
        placeholders = ','.join(['?'] * len(challenge_ids))
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute(f"select c.id, c.name, a.difficulty from challenges c left join activities a on c.id=a.challenge_id where c.id in ({placeholders})", challenge_ids)
        results = cursor.fetchall()
        conn.close()

        from collections import defaultdict
        by_challenge = defaultdict(list)
        for r in results:
            by_challenge[r[0]].append(r[2])

        if st.button(f"View {diff} Sports Challenges", use_container_width=True):
            st.session_state.fitness_level_filter = diff
            st.switch_page("pages/view_challenges.py")

        st.subheader("Available Challenges")
        for ch in challenges:
            matching = [d for d in by_challenge.get(ch[0], []) if d == diff]
            with st.expander(f"{ch[1]} - {len(matching)} {diff} activities"):
                st.write(f"**Category:** Sports")
                if matching:
                    st.write(f"Has {len(matching)} {diff} activities")
                else:
                    st.write(f"No {diff} activities yet")

st.divider()
header("Fitness Level Calculator", "Enter the number of reps or duration you can do")

pushups = st.number_input("Push-ups (reps)", min_value=0, max_value=100, step=1)
squats = st.number_input("Squats (reps)", min_value=0, max_value=200, step=1)
plank = st.number_input("Plank hold (seconds)", min_value=0, max_value=600, step=5)

if st.button("Calculate Fitness Level"):
    score = pushups + squats + (plank // 10)
    if score < 50:
        level = "Beginner"
        st.warning(f"Your Fitness Level: {level}")
    elif score < 120:
        level = "Intermediate"
        st.success(f"Your Fitness Level: {level}")
    else:
        level = "Advanced"
        st.success(f"Your Fitness Level: {level}")
    st.session_state.selected_level = level
    st.rerun()