### Mentor and Mentee Management
### View mentors and mentees and add/drop if needed
### user stories 4, 5
import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
from PIL import Image
import os

st.set_page_config(layout = 'wide')

SideBarLinks()

directory = 'assets/'


def view_mentors():

    try:
        response = requests.get(f"http://web-api:4000/o/viewMentorList") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving list: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    return None
mentors = view_mentors()



def view_mentees():

    try:
        response = requests.get(f"http://web-api:4000/o/viewMentorList") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving list: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    return None

mentees = view_mentees()

def delete_mentor(mentorId):
    try:
        response = requests.delete(f"http://web-api:4000/o/delete_mentor/{mentorId}")
        if response.status_code == 200:
            st.success("Mentor successfully removed!")
            st.experimental_rerun()  # Refresh the page to update the list
        else:
            st.error(f"Error deleting mentor: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")

def delete_mentee(menteeId):
    try:
        response = requests.delete(f"http://web-api:4000/o/delete_mentee/{menteeId}")
        if response.status_code == 200:
            st.success("Mentor successfully removed!")
            st.experimental_rerun()  # Refresh the page to update the list
        else:
            st.error(f"Error deleting mentor: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")

# used code from pg 12_Mentor_Network
if mentors:
    st.title('Active Mentors')
    for idx, mentor in enumerate(mentors):
        with st.container(border=True):
            img_path = os.path.join(directory, mentors[0]["profilepic"])
            if os.path.exists(img_path):
                img = Image.open(img_path)
                st.image(img, width=200)
            else:
                st.write("No profile picture available.")

            st.write(f"**Name**: {mentors['name']}")
            st.write(f"**Major**: {mentors['major']}")
            st.write(f"**Bio**: {mentors['bio']}")

            if mentors['resume'] and mentors['resume'].lower() != "none":
                resume_path = os.path.join(directory, mentors['resume'])
                if os.path.exists(resume_path):
                    st.download_button(
                    label="Download Resume",
                    data=open(resume_path, "rb").read(),
                    file_name=f"{mentors['name']}_Resume.pdf",
                    mime="application/pdf",
                    key=f"resume_{idx}" 
                )
            else:
                st.write("Resume not available.")

            if st.button(f"Delete {mentor['name']}", key=f"delete_mentor_{idx}"):
                delete_mentor(mentor['id'])
else:
    st.write("No mentors found.")


# code from page 12_Mentor_Network
if mentees:
    st.write('')
    st.title('Active Mentees')
    for idx, mentee in enumerate(mentees):
        with st.container(border=True):
            img_path = os.path.join(directory, mentee[0]["profilepic"])
            if os.path.exists(img_path):
                img = Image.open(img_path)
                st.image(img, width=200)
            else:
                st.write("No profile picture available.")

            st.write(f"**Name**: {mentee['name']}")
            st.write(f"**Major**: {mentee['major']}")
            st.write(f"**Bio**: {mentee['bio']}")

            if mentee['resume'] and mentee['resume'].lower() != "none":
                resume_path = os.path.join(directory, mentee['resume'])
                if os.path.exists(resume_path):
                    st.download_button(
                    label="Download Resume",
                    data=open(resume_path, "rb").read(),
                    file_name=f"{mentee['name']}_Resume.pdf",
                    mime="application/pdf",
                    key=f"resume_{idx}" 
                )
            else:
                st.write("Resume not available.")

            if st.button(f"Delete {mentee['name']}", key=f"delete_mentee_{idx}"):
                delete_mentee(mentee['id'])
else:
    st.write("No mentees found.")
