import streamlit as st

st.title("American English")





c1, c2, c3 = st.columns(3)

with c1:
    st.header("Easy")
with c2:
    st.header("Medium")

with c3:
    st.header("Hard")

