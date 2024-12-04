import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
from datetime import datetime

current_timestamp = datetime.now()
formatted_timestamp = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')

SideBarLinks()

st.header(f"Hi, {st.session_state.get('first_name', 'User')}!")
st.write('### Here are Some Jobs Related to Your Interests')

menteeId = 27

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

        for idx, job in enumerate(all_jobs):
         with st.container(border=True):
            st.subheader(job['name'])
            st.text(f"Role: {job['role']}")
            st.text(f"Description: {job['jobDesc']}")
            if st.button('Apply to Job', key=f"apply_button_{idx}"):
            
                applicant_data = {
                "studentId": menteeId,
                "jobId": job['jobNum'],
                "empId": job['empId'],
                "completed": False,
                "timeApplied": formatted_timestamp
            }
            
                st.write(applicant_data)

                try:
                    create_application = requests.post(f'http://web-api:4000/o/NewApplications', json=applicant_data)
                
                    if create_application.status_code == 200:
                        st.success(f"Application submitted for {job['role']} at {job['name']}")
                    else:
                        st.error("Error creating user profile. Please try again later.")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error connecting to server: {str(e)}")

else:
    st.write("No jobs found. Please check back later!")


