import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome to your Mentee Profile, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Build Profile', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_Mentee_Profile.py')

if st.button('Expand Network', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Mentee_Network.py')

if st.button('Apply To Jobs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/05_Mentee_Jobs.py')

if st.button('Chat', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/06_Mentee_Chats.py')
  