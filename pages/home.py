import streamlit as st
import sqlite3
import os
from assets.config import PRIMARY_DARK, DATABASE_PATH

st.set_page_config(page_title="Daily Challenges", page_icon="✨", layout="wide")

st.title("Daily Challenge")
st.caption("Transform your daily routine with fun and engaging challenges")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("🏋️ Sports")
    st.image("assets/sport_challenge.png", use_container_width=True, caption="Stay fit and active")
    st.write("Daily physical activities to boost your energy and improve your fitness level.")
with col2:
    st.subheader("🗣️ Language Challenge")
    st.image("assets/language_challenge.png", use_container_width=True, caption="Expand your vocabulary")
    st.write("Daily words and phrases to help you master English and communicate effectively.")
with col3:
    st.subheader("🧠 General Knowledge")
    st.image("assets/General-Knowledge.jpg", use_container_width=True, caption="Expand your knowledge")
    st.write("Daily facts and trivia to boost your general knowledge.")

st.divider()

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("Start Sports Challenge", use_container_width=True):
        st.switch_page("pages/view_challenges.py")
with c2:
    if st.button("Start Language Challenge", use_container_width=True):
        st.switch_page("pages/language_challenge.py")
with c3:
    if st.button("Start General Knowledge Challenge", use_container_width=True):
        st.switch_page("pages/view_challenges.py")

st.subheader("More Ways to Train")
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🏋️ Workout by Equipment", use_container_width=True):
        st.switch_page("pages/workout.py")
with c2:
    if st.button("📊 Fitness Level Test", use_container_width=True):
        st.switch_page("pages/sport-challenge.py")
with c3:
    if st.button("💪 View All Exercises", use_container_width=True):
        st.switch_page("pages/view_exercise.py")

st.markdown("""
## How It Works
1. **Choose your level** - Beginner, Intermediate, or Advanced
2. **Get daily challenges** - Three new challenges every day
3. **Track your progress** - Watch yourself improve over time
4. **Evolve** - Challenges adapt as you grow stronger
""")