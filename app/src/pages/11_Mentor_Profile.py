import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
from PIL import Image, ImageDraw

st.set_page_config(layout = 'wide')

SideBarLinks()

def fetch_mentor_profile(mentorId):
    try:
        response = requests.get(f"http://web-api:4000/o/viewMentorProfile/{mentorId}") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving profile: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    return None

def fetch_mentor():
    response = requests.get("http://web-api:4000/o/mostRecentMentor")
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: {response.json().get('error')}")
        return []
    

mentorId = fetch_mentor().get("MAX(mentorId)")

if mentorId == 15 :
    mentorId = fetch_mentor().get("MAX(mentorId)")
    mentor_data = fetch_mentor_profile(mentorId)

else :
    mentorId = fetch_mentor().get("MAX(mentorId)") + 1
    mentor_data = fetch_mentor_profile(mentorId)

if mentor_data:
    st.session_state['profile_built'] = True
    mentor_data = mentor_data[0] 

    if mentor_data.get("profilepic"):
                img = Image.open(mentor_data['profilepic']) 
                st.write(f'{mentor_data.get("profilepic")}')
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
        st.warning("No profile picture uploaded.")

    st.subheader(f"{mentor_data['name']}")
    st.text(f"Email: {mentor_data['email']}")
    st.text(f"Major: {mentor_data['major']}")
    
    if mentor_data.get("minor"):
        st.text(f"Minor: {mentor_data['minor']}")
    
    st.text(f"College: {mentor_data['college']}")
   
    if mentor_data.get("isWorking"):
        st.text(f"{mentor_data['currentPosition']} at {mentor_data['company']}")
        
    if st.button('Edit Profile', type='primary', use_container_width=True):
        st.switch_page('pages/17_Mentor_Edit_Profile.py')
else:
    st.warning("No profile information found. Please Create Your Profile.")
    st.session_state['profile_built'] = False
    if st.button('Create Profile', type='primary', use_container_width=True):
        st.switch_page('pages/16_Mentor_Create_Profile.py')