import logging
import streamlit as st
from streamlit_extras.app_logo import add_logo
import random
import time
from modules.nav import SideBarLinks
import requests
from PIL import Image, ImageDraw
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

if mentor_Id == 15 :
    mentor_Id = fetch_mentor().get("MAX(mentorId)") 
else : 
    mentor_Id = fetch_mentor().get("MAX(mentorId)") + 1

mentees = fetch_mentees(mentor_Id)
directory = "assets/"

if mentees:
    for idx, mentee in enumerate(mentees):
        with st.container(border=True):
            img_path = os.path.join(directory, mentee["profilepic"])
            if img_path!= "assets/":
                if img_path!= "assets/":
                    img = Image.open(img_path)
                    width, height = img.size
                    min_side = min(width, height)
                    left = (width - min_side) / 2
                    top = (height - min_side) / 2
                    right = (width + min_side) / 2
                    bottom = (height + min_side) / 2
                    img = img.crop((left, top, right, bottom))
                    
                    mask = Image.new("L", (min_side, min_side), 0)
                    draw = ImageDraw.Draw(mask)
                    draw.ellipse((0, 0, min_side, min_side), fill=255)
                    
                    img = img.resize((140, 140)) 
                    circular_img = Image.new("RGBA", (140, 140), (0, 0, 0, 0))
                    circular_img.paste(img, (0, 0), mask.resize((140, 140)))
                    
                    st.image(circular_img)

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

