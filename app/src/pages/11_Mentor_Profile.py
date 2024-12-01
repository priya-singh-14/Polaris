import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

if "mentor_data" not in st.session_state:
    st.session_state["mentor_data"] = None  

st.title("Your Profile")

if st.session_state["mentor_data"] is None:
    st.warning("Profile has not been created.")
    if st.button('Create Your Profile', 
                 type='primary', 
                 use_container_width=True):
        st.switch_page('pages/16_Mentor_Create_Profile.py')  
else:

    mentor_data = st.session_state["mentor_data"]

    st.subheader("Your Profile Details")
    st.text(f"{mentor_data['name']}")
    st.text(f"{mentor_data['email']}")
    st.text(f"Major: {mentor_data['major']}")

    if mentor_data["isWorking"] == True:
        st.text(f"Currently Works as: {mentor_data['currentPosition']}")

    if mentor_data["minor"]:
        st.text(f"Minor: {mentor_data['minor']}")
    st.text(f"College: {mentor_data['college']}")

    if mentor_data["profile_pic"]:
        img = Image.open(mentor_data["profile_pic"])
        st.image(img, caption="Profile Picture", use_column_width=True)
    else:
        st.warning("No profile picture uploaded.")


    if st.button('Edit Profile', 
                 type='primary', 
                 use_container_width=True):
        st.switch_page('pages/17_Mentor_Edit_Profile.py') 
