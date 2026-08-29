import streamlit as st
import sqlite3




st.set_page_config(page_title="View Challenges", page_icon="📊", layout="wide")

st.title("View Challenges")

conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

cursor.execute("""
select id, name, number_of_levels, number_of_activities, category from challenges order by name
""")

challenges = cursor.fetchall()
columns = [description[0] for description in cursor.description]

conn.close()



cols = st.columns(3)
for i, challenge in enumerate(challenges):

    with cols[i % 3]:
    
        with st.container():
            st.header(challenge[1])
            st.text("name")
            st.text(f"Number of levels: {challenge[2]}")
            st.text(f"Number of activities: {challenge[3]}")
            st.text(f"Category: {challenge[4]}")
            
            if st.button("view details", use_container_width=True, key=f"view_details_{i}"):
                st.session_state.selected_challenge_id = challenge[0]
                st.switch_page("pages/challenge_details.py")






