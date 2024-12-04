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
    response = requests.get(f"http://web-api:4000/o/MentorMentees/{mentor_id}", params={"mentor_id": mentor_id})
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: Please Build Profile First{response.json().get('error')}")
        return []
    
def fetch_mentor():
    response = requests.get("http://web-api:4000/o/mostRecentMentor")
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: {response.json().get('error')}")
        return []
    
mentorId = fetch_mentor().get("MAX(mentorId)")

if mentorId == 15 :
    mentorId = fetch_mentor().get("MAX(mentorId)")
    mentees = fetch_mentees(mentorId)

else :
    mentorId = 2 
    # fetch_mentor().get("MAX(mentorId)") + 1
    mentees = fetch_mentees(mentorId)

if mentees:
    mentee_names = [mentee['name'] for mentee in mentees] 
    selected_name = st.selectbox('Choose Mentee', mentee_names) 
    selected_mentee = next((mentee for mentee in mentees if mentee['name'] == selected_name), None)

    if selected_mentee:
            with st.container(border=True):
                img_path = os.path.join(directory, selected_mentee["profilepic"])
                if img_path!= "assets/":
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

    st.subheader(f"Recommended Jobs for {selected_mentee['name']}")