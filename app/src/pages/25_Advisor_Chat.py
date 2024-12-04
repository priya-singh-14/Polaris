import logging
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import random
import time

# Logging setup
logger = logging.getLogger(__name__)

# Add Sidebar Links
SideBarLinks()

# Add Logo
add_logo("assets/logo.png", height=400)

# Page title
st.title("Alumni Chat Dashboard 🎓")

# Page description
st.markdown("""
Welcome to your Alumni Chat Dashboard! Use this space to connect with mentees, mentors, and other alumni, share resources, and coordinate events for networking and guidance.
""")

# Initialize session state for chat history and user lists
if "messages" not in st.session_state:
    st.session_state.messages = []
if "connected_users" not in st.session_state:
    st.session_state.connected_users = [
        {"name": "Tyler Dipper", "role": "Mentee", "tags": ["CS", "Math", "Co-op"]},
        {"name": "Sarah Star", "role": "Mentor", "tags": ["Finance", "Investment", "Alumni"]}
    ]
if "events" not in st.session_state:
    st.session_state.events = [
        {"title": "Networking Night", "date": "2024-12-10", "description": "Connect with peers in Finance and Tech."},
        {"title": "Career Growth Workshop", "date": "2024-12-15", "description": "Learn strategies to advance your career."}
    ]

# Display connected users (mentors and mentees)
st.subheader("Connected Users")
for user in st.session_state.connected_users:
    st.markdown(f"**Name:** {user['name']}")
    st.markdown(f"**Role:** {user['role']}")
    st.markdown(f"**Tags:** {', '.join(user['tags'])}")
    st.markdown("---")

# Event Coordination Section
st.subheader("Upcoming Events")
for event in st.session_state.events:
    st.markdown(f"**Title:** {event['title']}")
    st.markdown(f"**Date:** {event['date']}")
    st.markdown(f"**Description:** {event['description']}")
    st.markdown("---")

# Add a new event
st.subheader("Plan a New Event")
event_title = st.text_input("Event Title")
event_date = st.date_input("Event Date")
event_description = st.text_area("Event Description")

if st.button("Add Event"):
    if event_title and event_description:
        st.session_state.events.append({"title": event_title, "date": str(event_date), "description": event_description})
        st.success(f"Event '{event_title}' added successfully!")
    else:
        st.error("Please fill in all fields to add an event.")

# Response generator for chat
def response_generator():
    responses = [
        "Thank you for sharing! Let's coordinate on that.",
        "I'll follow up with the mentees about this.",
        "Great point! Let’s add that to our next event."
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

# Alumni-to-Mentee/Mentor Interaction
if prompt := st.chat_input("Send a message to your mentees or mentors..."):
    # Display alumni's message
    with st.chat_message("alumni"):
        st.markdown(f"**You:** {prompt}")
        st.session_state.messages.append({"role": "alumni", "content": prompt})

    # Simulate a response from a mentee or mentor
    with st.chat_message("user"):
        response = st.write_stream(response_generator())
        st.session_state.messages.append({"role": "user", "content": response})

# Resource Sharing Section
st.subheader("Share Resources")
uploaded_file = st.file_uploader("Upload a resource (PDF only)", type="pdf")
if uploaded_file:
    st.success("Resource uploaded successfully!")
    st.write(f"Shared: {uploaded_file.name}")