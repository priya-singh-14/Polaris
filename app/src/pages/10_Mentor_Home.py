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

if 'profile_built' not in st.session_state:
    st.session_state['profile_built'] = False

if st.session_state['profile_built']:
  if st.button('View Profile', 
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

else :
  st.info("It seems like you haven't built your profile yet. Add your details and unlock aditional functionality", icon="⚠️")
  if st.button('View Profile', 
             type='primary',
             use_container_width=True):
      st.switch_page('pages/11_Mentor_Profile.py')