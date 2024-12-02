import logging
import pandas as pd
import streamlit as st
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

SideBarLinks()

st.header(f"Hi, {st.session_state.get('first_name', 'User')}!")
st.write('### Here are Some Jobs Related to Your Interests')


def get_all_jobs():
    try:
        response = requests.get("http://web-api:4000/o/JobPosting") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving jobs: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    return None

all_jobs = get_all_jobs()

if all_jobs:

    if all_jobs:

        for idx, job in enumerate(all_jobs):
         st.subheader(job['name'])
         st.text(f"Role: {job['role']}")
         st.text(f"Description: {job['jobDesc']}")
         if st.button('Apply to Job', key=f"apply_button_{idx}"):
            st.success(f"Application submitted for {job['role']} at {job['name']}")

    

else:
    st.write("No jobs found. Please check back later!")
