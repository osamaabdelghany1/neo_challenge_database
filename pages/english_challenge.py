import streamlit as st

st.set_page_config(layout="wide")




st.title("English Challenge")




c1, c2, = st.columns(2)

with c1:
    st.header("American English")
    st.image("assets/American.png", use_container_width=True)
    if st.button("start with American", use_container_width=True):
        st.switch_page("pages/american_english.py")

with c2:
    st.header("British English")
    st.image("assets/Bretish.png", use_container_width=True)
    if st.button("start with Britch", use_container_width=True):
        st.switch_page("pages/British_english.py")
