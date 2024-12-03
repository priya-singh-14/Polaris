import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Mentor, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Build Profile', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Mentor_Profile.py')

if st.button('View Network', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Mentor_Network.py')

if st.button("Match Mentees to Jobs",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Mentor_Matching.py')


if st.button("Chat",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Mentor_Chats.py')
