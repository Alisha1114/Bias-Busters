import streamlit as st
import base64
def background(image_path):
    with open (image_path,"rb") as f:
        encoded=base64.b64encode(f.read()).decode()
    st.markdown(
        f'<style> html, body,[data-testid="stAppViewContainer"]{{height: 100%; width: 100%; margin: 0; padding: 0;}} .stApp{{background-image:url("data:image/jpg;base64,{encoded}");background-repeat:no-repeat; background-size:cover; background-position:center; min-height:100vh; min-width:100vw;}} </style>',unsafe_allow_html=True)
background('images/mars.jpeg')


st.markdown('<p style="text-align:center; padding:6px; background-color:black">Students are learning the same lesson, but some finish faster than others. What is the fairest choice?</p>',unsafe_allow_html=True)

st.title("Well done, game over!")