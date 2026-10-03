import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH, LEVEL_ICONS

st.set_page_config(page_title="General Knowledge", page_icon="🧠", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.caption(subtitle)

header("🧠 General Knowledge", "Test your knowledge")

st.divider()

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
gk = cursor.execute("select id from challenges where category='General Knowledge' limit 1").fetchone()
conn.close()

if not gk:
    st.info("General Knowledge challenge not found")
    st.stop()

challenge_id = gk[0]

st.subheader("Choose Level")
lvl_cols = st.columns(3)
for i, level in enumerate(["Easy", "Medium", "Hard"]):
    with lvl_cols[i]:
        icon = LEVEL_ICONS[level]["icon"]
        is_selected = st.session_state.get("quiz_level") == level
        if st.button(f"{icon} {level}", key=f"gk_lvl_{level}", use_container_width=True, type="primary" if is_selected else "secondary"):
            st.session_state.quiz_level = level
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            questions = cursor.execute(
                "select id, question, option_a, option_b, option_c, option_d, correct_answer from questions where challenge_id=? and level=? order by random() limit 10",
                (challenge_id, level),
            ).fetchall()
            conn.close()
            st.session_state.quiz_questions = questions
            if "quiz_submitted" in st.session_state:
                del st.session_state.quiz_submitted
            st.rerun()

level = st.session_state.get("quiz_level")
questions = st.session_state.get("quiz_questions", [])

if level and questions:
    with st.form("quiz"):
        for q in questions:
            options = [f"A. {q[2]}", f"B. {q[3]}", f"C. {q[4]}", f"D. {q[5]}"]
            st.radio(q[1], options, index=None, key=f"q_{q[0]}")
        submitted = st.form_submit_button("Submit Answers", use_container_width=True)

    if submitted:
        st.session_state.quiz_submitted = True

    if st.session_state.get("quiz_submitted"):
        score = 0
        for q in questions:
            qid = q[0]
            correct = q[6]
            key = f"q_{qid}"
            if key in st.session_state:
                selected = st.session_state[key]
                if selected:
                    selected_letter = selected[0]
                    if selected_letter == correct:
                        score += 1
        st.metric("Score", f"{score} / {len(questions)}")
        if score >= 7 and submitted:
            st.balloons()
        for q in questions:
            selected = st.session_state.get(f"q_{q[0]}")
            with st.container(border=True):
                st.write(f"{'✅' if selected and selected[0] == q[6] else '❌'} {q[1]}")
                st.write(f"Your answer: {selected or 'Not answered'}")
                st.write(f"Correct answer: {q[6]}. {q[2 + 'ABCD'.index(q[6])]}")

    if st.button("New Quiz", use_container_width=True):
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        questions = cursor.execute(
            "select id, question, option_a, option_b, option_c, option_d, correct_answer from questions where challenge_id=? and level=? order by random() limit 10",
            (challenge_id, level),
        ).fetchall()
        conn.close()
        st.session_state.quiz_questions = questions
        if "quiz_submitted" in st.session_state:
            del st.session_state.quiz_submitted
        st.rerun()
