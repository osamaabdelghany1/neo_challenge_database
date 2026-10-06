import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

st.title("➕ Create muscle")
st.caption("Fields with * are required")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Name *")
    latin_name = st.text_input("Latin name")
    muscle_group = st.selectbox("Muscle group *", ["Upper Body", "Core", "Lower Body"])
    location = st.text_input("Location *")
    origin = st.text_input("Origin")
    insertion = st.text_input("Insertion")
with col2:
    muscle_type = st.selectbox("Muscle type", ["Skeletal", "Smooth", "Cardiac"])
    difficulty = st.selectbox("Difficulty to train", ["Easy", "Medium", "Hard"])
    image_url = st.text_input("Image file", placeholder="assets/chest.jpg")
    video_url = st.text_input("Video file")
description = st.text_area("Description *")
function = st.text_area("What it does *")

if st.button("Create muscle", type="primary", width="stretch"):
    conn = sqlite3.connect(DATABASE_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    name_taken = conn.execute("select 1 from muscles where name = ?", (name,)).fetchone()

    if name == "" or location == "" or description == "" or function == "":
        st.error("Please fill in every field marked with *.")
    elif name_taken:
        st.error("A muscle with that name already exists.")
    else:
        conn.execute(
            """insert into muscles (name, latin_name, description, muscle_group, location, function,
                                    origin, insertion, muscle_type, difficulty_to_train, image_url, video_url)
               values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (name, latin_name, description, muscle_group, location, function,
             origin, insertion, muscle_type, difficulty, image_url, video_url),
        )
        conn.commit()
        st.success("Muscle created!")
    conn.close()
