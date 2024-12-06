### Mentor and Mentee Management
### View mentors and mentees and add/drop if needed
### user stories 4, 5
import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
from PIL import Image, ImageDraw
import os

st.set_page_config(layout = 'wide')

SideBarLinks()

directory = 'assets/'
default = 'assets/default.jpg'

def view_mentors():

    try:
        response = requests.get(f"http://web-api:4000/u/viewMentorList") 
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
        response = requests.get(f"http://web-api:4000/u/AllMentees") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving list: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    return None

mentees = view_mentees()
st.write(mentees)
# used code from pg 12_Mentor_Network
if mentors:
    st.title('Active Mentors')
    for idx, mentor in enumerate(mentors):
        with st.container(border=True):
            if mentor["profilepic"] and "assets/" not in mentor["profilepic"]:
                    img_path = os.path.join(directory, mentor["profilepic"])
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
            elif mentor["profilepic"] and "assets/" in mentor["profilepic"]:
                    img_path = mentor["profilepic"]
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
                    img = Image.open(default) 
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

            st.write(f"**Name**: {mentor['name']}")
            st.write(f"**Major**: {mentor['major']}")
            mentorId = mentor['mentorId']

            if st.button(f"Delete {mentor['name']}", key=f"delete_mentor_{idx}"):
                
                mentor_data = {
                    'mentorId' : mentorId
                }

                try:
                        response = requests.delete(f"http://web-api:4000/u/DeleteMentor", json=mentor_data) 
                        if response.status_code == 200:
                            st.info("Mentor Removed")
                        else:
                            st.error(f"Error withdrawing Applicaton: {response.json().get('error', 'Unknown error')}")
                except requests.exceptions.RequestException as e:
                        st.error(f"Error connecting to server: {str(e)}")
else:
    st.write("No mentors found.")


# code from page 12_Mentor_Network
if mentees:
    st.write('')
    st.title('Active Mentees')
    for idx, mentee in enumerate(mentees):
        with st.container(border=True):
            if mentee["profilepic"] and "assets/" not in mentee["profilepic"]:
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
            else:
                    img = Image.open(default) 
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

            st.write(f"**Name**: {mentee['name']}")
            st.write(f"**Major**: {mentee['major']}")
            st.write(f"**Bio**: {mentee['bio']}")
            
            menteeId = mentee['menteeId']

            if mentee['resume'] and mentee['resume'].lower() != "none" and "assets/" not in mentee["resume"]:
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

            if st.button(f"Delete {mentee['name']}", key=f"delete_mentee_{idx}"):
                mentee_data = {
                    'menteeId' : menteeId
                }

                try:
                        response = requests.delete(f"http://web-api:4000/u/DeleteMentee", json=mentee_data) 
                        if response.status_code == 200:
                            st.info("Mentee Removed")
                        else:
                            st.error(f"Error withdrawing Applicaton: {response.json().get('error', 'Unknown error')}")
                except requests.exceptions.RequestException as e:
                        st.error(f"Error connecting to server: {str(e)}")
else:
    st.write("No mentees found.")
