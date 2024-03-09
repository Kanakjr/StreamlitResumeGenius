from utils import setup_page_config, display_resume
import os
import streamlit as st

# Function to list all files in a directory
def list_files(directory):
    # List comprehension to get files (not directories) within the given directory
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Directory path containing the markdown files
dir_path = './resume_md/'

# Getting the list of files in the specified directory
files = list_files(dir_path)

#Sorting the files
files.sort()

# Setting up page configuration using a utility function (not shown)
setup_page_config()

# Using st.sidebar.radio to add a radio button selection to the sidebar.
# 'Select File:' is the label shown above the radio button.
# 'files' is the list of file names to choose from.
# 'horizontal=True' is to align the radio buttons horizontally. (Note: As of my last update, Streamlit does not support horizontal alignment for sidebar widgets directly. If this feature is essential, consider checking Streamlit's latest documentation for any updates or workarounds.)
file_path = dir_path + st.sidebar.radio('Select Resume:', files,index=files.index('0_Main.md'))

# Displaying the resume based on the selected file using a utility function (not shown)
display_resume(file_path)