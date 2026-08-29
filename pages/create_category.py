from turtle import color
import streamlit as st
import sqlite3

st.title("Add Category")

name = st.text_input("Name")
description = st.text_area("Description")
category = st.text_input("Category")
difficulty = st.text_input("Difficulty")
challenge_id = st.number_input("Challenge ID")



if st.button("Create Category", use_container_width=True):


    if not name or not description or not category or not difficulty or not challenge_id:

        st.error("Please enter a valid info")


    else:

        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
       
        cursor.execute("""
        insert into categories (name, description, category, difficulty, challenge_id)
        values(?, ?, ?, ?, ?)
        """, (name, description, category, difficulty, challenge_id))
       
        conn.commit()
        conn.close()
       
        st.success("Category created successfully")
