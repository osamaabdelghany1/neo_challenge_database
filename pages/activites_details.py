import streamlit as st
import sqlite3


if "selected_activities_id" not in st.session_state:
    st.switch_page("pages/view_activities.py")


conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()
activity = cursor.execute("SELECT * FROM activities WHERE id = ?", (st.session_state.selected_activities_id,)).fetchone()

activity_data = activity
st.title(f"Details for {activity_data[1]}")

with st.container():
    st.subheader("Activity Information")
    st.text(f"description: {activity_data[2]}")
    st.text(f"category: {activity_data[3]}")
    st.text(f"difficulty: {activity_data[4]}")



    if st.button("Start Activity"):
        st.success("Activity started!")
        st.balloons()


