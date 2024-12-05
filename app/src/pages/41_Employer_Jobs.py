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
        response = requests.get(f"http://web-api:4000/c/EmployerJobs/{empId}") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving profile: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    return None

all_jobs = fetch_job_postings(1)

if all_jobs:
    for job in all_jobs:
        status = "Open" if job['filledBool'] == 0 else "Filled"

        with st.container(border=True):
            st.text(f"{job['jobDesc']}")
            st.text(f"Position: {job['role']}")
            st.text(f"Position Status : {status}")

            job_data = {
            "empId" : 1,
            "jobId" : job['jobNum']
             }
            
            if st.button(f"View Applications for Job {job['jobNum']}", key=job['jobNum']):
                st.session_state['jobNum'] = job['jobNum']
                st.switch_page('pages/44_Employer_View_Applicants.py')

            if st.button(f"Delete Job {job['jobNum']}", type="primary", key=job['jobNum']+1):
                st.session_state['jobNum'] = job['jobNum']
                try:
                        response = requests.delete(f"http://web-api:4000/c/DeleteJobPosting", json=job_data) 
                        if response.status_code == 200:
                            st.info("Job Posting Removed")
                        else:
                            st.error(f"Error withdrawing Applicaton: {response.json().get('error', 'Unknown error')}")
                except requests.exceptions.RequestException as e:
                        st.error(f"Error connecting to server: {str(e)}")