import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
import os

SideBarLinks()

def get_advisor(college):
    try:
        response = requests.get(f"http://web-api:4000/o/PairAdvisor/{college}") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving profile: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    return None

directory = "assets/"

st.title("Mentor Profile")
st.write("Fill out your profile details below to connect with students!")

with st.form(key="mentor_profile_form"):
    name = st.text_input("Name")
    profile_pic = st.file_uploader("Upload Profile Picture", type=["jpg", "png", "jpeg"])
    email = st.text_input("Email")
    major = st.text_input("Major")
    minor = st.text_input("Minor (if applicable)")
    isInSchool = st.checkbox("Are you currently a student?")
    isWorking = st.checkbox("Are you currently working?")
    currentPosition = st.text_input("If you work, what is your title and position")
    company = st.text_input("Which company do you work?")
    college = st.selectbox(
        "College When Admitted",
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
        advisorID = get_advisor(college)['advisorId']
        
        profile_pic_path = ""
        if profile_pic:
            profile_pic_path = os.path.join(directory, profile_pic.name)
            with open(profile_pic_path, "wb") as f:
                f.write(profile_pic.getbuffer())

        generate_userid_response = requests.get('http://web-api:4000/o/generateUserID')
        if generate_userid_response.status_code == 200:
                new_userID = generate_userid_response.json().get("new_userID")
                # st.info(f"Generated userID: {new_userID}")
                
        else:
                st.error("Error generating userID. Please try again later.")

        profile_data = {
            "name": name,
            "profilepic": profile_pic_path,
            "email": email,
            "major": major,
            "minor": minor,
            "college": college,
            "company": company,
            "isInSchool": isInSchool,
            "isWorking": isWorking,
            "currentPosition": currentPosition,
            "userID": new_userID,
            "advisorID": advisorID
        }
        st.session_state['profile_built'] = True

        try:
            create_user_response = requests.post('http://web-api:4000/o/createNewUser', json=profile_data)
             
            # if create_user_response.status_code == 200:
            #     st.info("View Profile Details on the Previous Page")
            # else:
            #     st.error("Error creating user profile. Please try again later.")

            create_mentor_response = requests.post('http://web-api:4000/o/createNewMentor', json=profile_data)

            if create_mentor_response.status_code == 200:
                st.success("Mentor profile created successfully!")
                st.session_state['profile_built'] = True
            else:
                st.error("Error creating mentor profile. Please try again later.")
                
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")
