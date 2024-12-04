import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.header(f"Here Are Your Submitted Applications, {st.session_state['first_name']}.")

def get_applications(menteeId):
    try:
        response = requests.get(f"http://web-api:4000/o/Applications/{menteeId}") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving profile: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    return None


menteeId = 4
mentee_applications = get_applications(menteeId)

if mentee_applications:
        for application in mentee_applications:
            with st.container(border=True):
                st.write(f"**Company:** {application['name']}")
                st.write(f"**Role:** {application['role']}")
                st.write(f"**Application Submitted:** {application['timeApplied']}")
                
                application_data = {
                     "studentId" : menteeId,
                     "jobId" : application['jobId']
                }
                st.write(application_data)
                jobId = application['jobId']

                if st.button(f"Withdraw from Job"):
                    try:
                        response = requests.delete(f"http://web-api:4000/o/DeleteApplication", json=application_data) 
                        if response.status_code == 200:
                            st.info("Application Withdrawn")
                        else:
                            st.error(f"Error withdrawing Applicaton: {response.json().get('error', 'Unknown error')}")
                    except requests.exceptions.RequestException as e:
                        st.error(f"Error connecting to server: {str(e)}")
else:
        st.warning("No applications found.")