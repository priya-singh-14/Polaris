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


with st.form(key="mentee_profile_form"):
    menteeId = 3
    
    get_mentee_data = requests.get('http://web-api:4000/o/getMenteeData/{menteeId}')
    if get_mentee_data.status_code == 200:
        mentee_data = get_mentee_data.json()

    name = st.text_input("name", mentee_data.get("name"))
    profile_pic = st.file_uploader("Upload Profile Picture", type=["jpg", "png", "jpeg"])
    uploaded_resume = st.file_uploader("Upload Resume", type=["pdf"])
    email = st.text_input(email)
    major = st.text_input(major)
    minor = st.text_input(minor)
    bio = st.text_input(bio)
    college = st.selectbox(
        college,
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
        
        profile_pic_path = ""
        if profile_pic:
            profile_pic_path = os.path.join(directory, profile_pic.name)
            with open(profile_pic_path, "wb") as f:
                f.write(profile_pic.getbuffer())

        resume_path = ""
        if uploaded_resume:
            resume_path = os.path.join(directory, uploaded_resume.name)
            with open(resume_path, "wb") as f:
                f.write(uploaded_resume.getbuffer())  

        generate_userid_response = requests.get('http://web-api:4000/o/generateUserID')
        if generate_userid_response.status_code == 200:
                new_userID = generate_userid_response.json().get("new_userID")
                st.info(f"Generated userID: {new_userID}")
                
        else:
                st.error("Error generating userID. Please try again later.")

        profile_data = {
            "name": name,
            "profilepic": profile_pic_path,
            "email": email,
            "major": major,
            "minor": minor,
            "college": college,
            "bio": bio,
            "resume": resume_path,
            "userID": new_userID
        }
      
        try:
            create_user_response = requests.post('http://web-api:4000/o/createNewUser', json=profile_data)
             
            if create_user_response.status_code == 200:
                st.info("View Profile Details on the Previous Page")
            else:
                st.error("Error creating user profile. Please try again later.")

            create_mentee_response = requests.post('http://web-api:4000/o/createNewMentee', json=profile_data)

            if create_mentee_response.status_code == 200:
                st.success("Mentee profile created successfully!")
            else:
                st.error("Error creating mentee profile. Please try again later.")
                
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")
