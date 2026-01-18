import streamlit as st
import base64

def background(image_path):
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f'<style> html, body,[data-testid="stAppViewContainer"]{{height: 100%; width: 100%; margin: 0; padding: 0;}} .stApp{{background-image:url("data:image/jpg;base64,{encoded}");background-repeat:no-repeat; background-size:cover; background-position:center; min-height:100vh; min-width:100vw;}} </style>',
        unsafe_allow_html=True
    )

background('images/space.jpeg')

if "clicked" not in st.session_state:
    st.session_state.clicked = None
if "done_clicked" not in st.session_state:
    st.session_state.done_clicked = False

# Bold title and text
st.markdown('<h1 style="font-weight:bold;">Level 3:</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-weight:bold; font-size:1.2rem;">Educational Bias</p>', unsafe_allow_html=True)

# Centered button
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    if st.button("Start", use_container_width=True):
        st.switch_page("pages/level3_q1.py")