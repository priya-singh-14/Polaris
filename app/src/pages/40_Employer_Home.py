import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Employer, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View Active Job Postings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/41_Employer_Jobs.py')

if st.button('Post a New Job', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/42_Employer_Post_New_Job.py')

if st.button("Explore Candidates",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/43_Employer_Find_Candidates.py')

if st.button('Manage Events', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/45_Employer_Events.py')