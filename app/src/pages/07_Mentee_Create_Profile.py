import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
import os

SideBarLinks()

directory = "assets/"

st.title("Mentee Profile")
st.write("Fill out your profile details below to connect with mentors and other students!")


with st.form(key="mentee_profile_form"):
    name = st.text_input("Name")
    profile_pic = st.file_uploader("Upload Profile Picture", type=["jpg", "png", "jpeg"])
    uploaded_resume = st.file_uploader("Upload Resume", type=["pdf"])
    email = st.text_input("Email")
    major = st.text_input("Major")
    minor = st.text_input("Minor (if applicable)")
    bio = st.text_input("Write a brief bio")
    college = st.selectbox(
        "College",
        ["College of Engineering", "College of Social Sciences and Humanities", "Khoury College of Computer Science", 
         "Bouve College of Health Sciences", "College of Arts, Media, and Design", "D'Amore-McKim College of Business", "College of Science"]
    )

    submit_button = st.form_submit_button(label="Submit")

if submit_button:
     if not name:
        st.error("Name is required.")
     elif not email:
        st.error("Email is required.")
     elif not major:
        st.error("Major is required.")
     elif not college:
        st.error("College is required.")
     else:
        
        profile_pic_path = None
        if profile_pic:
            profile_pic_path = os.path.join(directory, profile_pic.name)
            with open(profile_pic_path, "wb") as f:
                f.write(profile_pic.getbuffer())

        resume_path = None
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
            "resume": resume_path
        }
      
        try:
            response = requests.post('http://web-api:4000/o/createMenteeProfile', json=profile_data)
            if response.status_code == 200:
                st.success("Profile created successfully!")
                st.write("Return to the profile page to view your details.")
            else:
                st.error(f"Error creating profile: Profile already exists under this email")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")
                            
