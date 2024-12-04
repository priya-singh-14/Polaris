import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
import os

SideBarLinks()

directory = "assets/"

st.title("Edit Mentee Profile")
st.write("Edit your profile details!")


menteeId = 27
mentee_data = {}

get_mentee_data = requests.get(f'http://web-api:4000/o/getMenteeData/{menteeId}')
if get_mentee_data.status_code == 200:
    mentee_data = get_mentee_data.json()



with st.form(key="mentee_profile_form"):
    name = st.text_input("Name", mentee_data.get("name"))
    profile_pic = st.file_uploader("Upload New Profile Picture", type=["jpg", "png", "jpeg"])
    uploaded_resume = st.file_uploader("Upload New Resume", type=["pdf"])
    email = st.text_input("email", mentee_data.get("email"))
    major = st.text_input("major", mentee_data.get("major"))
    minor = st.text_input("minor", mentee_data.get("minor"))
    bio = st.text_input("bio", mentee_data.get("bio"))
    college = st.selectbox(
        "college",
        ["College of Engineering", "College of Social Sciences and Humanities", "Khoury College of Computer Science", 
         "Bouve College of Health Sciences", "College of Arts, Media, and Design", "D'Amore-McKim College of Business", "College of Science"]
    )

    submit_button = st.form_submit_button(label="Submit")

if submit_button:
        profile_pic_path = mentee_data.get("profilepic")
        if profile_pic:
            profile_pic_path = os.path.join(directory, profile_pic.name)
            with open(profile_pic_path, "wb") as f:
                f.write(profile_pic.getbuffer())

        resume_path = mentee_data.get("resume")
        if uploaded_resume:
            resume_path = os.path.join(directory, uploaded_resume.name)
            with open(resume_path, "wb") as f:
                f.write(uploaded_resume.getbuffer())

        profile_data = {
            "name": name,
            "profilepic": profile_pic_path,
            "email": email,
            "major": major,
            "minor": minor,
            "college": college,
            "bio": bio,
            "resume": resume_path,
            "id": mentee_data.get("userId")
        }
    
        st.write(profile_data)

        try:
            update_user_response = requests.put('http://web-api:4000/o/updateUser', json=profile_data)

            if update_user_response.status_code == 200:
                st.success("User profile updated successfully!")
            else:
                st.error("Error updating user profile. Please try again later.")

            update_mentee_response = requests.put('http://web-api:4000/o/updateMentee', json=profile_data)

            if update_mentee_response.status_code == 200:
                st.success("Mentee profile updated successfully!")
            else:
                st.error("Error updating mentee profile. Please try again later.")
                
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")

