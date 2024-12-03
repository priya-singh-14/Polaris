import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
from PIL import Image
import os

SideBarLinks()

st.subheader(f"Which Mentee Would You Like To Chat With, {st.session_state['first_name']}.")

def fetch_mentees(mentor_id):
    response = requests.get(f"http://web-api:4000/o/MentorMentees/{mentor_id}", params={"mentor_id": mentor_id})
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: {response.json().get('error')}")
        return []

def fetch_mentor():
    response = requests.get("http://web-api:4000/o/mostRecentMentor")
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: {response.json().get('error')}")
        return []

mentor_Id = fetch_mentor().get("MAX(mentorId)")
mentees = fetch_mentees(mentor_Id)
directory = "assets/"

if mentees:
    for idx, mentee in enumerate(mentees):
        with st.container(border=True):
            img_path = os.path.join(directory, mentee["profilepic"])
            if os.path.exists(img_path):
                img = Image.open(img_path)
                st.image(img, width=100)
            else:
                st.write("No profile picture available.")

            st.write(f"{mentee['name']}")
            if st.button(f"Chat with {mentee['name']}", key=mentee['menteeId']):
                st.session_state['recipientId'] = mentee['menteeId']
                st.switch_page('pages/18_Mentor_Chat_With_Mentee.py')
else:
    st.write("No mentees found.")