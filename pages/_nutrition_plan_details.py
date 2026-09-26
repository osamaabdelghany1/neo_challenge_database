import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="Nutrition Plan Details", page_icon="🥗", layout="wide")

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def header(title, subtitle=""):
    st.markdown(f"<h1 style='color:{PRIMARY_DARK}'>{title}</h1>", unsafe_allow_html=True)
    if subtitle: st.caption(subtitle)

if "selected_nutrition_plans_id" not in st.session_state:
    st.switch_page("pages/view_nutrition_plan.py")

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
plan = cursor.execute("select * from Nutrition_Plans where id=?", (st.session_state.selected_nutrition_plans_id,)).fetchone()
conn.close()

if not plan:
    st.error("Plan not found")
    st.stop()

header(f"Nutrition Plan Details")
st.divider()

st.write(f"**BMI:** {plan[1]}")
st.write(f"**Category:** {plan[2]}")
st.write(f"**Goal:** {plan[3]}")
st.write(f"**Calories:** {plan[4]} kcal")
st.write(f"**Breakfast:** {plan[5]}")
st.write(f"**Lunch:** {plan[6]}")
st.write(f"**Dinner:** {plan[7]}")
st.write(f"**Water Intake:** {plan[8]}")

st.divider()
if st.button("Follow Plan", use_container_width=True):
    st.success("Plan activated!")
    st.balloons()