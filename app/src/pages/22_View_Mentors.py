###
import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('View a List of Active Mentors')

def view_mentor_ls():

    try:
        response = requests.get(f"http://web-api:4000/o/viewMentorList") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving list: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    return None

