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
    response = requests.get("http://web-api:4000/u/Employers")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching employers")
        return []

# Fetch Companies
def fetch_companies():
    response = requests.get("http://web-api:4000/c/Companies")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching companies")
        return []

# Fetch User Details by userId
def fetch_user(user_id):
    response = requests.get(f"http://web-api:4000/u/User/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Error fetching user with ID {user_id}")
        return None

# Load Data
companies = fetch_companies()
employers = fetch_employers()
advisorId = 1

# Create company options list
company_options = [company['name'] for company in companies]

# Initialize employee dropdowns dictionary
employee_dropdowns = {}
for company in companies:
    company_name = company['name']
    filtered_employers = [employer for employer in employers if employer['companyId'] == company['companyId']]
    
    # Fetch user details for each filtered employer
    employer_names = []
    for employer in filtered_employers:
        user_info = fetch_user(employer['userId'])
        if user_info:
            employer_names.append({"name": user_info[0]['name'], "userId": employer['userId']})
    
    # Store the employer names in the dictionary
    employee_dropdowns[company_name] = employer_names

# Manage selected company state
selected_company = st.selectbox("Select a Company", company_options)

# Dynamically update the employer dropdown
employer_options = employee_dropdowns.get(selected_company, [])
employer_names = [emp['name'] for emp in employer_options]
selected_employer_name = st.selectbox("Select an Employer", employer_names)

# Retrieve the selected employer's userId
selected_employer = next((emp for emp in employer_options if emp['name'] == selected_employer_name), None)

# Other inputs
industry = st.text_input("Industry")
when = st.date_input("When")

# Submit Button
if st.button("Submit"):
    if selected_employer:
        # Populate the data for the API request
        the_data = {
            "speakerId": selected_employer["userId"],  # The selected employer's userId
            "organizerId": advisorId,  # Replace with actual organizerId logic if needed
            "speakerName": selected_employer_name,
            "industry": industry,
            "when": str(when),  # Convert date object to string
        }
        try:
            # POST Request to Create Event
            response = requests.post("http://web-api:4000/c/createEvent", json=the_data)
            if response.status_code == 200:
                st.success("Event Invite Sent!")
            else:
                st.error("Error creating event. Please try again later.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")
    else:
        st.error("Please select a valid employer.")