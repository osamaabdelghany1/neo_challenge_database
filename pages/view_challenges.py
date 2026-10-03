import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DIFFICULTY_COLORS, CATEGORY_COLORS, DATABASE_PATH

st.set_page_config(page_title="View Challenges", page_icon="🏆", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

header("🏆 View Challenges", "Browse all available fitness challenges")
st.divider()

if st.session_state.get("fitness_level_filter"):
    diff = st.session_state.fitness_level_filter
    dc = DIFFICULTY_COLORS.get(diff, PRIMARY_DARK)
    st.markdown(f"<div style='background:{dc};color:white;padding:1rem;border-radius:8px;margin-bottom:1rem'><strong>Filtered by:</strong> {diff} difficulty activities</div>", unsafe_allow_html=True)
    if st.button("Clear Filter", use_container_width=True):
        st.session_state.fitness_level_filter = None
        st.rerun()

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
ff = st.session_state.get("fitness_level_filter")
if ff:
    cursor.execute("""select distinct c.id, c.name, c.number_of_levels, c.number_of_activities, c.category
        from challenges c join activities a on c.id=a.challenge_id
        where a.difficulty=? order by c.name""", (ff,))
else:
    cursor.execute("select id, name, number_of_levels, number_of_activities, category from challenges order by name")
challenges = cursor.fetchall()
conn.close()

if not challenges:
    st.info("No challenges found" + (f" with {ff} difficulty activities" if ff else ""))
else:
    cols = st.columns(3)
    for i, ch in enumerate(challenges):
        with cols[i % 3]:
            cc = CATEGORY_COLORS.get(ch[4], PRIMARY_DARK)
            with st.container(border=True):
                st.markdown(f"<h3 style='color:{cc};margin:0'>{ch[1]}</h3>", unsafe_allow_html=True)
                st.caption(f"{ch[2]} Levels · {ch[3]} Activities · {ch[4]}")
                if st.button("View Details", key=f"vd_{i}", use_container_width=True):
                    st.session_state.selected_challenge_id = ch[0]
                    st.switch_page("pages/challenge_details.py")