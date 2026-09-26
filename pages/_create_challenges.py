import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DIFFICULTY_COLORS, CATEGORY_COLORS, DATABASE_PATH

st.set_page_config(page_title="Create Challenge", page_icon="➕", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

header("➕ Create Challenge", "Design a new fitness challenge")
st.divider()

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Challenge Name")
    category = st.selectbox("Category", ["Sports", "Language", "General Knowledge"])
    duration = st.number_input("Duration (days)", min_value=1, max_value=365)
with col2:
    levels = st.number_input("Number of Levels", min_value=1, max_value=10)
    activities = st.number_input("Number of Activities", min_value=1, max_value=100)

description = st.text_area("Description", height=150)
st.divider()

if st.button("Create Challenge", use_container_width=True):
    if not name or not levels or not activities or not category or not duration or not description:
        st.error("Please enter all fields")
    else:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("insert into challenges (name, number_of_levels, number_of_activities, category, duration, description) values (?,?,?,?,?,?)",
                       (name, levels, activities, category, duration, description))
        conn.commit()
        conn.close()
        st.success("Challenge created!")
        st.balloons()