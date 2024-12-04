import requests
from PIL import Image
import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()

st.title("Your Profile")

def fetch_mentee():
    response = requests.get("http://web-api:4000/o/mostRecentMentee")
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: {response.json().get('error')}")
        return []

def fetch_mentee_profile(menteeId):
    try:
        response = requests.get(f"http://web-api:4000/o/viewMenteeProfile/{menteeId}") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving profile: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    return None

menteeId = fetch_mentee().get("MAX(menteeId)")

st.write(st.session_state['profile_built'])
st.write(menteeId)

if menteeId == 15 :
    menteeId = fetch_mentee().get("MAX(menteeId)")
    mentee_data = fetch_mentee_profile(menteeId)

else :
    menteeId = fetch_mentee().get("MAX(menteeId)") + 1
    mentee_data = fetch_mentee_profile(menteeId)

if mentee_data:
    st.session_state['profile_built'] = True
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
        resume_path = mentee_data['resume']  
        st.text(f"Resume:")  
        st.download_button(
            label="Download Resume",
            data=open(resume_path, "rb").read(),
            file_name="Resume.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("No resume uploaded. Upload a resume for extended job opportunities!")

   
    if st.button('Edit Profile', type='primary', use_container_width=True):
        st.switch_page('pages/08_Mentee_Edit_Profile.py')
else:
    st.warning("No profile information found. Please Create Your Profile.")
    st.session_state['profile_built'] = False
    if st.button('Create Profile', type='primary', use_container_width=True):
        st.switch_page('pages/07_Mentee_Create_Profile.py')