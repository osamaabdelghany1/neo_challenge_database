import streamlit as st
import sqlite3


name = st.text_input("Name")
number_of_levels = st.number_input("Number of levels")
number_of_activities = st.number_input("Number of activities")
category = st.text_input("Category")
duration = st.number_input("Duration")
description = st.text_area("Description")

if st.button("Create Challenge", use_container_width=True):
    if not name or not number_of_levels or not number_of_activities or not category or not duration or not description:
        st.error("Please enter a valid info")
    else:
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        cursor.execute("""
        insert into challenges (name, number_of_levels, number_of_activities, category, duration, description)
        values(?, ?, ?, ?, ?, ?)
        """, (name, number_of_levels, number_of_activities, category, duration, description))
        conn.commit()
        conn.close()
        st.success("Challenge created successfully")