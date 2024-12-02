import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
import os

SideBarLinks()

directory = "assets/"

st.title("Edit Mentor Profile")
st.write("Edit your profile details!")


mentorId = 4
mentor_data = {}

get_mentor_data = requests.get(f'http://web-api:4000/o/getMentorData/{mentorId}')
if get_mentor_data.status_code == 200:
    mentor_data = get_mentor_data.json()

with st.form(key="mentor_profile_form"):
    name = st.text_input("Name", mentor_data.get("name"))
    profile_pic = st.file_uploader("Upload New Profile Picture", type=["jpg", "png", "jpeg"])
    email = st.text_input("email", mentor_data.get("email"))
    major = st.text_input("major", mentor_data.get("major"))
    minor = st.text_input("minor", mentor_data.get("minor"))
    isInSchool = st.checkbox("Are you currently a student?", mentor_data.get("isInSchool"))
    isWorking = st.checkbox("Are you currently working?", mentor_data.get("isWorking"))
    currentPosition = st.text_input("If you work, what is your title and position")
    company = st.text_input("Which company do you work?")
    college = st.selectbox(
        "College When Admitted",
        ["College of Engineering", "College of Social Sciences and Humanities", "Khoury College of Computer Science", 
         "Bouve College of Health Sciences", "College of Arts, Media, and Design", "D'Amore-McKim College of Business", "College of Science"]
    )

    submit_button = st.form_submit_button(label="Submit")

if submit_button:
        profile_pic_path = mentor_data.get("profilepic")
        if profile_pic:
            profile_pic_path = os.path.join(directory, profile_pic.name)
            with open(profile_pic_path, "wb") as f:
                f.write(profile_pic.getbuffer())

        profile_data = {
            "name": name,
            "profilepic": profile_pic_path,
            "email": email,
            "major": major,
            "minor": minor,
            "college": college,
            "isInSchool": isInSchool,
            "isWorking": isWorking,
            "currentPosition": currentPosition,
            "company": company,
            "id": mentor_data.get("userId")
        }
    
        st.write(profile_data)

        try:
            update_user_response = requests.put('http://web-api:4000/o/updateUser', json=profile_data)

            if update_user_response.status_code == 200:
                st.success("User profile updated successfully!")
            else:
                st.error("Error updating user profile. Please try again later.")

            update_mentor_response = requests.put('http://web-api:4000/o/updateMentor', json=profile_data)

            if update_mentor_response.status_code == 200:
                st.success("Mentor profile updated successfully!")
            else:
                st.error("Error updating mentor profile. Please try again later.")
                
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")

