import streamlit as st
import sqlite3

st.set_page_config(page_title="View Users", page_icon="📊", layout="wide")

st.title("View Users")

conn = sqlite3.connect("database/database.db")

cursor = conn.cursor()


cursor.execute("""
select 
    username, 
    email, 
    DOB, 
    height, 
    weight, 
    phone, 
    ssn 
from users 
order by created_at 
desc
""")

users = cursor.fetchall()

conn.close()


cols = st.columns(3)
for i, user in enumerate(users):

    with cols[i % 3]:
    
        with st.container():
            st.header(user[0])
    
            st.text(f"Email: {user[1]}")
            st.text(f"DOB: {user[2]}")
            st.text(f"Height: {user[3]}")
            
            st.text(f"Weight: {user[4]}")
            st.text(f"Phone: {user[5]}")
            st.text(f"SSN: {user[6]}")

            st.button("view details", use_container_width=True, key=f"view_details_{user[0]}")


