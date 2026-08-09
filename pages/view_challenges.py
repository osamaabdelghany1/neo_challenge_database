import streamlit as st
import sqlite3




st.set_page_config(page_title="View Challenges", page_icon="📊", layout="wide")

st.title("View Challenges")

conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

cursor.execute("""
select name, number_of_levels, number_of_activities, category from challenges order by name
""")

challenges = cursor.fetchall()
columns = [description[0] for description in cursor.description]

conn.close()



cols = st.columns(3)
for i, challenge in enumerate(challenges):

    with cols[i % 3]:
    
        with st.container():
            st.header(challenge[0])
            st.text("name")
            st.text(f"Number of levels: {challenge[1]}")
            st.text(f"Number of activities: {challenge[2]}")
            st.text(f"Category: {challenge[3]}")
            
            st.button("view details", use_container_width=True, key=f"view_details_{challenge[0]}")






