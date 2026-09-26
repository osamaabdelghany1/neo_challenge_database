import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DIFFICULTY_COLORS, CATEGORY_COLORS, DATABASE_PATH

st.set_page_config(page_title="View Activities", page_icon="🏃", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

header("🏃 View Activities", "Browse all workout activities and exercises")
st.divider()

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
cursor.execute("select id, name, description, category, difficulty from activities order by name")
activities = cursor.fetchall()
conn.close()

if not activities:
    st.info("No activities found")
else:
    cols = st.columns(3)
    for i, act in enumerate(activities):
        with cols[i % 3]:
            dc = DIFFICULTY_COLORS.get(act[4], "#77ABB7")
            cc = CATEGORY_COLORS.get(act[3], PRIMARY_DARK)
            with st.container(border=True):
                st.markdown(f"<h3 style='color:{PRIMARY_DARK};margin:0'>{act[1]}</h3>", unsafe_allow_html=True)
                st.caption(f"{act[3]} · {act[4]}")
                st.write(act[2])
                if st.button("View Details", key=f"va_{i}", use_container_width=True):
                    st.session_state.selected_activities_id = act[0]
                    st.switch_page("pages/_activites_details.py")