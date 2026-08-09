import streamlit as st
import sqlite3



st.title("View Activities")

conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

cursor.execute("""
select name, description, category, difficulty from activities order by name
""")

activities = cursor.fetchall()

conn.close()



cols = st.columns(3)
for i, activity in enumerate(activities):

    with cols[i % 3]:
    
        with st.container():
            st.header(activity[0])
            st.text("name")
            st.text(f"Description: {activity[1]}")
            st.text(f"Category: {activity[2]}")
            st.text(f"Difficulty: {activity[3]}")
            
            st.button("view details", use_container_width=True, key=f"view_details_{activity[0]}")




