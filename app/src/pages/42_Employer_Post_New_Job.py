import logging
import requests
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()


# empId = st.session_state['empId']
# if isinstance(empId, set):
#     empId = next(iter(empId)) 

# companyId = st.session_state['companyId']
# if isinstance(companyId, set):
#     companyId = next(iter(companyId))
    
# st.write(empId)
# st.write(companyId)

empId = 1
companyId = 1
status = False

st.title(f"Post a New Job, {st.session_state['first_name']}.")
with st.form(key="new_job_form"):
    role = st.text_input("Role")
    description = st.text_input("Description")
    company = st.text_input("Company")
    desiredMajors = st.text_input("Desired Majors (as a comma separated list)")

    submit_button = st.form_submit_button(label="Post Job")

    if submit_button:
        if not role:
         st.error("Role is required.")
        elif not description:
         st.error("Job description is required.")
        elif not company:
         st.error("Company is required.")
        elif not desiredMajors:
         st.error("Company is required.")

        else:
            job_data = {
            "empId": empId,
            "companyId": companyId,
            "jobDesc": description,
            "role": role,
            "filledBool": status,
            "majors": desiredMajors
            }

        st.write(job_data)


        try:
            create_new_job = requests.post('http://web-api:4000/o/NewJobPosting', json=job_data)
             
            if create_new_job.status_code == 200:
                st.info("Job Posted")
            else:
                st.error("Error posting this job. Please try again later.") 
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")

    