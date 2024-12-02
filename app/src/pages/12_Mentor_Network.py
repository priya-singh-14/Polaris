import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests
from PIL import Image
import os

directory = 'assets/'
st.set_page_config(layout='wide')

SideBarLinks()

def fetch_mentees(mentor_id):
    response = requests.get("http://web-api:4000/o/MentorMentees/1", params={"mentor_id": mentor_id})
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: {response.json().get('error')}")
        return []

st.title(f"Your Network, {st.session_state['first_name']}.")

mentees = fetch_mentees(1)

if mentees:
    for idx, mentee in enumerate(mentees):
        img_path = os.path.join(directory, mentee["profilepic"])
        if os.path.exists(img_path):
            img = Image.open(img_path)
            st.image(img, width=200)
        else:
            st.write("No profile picture available.")

        st.write(f"**Name**: {mentee['name']}")
        st.write(f"**Major**: {mentee['major']}")
        st.write(f"**Bio**: {mentee['bio']}")

        if mentee['resume'] and mentee['resume'].lower() != "none":
            resume_path = os.path.join(directory, mentee['resume'])
            if os.path.exists(resume_path):
                st.download_button(
                    label="Download Resume",
                    data=open(resume_path, "rb").read(),
                    file_name=f"{mentee['name']}_Resume.pdf",
                    mime="application/pdf",
                    key=f"resume_{idx}" 
                )
        else:
            st.write("Resume not available.")
        st.markdown("---")
else:
    st.write("No mentees found.")


st.write('')
st.write('')

if st.button('Find More Mentees', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/15_Mentor_Find_Mentees.py')
