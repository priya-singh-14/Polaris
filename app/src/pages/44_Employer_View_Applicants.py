import logging
logger = logging.getLogger(__name__)
import requests

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title(f"Submitted Applications")
st.write(st.session_state['jobNum'])

jobId = st.session_state['jobNum']
if isinstance(jobId, set):
    jobId = next(iter(jobId)) 

def fetch_job_applications(jobId):
    try:
        response = requests.get(f"http://web-api:4000/o/JobApplications/{jobId}") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving profile: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    return None


all_applications = fetch_job_applications(2)
if all_applications:
        for application in all_applications:
            with st.container():
                st.subheader(application['name'])
                st.write(f"**Major:** {application['major']}")
                st.write(f"**Minor:** {application['minor'] if application['minor'] else 'Not specified'}")
                st.write(f"**Application Submitted:** {application['timeApplied']}")
                
                if st.button(f"Visit {application['name']}'s Profile"):
                    st.session_state['menteeId'] = application['menteeId']
                    st.switch_page('pages/45_Employer_Visit_Profile.py')
else:
        st.warning("No applications found.")