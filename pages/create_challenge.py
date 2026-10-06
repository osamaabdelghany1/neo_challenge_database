import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

st.title("➕ Create challenge")
st.caption("Add a new challenge")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Challenge name")
    category = st.selectbox("Category", ["Sports", "Language", "General Knowledge"])
with col2:
    duration = st.number_input("Duration (days)", min_value=1, max_value=365)
description = st.text_area("Description", height=150)

if st.button("Create challenge", type="primary", width="stretch"):
    conn = sqlite3.connect(DATABASE_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    name_taken = conn.execute("select 1 from challenges where name = ?", (name,)).fetchone()

    if name == "" or description == "":
        st.error("Please fill in every field.")
    elif name_taken:
        st.error("A challenge with that name already exists.")
    else:
        conn.execute(
            "insert into challenges (name, category, duration, description) values (?, ?, ?, ?)",
            (name, category, duration, description),
        )
        conn.commit()
        st.success("Challenge created!")
    conn.close()
