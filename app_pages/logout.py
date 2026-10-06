import streamlit as st

# Forget who is logged in, then reload so the menu changes back.
st.session_state.clear()
st.rerun()
