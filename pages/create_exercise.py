import streamlit as st
import sqlite3

st.title("Create Exercises")



nmuscle_id = st.text_input("Muscle ID")
name = st.text_input("Name")
description = st.text_area("Description")
equipment_needed = st.text_input("Equipment Needed")
difficulty = st.text_input("Difficulty")
video_url = st.text_input("Video URL")




if st.button("Create Exercise", use_container_width=True):
    if not nmuscle_id or not name or not description:
        st.error("Please enter a valid info")
    else:
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        cursor.execute("""
        insert into exercises  (muscle_id, name, description, equipment_needed, difficulty, video_url)
)
        values(?, ?, ?, ?, ?, ?)
        """, (muscle_id, name, description, equipment_needed, difficulty, video_url))
        conn.commit()
        conn.close()
        st.success("Exercise created successfully")