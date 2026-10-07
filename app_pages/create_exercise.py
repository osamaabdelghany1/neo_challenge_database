import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

st.title("➕ Create exercise")
st.caption("Add an exercise for a muscle")

conn = sqlite3.connect(DATABASE_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
muscles = conn.execute("select id, name from muscles order by name").fetchall()
conn.close()

# The dropdown shows muscle names; this remembers which id belongs to each name.
muscle_ids = {}
for muscle in muscles:
    muscle_ids[muscle["name"]] = muscle["id"]

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Exercise name")
    muscle_name = st.selectbox("Muscle", list(muscle_ids.keys()))
    equipment = st.selectbox("Equipment", ["Machine", "Free Weights", "Bodyweight", "Cable"])
with col2:
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    video_url = st.text_input("Video file", placeholder="videos/pushups.mp4")
    thumbnail_url = st.text_input("Thumbnail file", placeholder="assets/thumbnails/pushups.jpg")
description = st.text_area("Description", height=150)

if st.button("Create exercise", type="primary", width="stretch"):
    if name == "" or muscle_name is None:
        st.error("Please enter a name and pick a muscle.")
    else:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute(
            "insert into exercises (muscle_id, name, description, equipment, difficulty, video_url, thumbnail_url) values (?, ?, ?, ?, ?, ?, ?)",
            (muscle_ids[muscle_name], name, description, equipment, difficulty, video_url, thumbnail_url),
        )
        conn.commit()
        conn.close()
        st.success("Exercise created!")
