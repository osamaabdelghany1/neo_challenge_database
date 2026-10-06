import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

st.title("➕ Create activity")
st.caption("Add an activity to a challenge")

conn = sqlite3.connect(DATABASE_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
challenges = conn.execute("select id, name from challenges order by name").fetchall()
conn.close()

# The dropdown shows challenge names; this remembers which id belongs to each name.
challenge_ids = {}
for challenge in challenges:
    challenge_ids[challenge["name"]] = challenge["id"]

col1, col2 = st.columns(2)
with col1:
    challenge_name = st.selectbox("Challenge", list(challenge_ids.keys()))
    name = st.text_input("Activity name")
with col2:
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
description = st.text_area("Description", height=150)

if st.button("Create activity", type="primary", width="stretch"):
    if challenge_name is None or name == "" or description == "":
        st.error("Please fill in every field.")
    else:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute(
            "insert into activities (challenge_id, name, description, difficulty) values (?, ?, ?, ?)",
            (challenge_ids[challenge_name], name, description, difficulty),
        )
        conn.commit()
        conn.close()
        st.success("Activity created!")
