import streamlit as st

def setup_page_config():
    st.set_page_config(
        page_title="Kanak Dahake", 
        page_icon="https://kanakjr.in/wp-content/uploads/2017/04/logokanakjr.png",
        layout="wide", 
        initial_sidebar_state="collapsed"
    )
    st.markdown(
        """<style>
    #MainMenu,stDeployButton,footer {visibility: hidden;}
    .block-container {padding-top: 1.2rem; padding-bottom: 0rem; }
    div[data-testid="stMarkdownContainer"] {padding-top: 0rem;line-height: 1.3;}                
    h1,h2,h3,h4,h5,h6,span {padding-top: 0.2rem;padding-bottom: 0.1rem;}
    html {font-size: 1.1rem;}
    </style>""",
        unsafe_allow_html=True,
    )

def display_resume(file_path):
    header, sidebar, body = "", "", ""
    with open(file_path, "r") as file:
        content = file.read()
    education_index = content.find("## Education")
    experience_index = content.find("## Experience")
    if education_index != -1 and experience_index != -1:
        header = content[:education_index]
        sidebar = content[education_index:experience_index]
        body = content[experience_index:]
    else:
        st.error("One or both of the keywords not found in the resume.")
        st.stop

    st.markdown(header, unsafe_allow_html=True)
    col1, col2 = st.columns([1.3, 3])
    col1.markdown(sidebar, unsafe_allow_html=True)
    col2.markdown(body, unsafe_allow_html=True)