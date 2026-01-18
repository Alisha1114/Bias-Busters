import streamlit as st
import base64

def background(image_path):
    with open (image_path,"rb") as f:
        encoded=base64.b64encode(f.read()).decode()
    st.markdown(
        f'<style> html, body,[data-testid="stAppViewContainer"]{{height: 100%; width: 100%; margin: 0; padding: 0;}} .stApp{{background-image:url("data:image/jpg;base64,{encoded}");background-repeat:no-repeat; background-size:cover; background-position:center; min-height:100vh; min-width:100vw;}} </style>',unsafe_allow_html=True)
background('images/earth.jpeg')


st.markdown('<p style="text-align:center; padding:6px; background-color:black">A new student joins your class and speaks with an accent. What should classmates do?</p>',unsafe_allow_html=True)

if "clicked" not in st.session_state:
     st.session_state.clicked=None
if "done_clicked" not in st.session_state:
    st.session_state.done_clicked = False
option=[
    ("Be patient and listen carefully.", "green", "This option is gender bias free because it includes anyone."),
    ("Assume they are not good at school.", "red", "This option shows gender bias because its states only boys are technical."),
    ("Help them learn classroom rules.","green", "This option is gender bias free because its states boys and girls as equals."),
    ("Include them in group activities.", "green", "This option is gender bias free because its includes anyone.")
]

for i, (text, color, message) in enumerate(option):
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        if st.session_state.clicked==i:
            st.markdown(f'<button style= "background-color:{color}; color:white; border:none; border-radius:none; width:100%; margin-botton:0.5rem;">{text}</button>',unsafe_allow_html=True)
            st.markdown(f'<p style="font-weight:bold; text-align: center;">{message}</p>',unsafe_allow_html=True)
        else:
            if st.button(text, key=i, use_container_width=True):
                st.session_state.clicked=i
                st.rerun()

if st.button("Done"):
    st.session_state.done_clicked = True
    st.rerun()

if st.session_state.done_clicked:
    st.markdown(
        '<p style="text-align:center; color:white; font-weight:bold; background-color:rgba(0,0,0,0.7); padding:1rem; border-radius:5px;">Bias lesson: Interests are not based on gender.</p>',
        unsafe_allow_html=True
    )

    if st.button("Next"):
        # Reset session state before switching pages
        st.session_state.clicked = None
        st.session_state.done_clicked = False
        st.switch_page("pages/level2_q2.py")

