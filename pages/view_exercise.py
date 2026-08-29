import streamlit as st
import sqlite3







st.set_page_config(page_title="View exercise", page_icon="📊", layout="wide")

st.title("View exercise")

conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

cursor.execute("""
select    name, description, equipment_needed, difficulty, video_url from exercises order by name

""")

exercises = cursor.fetchall()
columns = [description[0] for description in cursor.description]

conn.close()



cols = st.columns(3)
for i,  exercise in enumerate(exercises):

    with cols[i % 3]:
    
        with st.container():
            st.header(exercise[0])            
            st.text("name")
            st.text(f"Number of levels: {exercise[1]}")
            st.text(f"Number of activities: {exercise[2]}")
            st.text(f"Category: {exercise[3]}")
            
            st.button("view details", use_container_width=True, key=f"view_details_{i}")






