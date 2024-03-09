import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

from langchain.cache import SQLiteCache
from langchain.globals import set_llm_cache

set_llm_cache(SQLiteCache(database_path=".langchain.db"))

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

def get_llm(OPENAI_MODEL=None, max_tokens=1000):
    if not OPENAI_MODEL:
        OPENAI_MODEL = os.environ.get("OPENAI_MODEL")
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    llm = ChatOpenAI(
        temperature=0,
        model_name=OPENAI_MODEL,
        openai_api_key=OPENAI_API_KEY,
        max_tokens=max_tokens,
    )
    return llm

def get_openAPI_response(text, task, OPENAI_MODEL=None, max_tokens=1000, llm=None):
    messages = [HumanMessage(content=text)]
    llm = get_llm(OPENAI_MODEL=OPENAI_MODEL, max_tokens=max_tokens)
    response = llm.invoke(messages, config={"run_name": task})
    response = str(response.content)
    return response

def save_to_md_file(job_description_name, text):
    # Replace blank spaces with "-"
    filename = job_description_name.replace(" ", "-") + ".md"
    # Create the "articles" folder if it doesn't exist
    folder_path = "resume_md"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Create and write to the Markdown file
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "w") as file:
        file.write(f"{text}")
    print(f"File '{filename}' saved successfully in the 'resume_md' folder.")
    return file_path