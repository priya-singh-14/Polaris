import logging
import requests
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Post a New Job, {st.session_state['first_name']}.")

FLASK_BACKEND = "http://api:4000"
results = requests.get(f"{FLASK_BACKEND}/o/JobPosting").json()

st.write(results)