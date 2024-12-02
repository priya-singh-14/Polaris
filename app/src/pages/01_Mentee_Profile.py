import requests
from PIL import Image
import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()

st.title("Your Profile")

def fetch_mentee_profile(menteeId):
    menteeId = 3

    try:
        response = requests.get(f"http://web-api:4000/o/viewMenteeProfile/{menteeId}") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving profile: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    return None

menteeId = 3
mentee_data = fetch_mentee_profile(menteeId)

if mentee_data:
    mentee_data = mentee_data[0] 
    

    if mentee_data.get("profilepic"):
        img = Image.open(mentee_data['profilepic']) 
        st.image(img, width=200)
    else:
        st.warning("No profile picture uploaded. Uploading a profile picture will make you more noticeable to employers and mentors!")

    st.subheader(f"{mentee_data['name']}")
    st.text(f"Email: {mentee_data['email']}")
    st.text(f"Major: {mentee_data['major']}")
    
    if mentee_data.get("minor"):
        st.text(f"Minor: {mentee_data['minor']}")
    
    st.text(f"College: {mentee_data['college']}")
    st.text(f"Bio: {mentee_data['bio']}")

    if mentee_data.get("resume") and mentee_data["resume"].lower() != "none":
        resume_path = mentee_data['resume']  # Assuming the 'resume' field is a path to the resume file
        st.text(f"Resume: {resume_path}")  # Display resume file path or URL
        st.download_button(
            label="Download Resume",
            data=open(resume_path, "rb").read(),  # Load resume file
            file_name="Resume.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("No resume uploaded. Upload a resume for extended job opportunities!")

   
    if st.button('Edit Profile', type='primary', use_container_width=True):
        st.switch_page('pages/08_Mentee_Edit_Profile.py')
else:
    st.warning("No profile information found. Please Create Your Profile.")
    if st.button('Create Profile', type='primary', use_container_width=True):
        st.switch_page('pages/07_Mentee_Create_Profile.py')