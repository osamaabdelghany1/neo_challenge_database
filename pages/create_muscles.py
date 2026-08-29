import streamlit as st
import sqlite3

st.set_page_config(page_title="Create Muscle", page_icon="💪", layout="wide")

st.title("Create Muscles")

with st.form("muscle_form"):
    name = st.text_input("Name *")
    latin_name = st.text_input("Latin Name")
    description = st.text_area("Description *")
    muscle_group = st.selectbox("Muscle Group *", ["Upper Body", "Core", "Lower Body"])
    location = st.text_input("Location *")
    function = st.text_area("Function *")
    origin = st.text_input("Origin")
    insertion = st.text_input("Insertion")
    muscle_type = st.selectbox("Muscle Type", ["Skeletal", "Smooth", "Cardiac"])
    difficulty_to_train = st.selectbox("Difficulty to Train", ["Easy", "Medium", "Hard"])
    image_url = st.text_input("Image URL")
    video_url = st.text_input("Video URL")
    
    submitted = st.form_submit_button("Create Muscle", use_container_width=True)

if submitted:
    if not name or not description or not muscle_group or not location or not function:
        st.error("Please fill in all required fields (*)")
    else:
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        cursor.execute("""
        insert into muscles (name, latin_name, description, muscle_group, location, function, origin, insertion, muscle_type, difficulty_to_train, image_url, video_url)
        values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, latin_name, description, muscle_group, location, function, origin, insertion, muscle_type, difficulty_to_train, image_url, video_url))
        conn.commit()
        conn.close()
        st.success("Muscle created successfully!")