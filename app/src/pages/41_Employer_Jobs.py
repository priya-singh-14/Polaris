import logging
logger = logging.getLogger(__name__)
import requests

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Jobs You've Posted, {st.session_state['first_name']}.")


def fetch_job_postings(empId):
    try:
        response = requests.get(f"http://web-api:4000/o/EmployerJobs/{empId}") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving profile: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    return None

all_jobs = fetch_job_postings(1)

if all_jobs:
    all_jobs = all_jobs[0] 

    status = "Open" if all_jobs['filledBool'] == 0 else "Filled" 

    with st.container(border=True):
        st.text(f"{all_jobs['jobDesc']}")
        st.text(f"Position: {all_jobs['role']}")
        st.text(f"Position Status : {status}")
        if st.button('View Applications', type='primary', use_container_width=True):
            st.switch_page('pages/44_Employer_View_Applicants.py')