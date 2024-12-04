import streamlit as st
import requests
import logging
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
SideBarLinks()

# App Title
st.title('Schedule a Networking Event')

# Fetch Employers
def fetch_employers():
    response = requests.get("http://web-api:4000/o/Employers")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching employers")
        return []

# Fetch Companies
def fetch_companies():
    response = requests.get("http://web-api:4000/o/Companies")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching companies")
        return []

# Fetch User Details by userId
def fetch_user(user_id):
    response = requests.get(f"http://web-api:4000/o/User/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Error fetching user with ID {user_id}")
        return None

# Load Data
companies = fetch_companies()
employers = fetch_employers()

# Create company options list
company_options = [company['name'] for company in companies]

# Initialize employee dropdowns dictionary
employee_dropdowns = {}

# Loop through each company and filter employees
for company in companies:
    company_name = company['name']
    
    # Filter employers based on companyId (assumed relationship)
    filtered_employers = [employer for employer in employers if employer['companyId'] == company['companyId']]

    # Fetch user details for each filtered employer
    employer_names = []
    for employer in filtered_employers:
        user_info = fetch_user(employer['userId'])
        if user_info:
            employer_names.append(user_info[0]['name'])
    
    # Store the employer names in the dictionary
    employee_dropdowns[company_name] = employer_names

# Event Scheduling Form
with st.form(key="create_event_form"):
    # Select Company (store in session_state to trigger re-render on change)
    selected_company = st.selectbox("Select a Company", company_options, key="company_selectbox")

    # When the selected company changes, update the employer dropdown
    if selected_company in employee_dropdowns:
        selected_employer = st.selectbox("Select an Employer", employee_dropdowns[selected_company], key="employer_selectbox")
    else:
        selected_employer = None
        st.warning("No employers found for the selected company.")

    speakerName = st.text_input("Speaker Name")
    industry = st.text_input("Industry")
    when = st.date_input("When")

    submit_button = st.form_submit_button(label="Submit")

# Handle Submission
if submit_button:
    if not selected_company:
        st.error("Company is required.")
    elif not selected_employer:
        st.error("Employer is required.")
    elif not speakerName:
        st.error("Speaker name is required.")
    elif not industry:
        st.error("Industry is required.")
    elif not when:
        st.error("Day of event is required.")
    else:
        # Create Event Data
        event_data = {
            "speakerId": selected_employer,  # Refers to the selected employer
            "speakerName": speakerName,
            "industry": industry,
            "when": str(when)  # Convert date to string
        }
        
        try:
            # POST Request to Create Event
            response = requests.post("http://web-api:4000/o/createEvent", json=event_data)
            if response.status_code == 200:
                st.success("Event successfully scheduled!")
            else:
                st.error("Error creating event. Please try again later.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")