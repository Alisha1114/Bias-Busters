import streamlit as st

st.markdown('<h1 style="text-align: center;">Bias Busters</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center;">Can you spot all the biases?</h2>', unsafe_allow_html=True)
col1, col2, col3=st.columns([1,1,1])
with col2:
    st.button("Lets play!")
    if st.button:
        st.switch_page("pages/choose_level.py")

