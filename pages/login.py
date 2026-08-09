import streamlit as st
import sqlite3


email = st.text_input("Email")
password = st.text_input("Password")

if st.button("Login", use_container_width=True):
    conn = sqlite3.connect("database/database.db")
    cursor = conn.cursor()
    cursor.execute("""
    select * from users where email = ? and password = ?
    """, (email, password))
    user = cursor.fetchone()
    st.session_state.userId = user[0]
    conn.close()
    if user:
        st.success("User logged in successfully")
    else:
        st.error("Invalid email or password")
