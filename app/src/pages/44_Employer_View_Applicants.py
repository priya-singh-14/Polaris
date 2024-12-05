import logging
logger = logging.getLogger(__name__)
import requests

import streamlit as st
from modules.nav import SideBarLinks
import os

st.set_page_config(layout = 'wide')

directory = 'assets/'

SideBarLinks()

st.title(f"Submitted Applications")
# st.write(st.session_state['jobNum'])

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


all_applications = fetch_job_applications(jobId)
if all_applications:
        for application in all_applications:
            with st.container(border=True):
                st.subheader(application['name'])
                st.write(f"**Major:** {application['major']}")
                st.write(f"**Minor:** {application['minor'] if application['minor'] else 'Not specified'}")
                st.write(f"**Application Submitted:** {application['timeApplied']}")

                if "assets/" not in application["resume"] and application['resume'] and application['resume'].lower() != "none":
                    resume_path = os.path.join(directory, application['resume'])
                    if os.path.exists(resume_path):
                        st.download_button(
                        label="Download Resume",
                        data=open(resume_path, "rb").read(),
                        file_name=f"{application['name']}_Resume.pdf",
                        mime="application/pdf",
                        key=f"resume_{application['menteeId']}" 
                    )
                elif "assets/" in application["resume"] and application['resume'] and application['resume'].lower() != "none":
                        resume_path = application['resume']
                        if os.path.exists(resume_path):
                            st.download_button(
                            label="Download Resume",
                            data=open(resume_path, "rb").read(),
                            file_name=f"{application['name']}_Resume.pdf",
                            mime="application/pdf",
                            key=f"resume_{application['menteeId']}" 
                        )
                else:
                    st.write("Resume not available.")

        

                mailto_link = f"mailto:{application['email']}"
                st.markdown(f"[Contact {application['name']}]({mailto_link})", unsafe_allow_html=True)
                    
                    
else:
        st.warning("No applications found.")