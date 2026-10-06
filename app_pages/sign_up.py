import datetime
import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

# The oldest birthday the form lets you pick.
OLDEST_BIRTH_DATE = datetime.date(1940, 1, 1)

st.title("📝 Sign up")
st.caption("Create your NEO Challenge account")

col1, col2 = st.columns(2)
with col1:
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    phone = st.text_input("Phone")
with col2:
    birth_date = st.date_input("Date of birth", value=None, min_value=OLDEST_BIRTH_DATE, max_value=datetime.date.today())
    height = st.number_input("Height (cm)", min_value=0, max_value=300)
    weight = st.number_input("Weight (kg)", min_value=0, max_value=500)

if st.button("Sign up", type="primary", width="stretch"):
    conn = sqlite3.connect(DATABASE_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    email_taken = conn.execute("select 1 from users where email = ?", (email,)).fetchone()
    user_count = conn.execute("select count(*) from users").fetchone()[0]

    if username == "" or email == "" or password == "" or phone == "" or birth_date is None or height == 0 or weight == 0:
        st.error("Please fill in every field.")
    elif email_taken:
        st.error("That email is already used. Try logging in instead.")
    else:
        # The very first person who signs up becomes the admin.
        if user_count == 0:
            is_admin = 1
        else:
            is_admin = 0
        conn.execute(
            "insert into users (username, email, password, phone, birth_date, height, weight, is_admin) values (?, ?, ?, ?, ?, ?, ?, ?)",
            (username, email, password, phone, birth_date.isoformat(), height, weight, is_admin),
        )
        conn.commit()
        if is_admin == 1:
            st.success("Account created! You are the first user, so you are the admin. You can log in now.")
        else:
            st.success("Account created! You can log in now.")
        st.balloons()
    conn.close()
