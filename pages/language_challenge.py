import streamlit as st

from pages.register import height



st.set_page_config(layout="wide")




st.title("Language Challenge")


c1, c2, c3 = st.columns(3)

with c1:
    st.header("English")
    st.image("assets/English.jpg")
    st.write("The most important language to learn.")
    if st.button("start English chalenge", use_container_width=True):
        st.switch_page("pages/english_challenge.py")

with c2:
    st.header("German")
    st.image("assets/German.jpg")
    st.write("The most language that its peaple proud of it.")
    if st.button("Start german chalenge",use_container_width=True):
        st.switch_page("pages/german_challenge.py")

with c3:
    st.header("French")
    st.image("assets/French.png")
    st.write("French is spoken in 29 counries worldwide.")
    if  st.button("start french chalenge", use_container_width=True):
         st.switch_page("pages/french_challenge.py")
