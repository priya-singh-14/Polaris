import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Welcome, Administrator')

if st.button('Update ML Models', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_ML_Model_Mgmt.py')

if st.button('View Mentors and Mentees', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_View_Students.py')

if st.button('Schedule a Networking Event', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Create_Event.py')

if st.button('Update Mentor/Mentee Matches', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/24_Match_Management.py')

if st.button('Chat with Other Users', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/25_Advisor_Chat.py')

