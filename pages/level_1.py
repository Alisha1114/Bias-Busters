import streamlit as st

st.markdown('<h1 style="text-align: center;">Level 1:</h1>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align: center;">Gender Bias</h1>', unsafe_allow_html=True)
col1, col2, col3=st.columns([1,1,1])
with col2:
    if st.button("Start!"):
        st.switch_page("pages/level1_q1.py")

