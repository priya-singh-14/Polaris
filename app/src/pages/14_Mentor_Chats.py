import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
import requests
from modules.nav import SideBarLinks

SideBarLinks()

st.subheader(f"Who Would You Like To Chat With, {st.session_state['first_name']}.")

def fetch_mentees(mentor_id):
    response = requests.get("http://web-api:4000/o/MentorMentees/1", params={"mentor_id": mentor_id})
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: {response.json().get('error')}")
        return []

mentees = fetch_mentees(1)