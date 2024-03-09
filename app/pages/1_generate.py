from utils import get_llm
from dotenv import load_dotenv
from utils import display_resume
load_dotenv('./.env')

# Streamlit app to get job description and generate resume
import streamlit as st
from generate_resume import generate_resume_with_job_description

st.markdown("# Generate Resume")

filename = None
job_description = st.text_area("Enter job description", "We are looking for a software engineer with 3 years of experience in Python and Django.")
if st.button("Generate Resume"):
    llm = get_llm(max_tokens=2000)
    st.session_state['filename'] = generate_resume_with_job_description(job_description=job_description, llm=llm)

# if st.session_state['filename'] then Show the resume
if 'filename' in st.session_state:
    display_resume(st.session_state['filename'])