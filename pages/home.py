import streamlit as st

st.set_page_config(page_title="Daily Challenges", page_icon="✨", layout="wide")


st.title("Daily Challenge")
st.subheader("Transform your daily routine with fun and engaging challenges")


col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🏋️ Sports")
    st.image(
        "assets/sport_challenge.png",
        use_container_width=True,
        caption="Stay fit and active",
    )
    st.write(
        "Daily physical activities to boost your energy and improve your fitness level."
    )

with col2:
    st.subheader("🗣️ Language Challenge")
    st.image(
        "assets/language_challenge.png",
        use_container_width=True,
        caption="Expand your vocabulary",
    )
    st.write(
        "Daily words and phrases to help you master English and communicate effectively."
    )


with col3:
    st.subheader("General knowledge")
    st.image(
        "assets/General-Knowledge.jpg",
        use_container_width=True,
        caption="Expand your knowledge",
    )
    st.write(
        "Daily facts and trivia to boost your general knowledge."
    )

   









c1, c2, c3 = st.columns(3)

with c1:
    
    if st.button("Start sports challenge", key="sports", use_container_width=True):
        st.switch_page("pages/view_challenges.py")


with c2:
    
    if st.button("Start language challenge", key="challenge 2", use_container_width=True):
        st.switch_page("pages/view_challenges.py")


with c3:
    
    if st.button("Start General Knowledge challenge", key="challenge 3", use_container_width=True):
        st.switch_page("pages/view_challenges.py")


st.divider()


st.markdown("""
## How It Works
1. **Choose your level** - Select from Beginner, Intermediate, or Advanced
2. **Get daily challenges** - Receive three new challenges every day
3. **Track your progress** - Watch yourself improve over time
4. **Evolve** - Challenges adapt as you grow stronger and smarter
""")


st.markdown("---")
c1, c2, c3 = st.columns([2, 2, 1])

with c2:
    st.markdown(" Daily Challenge - Transform your life, one day at a time")
