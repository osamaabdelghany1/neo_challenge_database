import streamlit as st
import sqlite3







st.set_page_config(page_title="View muscles", page_icon="📊", layout="wide")

st.title("View muscles")

conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

cursor.execute(""" 
select name, latin_name, description, muscle_group, location, function, origin, insertion, muscle_type, difficulty_to_train, image_url, video_url
from muscles
order by name

""")

muscles = cursor.fetchall()
columns = [description[0] for description in cursor.description]

conn.close()



cols = st.columns(3)
for i,  muscle in enumerate(muscles):

    with cols[i % 3]:
    
        with st.container():
            st.header(muscle[0])            
            st.text("name")
            st.text(f"Number of levels: {muscle[1]}")
            st.text(f"Number of activities: {muscle[2]}")
            st.text(f"Category: {muscle[3]}")
            
            st.button("view details", use_container_width=True, key=f"view_details_{i}")






