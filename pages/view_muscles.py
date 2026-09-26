import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="View Muscles", page_icon="💪", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

header("💪 View Muscles", "Browse all muscle groups")
st.divider()

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
cursor.execute("select id, name, muscle_group, image_url from muscles order by name")
muscles = cursor.fetchall()
conn.close()

if not muscles:
    st.info("No muscles found")
else:
    cols = st.columns(3)
    for i, m in enumerate(muscles):
        with cols[i % 3]:
            with st.container(border=True):
                if m[3]:
                    st.image(m[3], use_container_width=True)
                st.markdown(f"<h3 style='color:{PRIMARY_DARK};margin:0.5rem 0 0.25rem'>{m[1]}</h3>", unsafe_allow_html=True)
                st.caption(f"Group: {m[2]}")
                if st.button("View Details", key=f"vm_{i}", use_container_width=True):
                    st.session_state.selected_muscle_id = m[0]
                    st.switch_page("pages/_muscle_details.py")