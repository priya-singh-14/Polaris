import logging
import streamlit as st
<<<<<<< HEAD
from streamlit_extras.app_logo import add_logo
import random
import time
=======
>>>>>>> d57a791ad3d9a394c4b192a51f72866119542400
from modules.nav import SideBarLinks
import requests
from PIL import Image
import os

# Logging setup
logger = logging.getLogger(__name__)

# Add Sidebar Links
SideBarLinks()

<<<<<<< HEAD
# Add Logo
add_logo("assets/logo.png", height=400)

# Page title
st.title("Mentor's Chat Dashboard 📚")

# Page description
st.markdown("""
Welcome to your mentor dashboard! This page allows you to interact with your matched mentees, track their progress, and share resources to help them grow.
""")

# Initialize session state for messages and mentee details
if "messages" not in st.session_state:
    st.session_state.messages = []
if "matched_mentees" not in st.session_state:
    st.session_state.matched_mentees = [
        {"name": "Jane Doe", "major": "Finance", "goals": "Learn about investment strategies", "tags": ["Finance", "Investment"], "progress": "80%"},
        {"name": "John Smith", "major": "Economics", "goals": "Prepare for finance job interviews", "tags": ["Economics", "Interview Prep"], "progress": "50%"}
    ]

# Display matched mentees
st.subheader("Your Matched Mentees")
for mentee in st.session_state.matched_mentees:
    st.markdown(f"**Name:** {mentee['name']}")
    st.markdown(f"**Major:** {mentee['major']}")
    st.markdown(f"**Goals:** {mentee['goals']}")
    st.markdown(f"**Tags:** {', '.join(mentee['tags'])}")
    st.progress(int(mentee["progress"].strip('%')))
    st.markdown("---")

# Response generator for chat
def response_generator():
    responses = [
        "That sounds great! Let me know how I can help further.",
        "Thanks for the update! Have you considered these resources?",
        "Let’s discuss this in detail during our next session."
    ]
    response = random.choice(responses)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# Display chat history
st.subheader("Chat History")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Mentor-to-Mentee Interaction
if prompt := st.chat_input("Send a message to your mentee..."):
    # Display mentor's message
    with st.chat_message("mentor"):
        st.markdown(f"**You:** {prompt}")
        st.session_state.messages.append({"role": "mentor", "content": prompt})

    # Simulate mentee's response
    with st.chat_message("mentee"):
        response = st.write_stream(response_generator())
        st.session_state.messages.append({"role": "mentee", "content": response})

# Resource Sharing Section
st.subheader("Share Resources with Your Mentees")
uploaded_file = st.file_uploader("Upload a guide, article, or book recommendation (PDF only)", type="pdf")
if uploaded_file:
    st.success("Resource uploaded successfully!")
    st.write(f"Shared: {uploaded_file.name}")
=======
st.subheader(f"Which Mentee Would You Like To Chat With, {st.session_state['first_name']}.")

def fetch_mentees(mentor_id):
    response = requests.get("http://web-api:4000/o/MentorMentees/1", params={"mentor_id": mentor_id})
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: {response.json().get('error')}")
        return []

mentees = fetch_mentees(1)
directory = "assets/"

if mentees:
    for idx, mentee in enumerate(mentees):
        with st.container(border=True):
            img_path = os.path.join(directory, mentee["profilepic"])
            if os.path.exists(img_path):
                img = Image.open(img_path)
                st.image(img, width=100)
            else:
                st.write("No profile picture available.")

            st.write(f"{mentee['name']}")
            if st.button(f"Chat with {mentee['name']}", key=mentee['menteeId']):
                st.session_state['recipientId'] = mentee['menteeId']
                st.switch_page('pages/18_Mentor_Chat_With_Mentee.py')
else:
    st.write("No mentees found.")
>>>>>>> d57a791ad3d9a394c4b192a51f72866119542400
