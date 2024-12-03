import logging
import streamlit as st
from streamlit_extras.app_logo import add_logo
import random
import time
from modules.nav import SideBarLinks

# Logging setup
logger = logging.getLogger(__name__)

# Add Sidebar Links
SideBarLinks()

# Add Logo
add_logo("assets/logo.png", height=400)

# Page title
st.title("Mentee Chat Dashboard 💬")

# Page description
st.markdown("""
Welcome to your mentee chat dashboard! Use this space to ask questions, seek guidance, and connect with your mentor or peers in your field of interest.
""")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "suggested_mentors" not in st.session_state:
    st.session_state.suggested_mentors = [
        {"name": "Sarah Star", "field": "Finance", "company": "McKinsey", "tags": ["Finance", "Investment"]},
        {"name": "Alan Turing", "field": "AI Research", "company": "Google", "tags": ["AI", "Research", "CS"]}
    ]
if "job_suggestions" not in st.session_state:
    st.session_state.job_suggestions = [
        {"title": "Software Engineering Co-op", "company": "Google", "location": "Remote", "tags": ["CS", "AI"]},
        {"title": "Data Analyst Internship", "company": "Meta", "location": "New York", "tags": ["Math", "Analytics"]}
    ]

# Suggested Mentors Section
st.subheader("Suggested Mentors")
for mentor in st.session_state.suggested_mentors:
    st.markdown(f"**Name:** {mentor['name']}")
    st.markdown(f"**Field:** {mentor['field']}")
    st.markdown(f"**Company:** {mentor['company']}")
    st.markdown(f"**Tags:** {', '.join(mentor['tags'])}")
    st.markdown("---")

# Suggested Jobs Section
st.subheader("Job Opportunities")
for job in st.session_state.job_suggestions:
    st.markdown(f"**Title:** {job['title']}")
    st.markdown(f"**Company:** {job['company']}")
    st.markdown(f"**Location:** {job['location']}")
    st.markdown(f"**Tags:** {', '.join(job['tags'])}")
    st.markdown("---")

# File Upload for Resume
st.subheader("Upload Your Resume")
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type="pdf")
if uploaded_file:
    st.success("Resume uploaded successfully!")
    st.write(f"Uploaded: {uploaded_file.name}")

# Response Generator for Chat
def response_generator():
    responses = [
        "That's a great question! Let me help you with that.",
        "Have you considered applying to internships in AI research?",
        "Networking is key! Reach out to alumni in your desired field."
    ]
    response = random.choice(responses)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# Display Chat History
st.subheader("Chat History")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle User Input
if prompt := st.chat_input("Ask your mentor or peers a question..."):
    # Display user's message
    with st.chat_message("user"):
        st.markdown(f"**You:** {prompt}")
        st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate bot response
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
        st.session_state.messages.append({"role": "assistant", "content": response})