import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

# How many questions one quiz round has.
QUESTIONS_PER_QUIZ = 10
# Score this many or more and you get balloons.
GREAT_SCORE = 7


def load_new_quiz(level):
    # Pick random questions for this level and remember them,
    # so they stay the same while you answer.
    conn = sqlite3.connect(DATABASE_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    questions = conn.execute("""
        select questions.*
        from questions
        join challenges on challenges.id = questions.challenge_id
        where challenges.category = 'General Knowledge' and questions.level = ?
        order by random()
        limit ?
    """, (level, QUESTIONS_PER_QUIZ)).fetchall()
    conn.close()
    # Forget the answers from the last round.
    for key in list(st.session_state.keys()):
        if key.startswith("answer_"):
            del st.session_state[key]
    st.session_state.quiz_level = level
    st.session_state.quiz_questions = questions
    st.session_state.quiz_submitted = False


st.title("🧠 General knowledge quiz")
st.caption("Answer the questions, then see your score")

level = st.radio("Choose a level", ["Easy", "Medium", "Hard"], horizontal=True)

# A new level, or the very first visit, gets a fresh set of questions.
if st.session_state.get("quiz_level") != level:
    load_new_quiz(level)

questions = st.session_state.quiz_questions

if len(questions) == 0:
    st.info("There are no questions for this level yet.")
    st.stop()

with st.form("quiz"):
    for question in questions:
        options = [
            "A. " + question["option_a"],
            "B. " + question["option_b"],
            "C. " + question["option_c"],
            "D. " + question["option_d"],
        ]
        st.radio(question["question"], options, index=None, key=f"answer_{question['id']}")
    submitted = st.form_submit_button("Submit answers", type="primary", width="stretch")

if submitted:
    st.session_state.quiz_submitted = True

if st.session_state.quiz_submitted:
    score = 0
    for question in questions:
        answer = st.session_state.get(f"answer_{question['id']}")
        # An answer looks like "B. Paris", so its first letter is the choice.
        if answer is not None and answer[0] == question["correct_answer"]:
            score = score + 1

    st.metric("Score", f"{score} / {len(questions)}")
    if submitted and score >= GREAT_SCORE:
        st.balloons()

    for question in questions:
        answer = st.session_state.get(f"answer_{question['id']}")
        correct_letter = question["correct_answer"]
        correct_text = question["option_" + correct_letter.lower()]
        with st.container(border=True):
            if answer is not None and answer[0] == correct_letter:
                st.write("✅ " + question["question"])
            else:
                st.write("❌ " + question["question"])
            if answer is None:
                st.write("Your answer: not answered")
            else:
                st.write("Your answer: " + answer)
            st.write("Correct answer: " + correct_letter + ". " + correct_text)

if st.button("New quiz", width="stretch"):
    load_new_quiz(level)
    st.rerun()
