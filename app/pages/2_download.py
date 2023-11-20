import base64
import os

import streamlit as st
from utils import setup_page_config
    
def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def displayPDF(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width=90% height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

dir_path = './resume_pdf/'
files = list_files(dir_path)
st.markdown("## Download Resume")
selected_tab = st.radio('Select File:',files,horizontal=True)
displayPDF(f'./resume_pdf/{selected_tab}')