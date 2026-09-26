import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="View Nutrition Plans", page_icon="🥗", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

header("🥗 View Nutrition Plans", "Browse nutrition plans for different fitness goals")
st.divider()

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
cursor.execute("select id, bmi, category, goal, calories, breakfast, lunch, dinner, water_intake from Nutrition_Plans order by created_at")
plans = cursor.fetchall()
conn.close()

if not plans:
    st.info("No nutrition plans found")
else:
    cols = st.columns(3)
    for i, p in enumerate(plans):
        with cols[i % 3]:
            gc = "#77ABB7" if p[3] == "Lose Weight" else "#476D7C" if p[3] == "Gain Weight" else PRIMARY_DARK
            with st.container(border=True):
                st.markdown(f"<h3 style='color:{PRIMARY_DARK};margin:0'>BMI: {p[1]}</h3>", unsafe_allow_html=True)
                st.caption(f"Goal: {p[3]} · Category: {p[2]}")
                st.metric("Calories", f"{p[4]} kcal")
                st.metric("Water", p[8])
                with st.expander("Meals"):
                    st.write(f"**Breakfast:** {p[5]}")
                    st.write(f"**Lunch:** {p[6]}")
                    st.write(f"**Dinner:** {p[7]}")
                if st.button("View Details", key=f"vnp_{i}", use_container_width=True):
                    st.session_state.selected_nutrition_plans_id = p[0]
                    st.switch_page("pages/_nutrition_plan_details.py")