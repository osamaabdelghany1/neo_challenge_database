import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="Create Muscle", page_icon="➕", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

header("➕ Create Muscle", "Add a new muscle group")
st.divider()

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
    difficulty = st.selectbox("Difficulty to Train", ["Easy", "Medium", "Hard"])
    image_url = st.text_input("Image URL")
    video_url = st.text_input("Video URL")
    submitted = st.form_submit_button("Create Muscle", use_container_width=True)

if submitted:
    if not name or not description or not muscle_group or not location or not function:
        st.error("Please fill in all required fields (*)")
    else:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("""insert into muscles (name, latin_name, description, muscle_group, location, function, origin, insertion, muscle_type, difficulty_to_train, image_url, video_url)
                       values (?,?,?,?,?,?,?,?,?,?,?,?)""",
                       (name, latin_name, description, muscle_group, location, function, origin, insertion, muscle_type, difficulty, image_url, video_url))
        conn.commit()
        conn.close()
        st.success("Muscle created!")