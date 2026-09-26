import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH, DIFFICULTY_COLORS, LEVEL_ICONS, CHALLENGE_IMAGES

st.set_page_config(page_title="Challenge Details", page_icon="🏆", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

def get_challenge_image(name):
    for keyword, img in CHALLENGE_IMAGES.items():
        if keyword.lower() in name.lower():
            return img
    return "assets/language_challenge.png"

if "selected_challenge_id" not in st.session_state:
    st.switch_page("pages/view_challenges.py")

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
ch = cursor.execute("""select id, name, number_of_levels, number_of_activities, category, duration, description 
    from challenges where id=?""", (st.session_state.selected_challenge_id,)).fetchone()
conn.close()

if not ch:
    st.error("Challenge not found")
    st.stop()

# ch = (id, name, number_of_levels, number_of_activities, category, duration, description)
challenge_id = ch[0]
name = ch[1]
number_of_levels = ch[2]
number_of_activities = ch[3]
category = ch[4]
duration = ch[5]
description = ch[6]

# Challenge image at top
img = get_challenge_image(name)
st.image(img, use_container_width=True)

header(name)
st.divider()

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Levels", number_of_levels)
with c2:
    st.metric("Activities", number_of_activities)
with c3:
    st.metric("Duration", f"{duration} days")

st.caption(f"Category: {category}")
st.write(description)

c1, c2 = st.columns(2)
with c1:
    if st.button("Start Challenge", use_container_width=True):
        st.success("Challenge started!")
        st.balloons()
with c2:
    if st.button("View All Activities", use_container_width=True):
        st.switch_page("pages/view_activities.py")

st.divider()

# Level selection - visual buttons
st.subheader("Choose Level")
lvl_cols = st.columns(3)
for i, level in enumerate(["Easy", "Medium", "Hard"]):
    with lvl_cols[i]:
        icon = LEVEL_ICONS[level]["icon"]
        color = LEVEL_ICONS[level]["color"]
        is_selected = st.session_state.get("selected_difficulty") == level
        if st.button(f"{icon} {level}", key=f"lvl_{level}", use_container_width=True, type="primary" if is_selected else "secondary"):
            st.session_state.selected_difficulty = level
            st.rerun()

# Filter activities
diff = st.session_state.get("selected_difficulty")
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
if diff:
    cursor.execute("select * from activities where challenge_id=? and difficulty=? order by name", (challenge_id, diff))
else:
    cursor.execute("select * from activities where challenge_id=? order by name", (challenge_id,))
acts = cursor.fetchall()
conn.close()

if diff:
    st.markdown(f"<div style='background:{DIFFICULTY_COLORS.get(diff, PRIMARY_DARK)};color:white;padding:0.5rem;border-radius:8px;margin:0.5rem 0;text-align:center'><strong>Showing {diff} activities</strong></div>", unsafe_allow_html=True)
    if st.button("Clear Filter", use_container_width=True):
        st.session_state.selected_difficulty = None
        st.rerun()

if acts:
    st.subheader("Activities")
    for act in acts:
        with st.container(border=True):
            dc = DIFFICULTY_COLORS.get(act[4], PRIMARY_DARK)
            st.markdown(f"<div style='display:flex;justify-content:space-between'><strong>{act[1]}</strong><span style='background:{dc};color:white;padding:0.2rem 0.5rem;border-radius:9999px;font-size:0.7rem'>{act[4]}</span></div>", unsafe_allow_html=True)
            st.caption(act[2])
            if st.button("Start Activity", key=f"act_{act[0]}", use_container_width=True):
                st.session_state.selected_activities_id = act[0]
                st.switch_page("pages/_activites_details.py")
else:
    st.info(f"No {diff} activities found" if diff else "No activities found")