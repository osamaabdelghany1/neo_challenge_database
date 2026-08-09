import streamlit as st
import sqlite3


username = st.text_input("Username")
password = st.text_input("Password")
email = st.text_input("Email")
dob = st.date_input("Date of Birth")
height = st.number_input("Height")
weight = st.number_input("Weight")
phone = st.text_input("Phone")
ssn = st.text_input("SSN")


if st.button("Register", use_container_width=True):
    conn = sqlite3.connect("database/database.db")
    cursor = conn.cursor()
    cursor.execute("""
    insert into users (username, password, email, DOB, height, weight, phone, ssn)
    values(?, ?, ?, ?, ?, ?, ?, ?)
    """, (username, password, email, dob, height, weight, phone, ssn))
    conn.commit()
    conn.close()
    st.success("User registered successfully")

