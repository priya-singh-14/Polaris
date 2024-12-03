import logging
import requests
import streamlit as st
from streamlit import session_state as ss
from modules.nav import SideBarLinks
from pathlib import Path
import base64
from PIL import Image

# Setup logging
logger = logging.getLogger(__name__)

# Configure Streamlit page
st.set_page_config(layout='wide')

# Display appropriate sidebar links
SideBarLinks()

# Initialize session state variables
if 'pdf_ref' not in ss:
    ss.pdf_ref = None

# Set up backend URL
FLASK_BACKEND = "http://api:4000"

# Fetch mentees data
try:
    response = requests.get(f"{FLASK_BACKEND}/o/Mentees", timeout=10)
    response.raise_for_status()  # Raise exception for HTTP errors
    results = response.json()
except requests.exceptions.RequestException as e:
    st.error(f"Failed to fetch data: {e}")
    st.stop()  # Stop execution if API fails

# Display mentees in card layout
st.title(f"Explore Candidates, {ss.get('first_name', 'User')}.")

for mentee in results:
    response = requests.get(f"{FLASK_BACKEND}/o/viewMenteeProfile/{mentee['menteeId']}", timeout=10)
    response.raise_for_status()  # Raise exception for HTTP errors
    mentee_info = response.json()
    # Display mentee details

    # Load the JPG image
    image_path = f"/appcode/assets/{mentee_info[0]['profilepic']}" 
    image = Image.open(image_path)
    st.image(image, width=700)

    st.subheader(f"Name: {mentee_info[0]['name']}")
    st.text(f"Major: {mentee_info[0]['major']} Minor: {mentee_info[0]['minor']}")
    st.text(f"Bio: {mentee_info[0]['bio']}")
    st.text(f"Email: {mentee_info[0]['email']}")

    file_name = mentee['resume'] 
    pdf_path = Path(f"/appcode/assets/{file_name}")

# Check if the file exists
    if pdf_path.exists():
        # Read PDF data and encode it properly
        with open(pdf_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
            base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
        
        # Render the PDF with an iframe
        pdf_data_url = f"data:application/pdf;base64,{base64_pdf}"
        st.markdown(
            f'<iframe src="{pdf_data_url}" width="700" height="500"></iframe>',
            unsafe_allow_html=True,
        )
    else:
        st.error(f"File not found: {pdf_path}")

    st.markdown("---")  # Divider for better readability