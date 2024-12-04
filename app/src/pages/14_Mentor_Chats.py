import logging
import streamlit as st
from streamlit_extras.app_logo import add_logo
import random
import time
from modules.nav import SideBarLinks
import requests
from PIL import Image
import os

# Logging setup
logger = logging.getLogger(__name__)

# Add Sidebar Links
SideBarLinks()

# Add Logo
add_logo("assets/logo.png", height=400)

# Page title
st.title("Mentor's Chat Dashboard 📚")

# Page description
st.markdown("""
Welcome to your mentor dashboard! This page allows you to interact with your matched mentees, track their progress, and share resources to help them grow.
""")

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
            if img_path!= "assets/":
                img = Image.open(img_path)
                st.image(img, width=100)
            else:
                st.write("No profile picture available.")

            st.write(f"{mentee['name']}")
            if st.button(f"Chat with {mentee['name']}", key=mentee['menteeId']):
                st.session_state['recipientId'] = mentee['menteeId']
                st.switch_page('pages/18_Mentor_Chat_With_Mentee.py')
else:
    st.info("No mentees found.")

st.subheader("Share Resources with All Your Mentees")
uploaded_file = st.file_uploader("Upload a guide, article, or book recommendation (PDF only)", type="pdf")
if uploaded_file:
    st.success("Resource uploaded successfully!")
    st.write(f"Shared: {uploaded_file.name}")

