import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

# def fetch_mentees(mentor_id):
#     response = requests.get("http://web-api:4000/o/MentorMentees", params={"mentor_id": mentor_id})
    
#     if response.status_code == 200:
#         return response.json()["mentees"]
#     else:
#         st.error(f"Error fetching mentees: {response.json().get('error')}")
#         return []

st.title(f"Your Network, {st.session_state['first_name']}.")

# mentees = fetch_mentees(2)

# if mentees:
#     for mentee in mentees:
#         st.write(f"**Name**: {mentee['name']}")
#         st.write(f"**Bio**: {mentee['bio']}")
#         st.write(f"**Resume**: {mentee['resume']}")
#         st.markdown("---")
# else:
#     st.write("No mentees found.")

# st.write('')
# st.write('')

if st.button('Find More Mentees', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/15_Mentor_Find_Mentees.py')
