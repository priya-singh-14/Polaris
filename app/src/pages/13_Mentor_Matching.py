import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests
import os
from PIL import Image, ImageDraw


SideBarLinks()


directory = "assets/"
def fetch_mentees(mentor_id):
    response = requests.get(f"http://web-api:4000/u/MentorMentees/{mentor_id}", params={"mentor_id": mentor_id})
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: Please Build Profile First{response.json().get('error')}")
        return []
    
def fetch_mentor():
    response = requests.get("http://web-api:4000/u/mostRecentMentor")
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: {response.json().get('error')}")
        return []
    

def fetch_jobs(mentee_id):
    response = requests.get(f"http://web-api:4000/c/MatchingJobs/{mentee_id}", params={"mentee_id": mentee_id})
    
    if response.status_code == 200:
            return response.json()
    else:
        st.error(f"Error fetching jobs: {response.status_code} - {response.text}")
        return []


mentorId = fetch_mentor().get("MAX(mentorId)")

if mentorId == 15 :
    mentorId = fetch_mentor().get("MAX(mentorId)")
    mentees = fetch_mentees(mentorId)

else :
    mentorId = fetch_mentor().get("MAX(mentorId)") + 1
    mentees = fetch_mentees(mentorId)

if mentees:
    mentee_names = [mentee['name'] for mentee in mentees] 
    selected_name = st.selectbox('Choose Mentee', mentee_names) 
    selected_mentee = next((mentee for mentee in mentees if mentee['name'] == selected_name), None)

    if selected_mentee:
            with st.container(border=True):
                if "assets/" not in selected_mentee["profilepic"]:
                    img_path = os.path.join(directory, selected_mentee["profilepic"])
                    img = Image.open(img_path)
                    width, height = img.size
                    min_side = min(width, height)
                    left = (width - min_side) / 2
                    top = (height - min_side) / 2
                    right = (width + min_side) / 2
                    bottom = (height + min_side) / 2
                    img = img.crop((left, top, right, bottom))
                    
                    mask = Image.new("L", (min_side, min_side), 0)
                    draw = ImageDraw.Draw(mask)
                    draw.ellipse((0, 0, min_side, min_side), fill=255)
                    
                    img = img.resize((140, 140)) 
                    circular_img = Image.new("RGBA", (140, 140), (0, 0, 0, 0))
                    circular_img.paste(img, (0, 0), mask.resize((140, 140)))
                    
                    st.image(circular_img)

                        # else:
                        #     st.write("No profile picture available.")
                elif "assets/" in selected_mentee["profilepic"]:
                    img_path = selected_mentee["profilepic"]
                    img = Image.open(img_path)
                    width, height = img.size
                    min_side = min(width, height)
                    left = (width - min_side) / 2
                    top = (height - min_side) / 2
                    right = (width + min_side) / 2
                    bottom = (height + min_side) / 2
                    img = img.crop((left, top, right, bottom))
                    
                    mask = Image.new("L", (min_side, min_side), 0)
                    draw = ImageDraw.Draw(mask)
                    draw.ellipse((0, 0, min_side, min_side), fill=255)
                    
                    img = img.resize((140, 140)) 
                    circular_img = Image.new("RGBA", (140, 140), (0, 0, 0, 0))
                    circular_img.paste(img, (0, 0), mask.resize((140, 140)))
                    
                    st.image(circular_img)

                        # else:
                        #     st.write("No profile picture available.")
                else:
                    st.write("No profile picture available.")

                st.write(f"**Name**: {selected_mentee['name']}")
                st.write(f"**Major**: {selected_mentee['major']}")
                st.write(f"**Bio**: {selected_mentee['bio']}")

                if selected_mentee['resume'] and selected_mentee['resume'].lower() != "none":
                    resume_path = os.path.join(directory, selected_mentee['resume'])
                    if os.path.exists(resume_path):
                        st.download_button(
                        label="Download Resume",
                        data=open(resume_path, "rb").read(),
                        file_name=f"{selected_mentee['name']}_Resume.pdf",
                        mime="application/pdf",
                    )
                else:
                    st.write("Resume not available.")
    st.markdown("---")
        
    if selected_mentee:
            st.subheader(f"Recommended Jobs for {selected_mentee['name']}")

            # st.write(selected_mentee['menteeId'])

            relevant_jobs = fetch_jobs(selected_mentee['menteeId'])
            if relevant_jobs:
                for idx, job in enumerate(relevant_jobs):
                    with st.container(border=True):
                        st.text(f"Role: {job['role']}")
                        st.text(f"Description: {job['jobDesc']}")
                        if st.button(f"Notify {selected_mentee['name']}?", key=idx):
                            recipientId = selected_mentee['menteeId']

                            chat_data = {
                            'senderId': mentorId,
                            'recipientId': recipientId,
                            'text': f"Hi, {selected_mentee['name']}, I think you should check out this opportunity: {job['jobDesc']}"
                            }

                            st.write(chat_data)

                            try:
                                create_user_response = requests.post('http://web-api:4000/o/createNewChat', json=chat_data)
                                if create_user_response.status_code == 200:
                                    st.success('Notified!')
                                
                                else:
                                    st.error("Error creating user profile. Please try again later.")
                            except requests.exceptions.RequestException as e:
                                        st.error(f"Error connecting to server: {str(e)}")


    else :
                        st.text("No Matching Jobs at This Time")             



else:
    st.warning("No mentees found.")
    st.write('')
    st.write('')

    if st.button('Find More Mentees', 
                type='primary',
                use_container_width=True):
        st.switch_page('pages/15_Mentor_Find_Mentees.py')


