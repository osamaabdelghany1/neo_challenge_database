import streamlit as st
import sqlite3



if "selected_challenge_id" not in st.session_state:
    st.switch_page("pages/view_challenges.py")




conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()
challenge = cursor.execute("SELECT * FROM challenges WHERE id = ?", (st.session_state.selected_challenge_id,)).fetchone()

challenge_data = challenge
st.title(f"Details for {challenge_data[1]}")

with st.container():
    st.subheader("Challenge Information")
    st.text(f"Number of levels: {challenge_data[2]}")
    st.text(f"Number of activities: {challenge_data[3]}")
    st.text(f"Category: {challenge_data[4]}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start Challenge"):
            st.success("Challenge started!")
            st.balloons()
    with col2:
        if st.button("📝 Take Quiz"):
            st.switch_page("pages/quiz.py")