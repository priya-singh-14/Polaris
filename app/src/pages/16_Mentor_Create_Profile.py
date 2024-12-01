import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.title("Mentor Profile")
st.write("Fill out your profile details below to connect with mentees!")


with st.form(key="mentee_profile_form"):
    name = st.text_input("Name")
    profile_pic = st.file_uploader("Upload Profile Picture", type=["jpg", "png", "jpeg"])
    email = st.text_input("Email")
    major = st.text_input("Major")
    minor = st.text_input("Minor (if applicable)")
    isInSchool = st.checkbox("Are you currently a student?")
    isWorking = st.checkbox("Are you currently working?")
    currentPosition = st.text_input("If you work, what is your title and position")
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
        # All required fields are filled, save the data
        st.session_state["mentor_data"] = {
            "name": name,
            "profile_pic": profile_pic,
            "email": email,
            "major": major,
            "minor": minor,
            "college": college,
            "isInSchool": isInSchool,
            "isWorking": isWorking,
            "currentPosition": currentPosition
        }
        st.success("Profile created successfully!")
        st.write("Return to the profile page to view your details.")
