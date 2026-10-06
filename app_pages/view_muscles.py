import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

st.title("🦵 Muscles")
st.caption("Get to know the muscles you train")

conn = sqlite3.connect(DATABASE_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
muscles = conn.execute("select * from muscles order by name").fetchall()
conn.close()

if len(muscles) == 0:
    st.info("No muscles yet.")

cols = st.columns(3)
number = 0
for muscle in muscles:
    with cols[number % 3]:
        with st.container(border=True):
            if muscle["image_url"]:
                st.image(muscle["image_url"], width="stretch")
            st.subheader(muscle["name"])
            st.caption(muscle["muscle_group"])
            with st.expander("Anatomy facts"):
                st.write(muscle["description"])
                st.write(f"**Latin name:** {muscle['latin_name'] or 'unknown'}")
                st.write(f"**Location:** {muscle['location']}")
                st.write(f"**What it does:** {muscle['function']}")
                st.write(f"**Starts at:** {muscle['origin'] or 'unknown'}")
                st.write(f"**Ends at:** {muscle['insertion'] or 'unknown'}")
                st.write(f"**Type:** {muscle['muscle_type'] or 'unknown'}")
                st.write(f"**Difficulty to train:** {muscle['difficulty_to_train'] or 'unknown'}")
            if st.button("Find a workout", key=f"workout_{muscle['id']}", width="stretch"):
                st.switch_page("app_pages/workout.py")
    number = number + 1
