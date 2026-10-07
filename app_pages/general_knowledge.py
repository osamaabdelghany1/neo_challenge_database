import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

# How many questions one quiz round has.
QUESTIONS_PER_QUIZ = 10
# Score this many or more and you get balloons.
GREAT_SCORE = 7
LETTERS = ["A", "B", "C", "D"]


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
    st.session_state.quiz_level = level
    st.session_state.quiz_questions = questions
    st.session_state.quiz_number = 0      # which question you are on (0 is the first)
    st.session_state.quiz_answers = []    # the letter you picked for each question
    st.session_state.quiz_just_finished = False


st.title("🧠 General knowledge quiz")
st.caption("One question at a time. Pick an answer and see if you are right.")

level = st.pills("Level", ["Easy", "Medium", "Hard"], default="Easy", required=True)

# A new level, or the very first visit, starts a fresh quiz.
if st.session_state.get("quiz_level") != level:
    load_new_quiz(level)

questions = st.session_state.quiz_questions
number = st.session_state.quiz_number
answers = st.session_state.quiz_answers

if len(questions) == 0:
    st.info("There are no questions for this level yet.")
    st.stop()

if number < len(questions):
    # Still answering: show one question.
    question = questions[number]
    answered = len(answers) > number
    st.progress(number / len(questions), text=f"Question {number + 1} of {len(questions)}")

    with st.container(border=True):
        st.subheader(question["question"])
        cols = st.columns(2)
        place = 0
        for letter in LETTERS:
            option = question["option_" + letter.lower()]
            with cols[place % 2]:
                # The buttons lock after you answer, so you can't change your mind.
                if st.button(letter + ". " + option, key=f"pick_{question['id']}_{letter}",
                             disabled=answered, type="primary", width="stretch"):
                    # "answers" is the list kept in session_state, so this remembers your pick.
                    answers.append(letter)
                    st.rerun()
            place = place + 1

    if answered:
        correct_letter = question["correct_answer"]
        correct_text = question["option_" + correct_letter.lower()]
        if answers[number] == correct_letter:
            st.success("✅ Right! " + correct_letter + ". " + correct_text + " is correct.")
        else:
            st.error("❌ Not quite. The answer is " + correct_letter + ". " + correct_text + ".")

        if number + 1 < len(questions):
            next_label = "Next question →"
        else:
            next_label = "See my score →"
        if st.button(next_label, type="primary", width="stretch"):
            st.session_state.quiz_number = number + 1
            if number + 1 == len(questions):
                st.session_state.quiz_just_finished = True
            st.rerun()
else:
    # All questions answered: show the score and what you got right.
    score = 0
    for place in range(len(questions)):
        if answers[place] == questions[place]["correct_answer"]:
            score = score + 1

    st.metric("Your score", f"{score} / {len(questions)}")
    # Right after the last question: save the round (if logged in) and maybe show balloons.
    # This runs only once per round, so a round is never saved twice.
    if st.session_state.quiz_just_finished:
        if "user_id" in st.session_state:
            conn = sqlite3.connect(DATABASE_PATH)
            conn.execute("PRAGMA foreign_keys = ON")
            conn.execute(
                "insert into quiz_results (user_id, level, score, total) values (?, ?, ?, ?)",
                (st.session_state.user_id, level, score, len(questions)),
            )
            conn.commit()
            conn.close()
        if score >= GREAT_SCORE:
            st.balloons()
        st.session_state.quiz_just_finished = False

    if "user_id" in st.session_state:
        st.caption("Your score is saved. See it in My challenges.")
    else:
        st.info("Log in to save your scores.")

    for place in range(len(questions)):
        question = questions[place]
        correct_letter = question["correct_answer"]
        picked_letter = answers[place]
        with st.container(border=True):
            if picked_letter == correct_letter:
                st.write("✅ " + question["question"])
            else:
                st.write("❌ " + question["question"])
            st.write("Your answer: " + picked_letter + ". " + question["option_" + picked_letter.lower()])
            st.write("Correct answer: " + correct_letter + ". " + question["option_" + correct_letter.lower()])

    if st.button("Play again", type="primary", width="stretch"):
        load_new_quiz(level)
        st.rerun()
