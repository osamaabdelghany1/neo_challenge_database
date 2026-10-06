import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

st.title("🔐 Log in")
st.caption("Welcome back")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary", width="stretch"):
    if email == "" or password == "":
        st.error("Please enter your email and password.")
    else:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        user = conn.execute(
            "select * from users where email = ? and password = ?",
            (email, password),
        ).fetchone()
        conn.close()

        if user is None:
            st.error("Wrong email or password.")
        else:
            # Remember who you are, then reload so the menu shows your pages.
            st.session_state.user_id = user["id"]
            st.session_state.username = user["username"]
            st.session_state.is_admin = user["is_admin"] == 1
            st.rerun()
