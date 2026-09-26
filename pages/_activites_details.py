import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="Activity Details", page_icon="🏃", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

if "selected_activities_id" not in st.session_state:
    st.switch_page("pages/view_activities.py")

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
act = cursor.execute("select * from activities where id=?", (st.session_state.selected_activities_id,)).fetchone()
conn.close()

if not act:
    st.error("Activity not found")
    st.stop()

header(f"Details for {act[1]}")
st.divider()

st.write(f"**Description:** {act[2]}")
st.write(f"**Category:** {act[3]}")
st.write(f"**Difficulty:** {act[4]}")

st.divider()
if st.button("Start Activity", use_container_width=True):
    st.success("Activity started!")
    st.balloons()