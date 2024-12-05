import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests
import os
from PIL import Image, ImageDraw

SideBarLinks()

st.subheader(f"Here are some potential mentees, {st.session_state['first_name']}.")

# session state these values somewhere
mentorId = 15
college = "Khoury"
major = "Computer Science"
minor = "Finance"
directory = "assets/"

option = st.selectbox('Explore Mentees?', ('All', 'Related to You'))

def fetch_all_mentees():
     try:
        response = requests.get(f"http://web-api:4000/o/AllMentees") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving profile: {response.json().get('error', 'Unknown error')}")
     except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    
     return None
     

def fetch_relevant_mentees(college, major, minor):
    try:
        response = requests.get(f"http://web-api:4000/o/Mentees/{college}/{major}/{minor}") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving profile: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    return None


if option == "All" :
     mentees = fetch_all_mentees()
     total = len(mentees)
     st.info(f"Here are all {total} registered mentees")

elif option == "Related to You" :
    mentees = fetch_relevant_mentees(college, major, minor)
    total = len(mentees)
    st.info(f"Here are all {total} mentees that share your major, minor, or college")

else :   
    mentees = []

if mentees:
    for idx, mentee in enumerate(mentees):
        with st.container(border=True):
            if "assets/" not in mentee["profilepic"]:
                    img_path = os.path.join(directory, mentee["profilepic"])
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
            elif "assets/" in mentee["profilepic"]:
                    img_path = mentee["profilepic"]
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

            
                
            st.write(f"**Name**: {mentee['name']}")
            st.write(f"**College**: {mentee['college']}")
            st.write(f"**Major**: {mentee['major']}")
            st.write(f"**Minor**: {mentee['minor']}")
            st.write(f"**Bio**: {mentee['bio']}")

            if "assets/" not in mentee["resume"] and mentee['resume'] and mentee['resume'].lower() != "none":
                    resume_path = os.path.join(directory, mentee['resume'])
                    if os.path.exists(resume_path):
                        st.download_button(
                        label="Download Resume",
                        data=open(resume_path, "rb").read(),
                        file_name=f"{mentee['name']}_Resume.pdf",
                        mime="application/pdf",
                        key=f"resume_{idx}" 
                    )
            elif "assets/" in mentee["resume"] and mentee['resume'] and mentee['resume'].lower() != "none":
                    resume_path = mentee['resume']
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

            if st.button(f"Add to Network", type='primary', key={mentee['name']}):

                    match_data = {
                    "menteeId": mentee['menteeId'],
                    "mentorId": mentorId,
                    }

                    try:
                            add_mentee = requests.post('http://web-api:4000/o/MatchMentees', json=match_data)
                
                            if add_mentee.status_code == 200:
                                st.success("Added to Network")
                            else:
                                st.error("Error adding mentee. Has your profile been completed?.")
                    except requests.exceptions.RequestException as e:
                        st.error(f"Error connecting to server: {str(e)}")
else:
    st.write("No mentees found.")