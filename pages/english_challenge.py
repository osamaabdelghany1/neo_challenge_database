import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH, CATEGORY_COLORS, CHALLENGE_IMAGES

st.set_page_config(page_title="English Challenges", page_icon="🇺🇸", layout="wide")

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

header("🇺🇸🇬🇧 English Challenges", "Choose your English dialect")
st.divider()

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
cursor.execute("""select id, name, number_of_levels, number_of_activities
    from challenges where category='Language' and (name like '%English%' or name like '%American%' or name like '%British%')
    order by name""")
challenges = cursor.fetchall()
conn.close()

if not challenges:
    st.info("No English challenges yet. Create one from the Challenges page!")
    if st.button("Create English Challenge"):
        st.switch_page("pages/_create_challenges.py")
else:
    cols = st.columns(2)
    for i, ch in enumerate(challenges):
        with cols[i % 2]:
            cc = CATEGORY_COLORS.get("Language", PRIMARY_DARK)
            img = get_challenge_image(ch[1])
            with st.container(border=True):
                st.image(img, use_container_width=True)
                st.markdown(f"<h3 style='color:{cc};margin:0.5rem 0 0.25rem'>{ch[1]}</h3>", unsafe_allow_html=True)
                st.caption(f"{ch[2]} Levels · {ch[3]} Activities")
                if st.button("Start Challenge", key=f"ec_{i}", use_container_width=True):
                    st.session_state.selected_challenge_id = ch[0]
                    st.switch_page("pages/challenge_details.py")