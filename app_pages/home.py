import streamlit as st

st.title("✨ Daily Challenge")
st.caption("Transform your daily routine with fun and engaging challenges")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("🏋️ Sports")
    st.image("assets/sport_challenge.png", width="stretch", caption="Stay fit and active")
    
    st.write("Daily physical activities to boost your energy and improve your fitness level.")
    
    
    if st.button("Start sports challenge", type="primary", width="stretch"):
        st.switch_page("app_pages/view_challenges.py")
        
        
with col2:
    st.subheader("🗣️ Language")
    
    st.image("assets/language_challenge.png", width="stretch", caption="Expand your vocabulary")
    
    st.write("""
             Daily words and phrases in English, French and German
             .
             """)
    if st.button("Start language challenge", type="primary", width="stretch"):
        st.switch_page("app_pages/language_challenge.py")
        
with col3:
    st.subheader("🧠 General knowledge")
    st.image("assets/General-Knowledge.jpg", width="stretch", caption="Expand your knowledge")

    st.write("""
             Daily facts and trivia to boost your general knowledge
             .
             """)
    if st.button("Start the quiz", type="primary", width="stretch"):
        st.switch_page("app_pages/general_knowledge.py")

st.divider()

st.subheader("More ways to train")
col1, col2 = st.columns(2)
with col1:
    if st.button("🏋️ Workout by equipment", type="primary", width="stretch"):
        st.switch_page("app_pages/workout.py")
with col2:
    if st.button("💪 See all exercises", type="primary", width="stretch"):
        st.switch_page("app_pages/view_exercise.py")

st.markdown("""
## How it works
1. **Pick a habit** - Sports, Language or General Knowledge
2. **Choose your level** - Easy, Medium or Hard
3. **Do a short challenge** - a workout with video, a language activity, or a 10-question quiz
4. **Join it** - log in and press Start challenge to save it to your account
""")
