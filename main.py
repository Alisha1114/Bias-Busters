import streamlit as st
import base64

def background(image_path):
    with open (image_path,"rb") as f:
        encoded=base64.b64encode(f.read()).decode()
    st.markdown(
        f'<style> html, body,[data-testid="stAppViewContainer"]{{height: 100%; width: 100%; margin: 0; padding: 0;}} .stApp{{background-image:url("data:image/jpg;base64,{encoded}");background-repeat:no-repeat; background-size:cover; background-position:center; min-height:100vh; min-width:100vw;}} </style>',unsafe_allow_html=True)
background('images/space.jpeg')

#st.markdown("<style> .stApp{background-color: #5b3e31;}</style>", unsafe_allow_html=True)

st.markdown('<h1 style="text-align: center;">Bias Busters</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center;">Can you spot all the biases?</h2>', unsafe_allow_html=True)
col1, col2, col3=st.columns([1,3,1])
with col2:
    if st.button("Lets play!", use_container_width=True):
        st.switch_page("pages/choose_level.py")

#streamlit run main.py