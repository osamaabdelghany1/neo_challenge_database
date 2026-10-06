import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

st.title("👥 Users")
st.caption("Everyone who signed up")

conn = sqlite3.connect(DATABASE_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
users = conn.execute("select * from users order by created_at desc").fetchall()
conn.close()

cols = st.columns(3)
number = 0
for user in users:
    with cols[number % 3]:
        with st.container(border=True):
            if user["is_admin"] == 1:
                st.subheader(user["username"] + " (admin)")
            else:
                st.subheader(user["username"])
            st.caption(user["email"])
            st.write(f"📅 Born: {user['birth_date']}")
            st.write(f"📏 Height: {user['height']} cm")
            st.write(f"⚖️ Weight: {user['weight']} kg")
            st.write(f"📱 Phone: {user['phone']}")
    number = number + 1
