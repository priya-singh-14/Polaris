##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import streamlit as st
import logging
from modules.nav import SideBarLinks

logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(45deg, #FFEECC, #CCFFFF, #EECCFF);
        font-family: 'Helvetica', sans-serif;
    }

    .parent-container {
        position: relative;
        width: 100%;
        z-index: 1; /* Ensure parent container has a higher stacking context */
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: -50px;
    }

    .centered-card {
        margin: 35px;
        margin-top: 90px;
        position: absolute;
        background: rgba(255, 255, 255, 0.4);
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        z-index: 2; /* Ensures card appears above the graphic */
    } 

    .wide-card {
        margin-left: 35px;
        margin-right: 35px;
        width: 95%;
        height: 80px;
        margin-top: 120px;
        top: 300px;
        position: absolute;
        text-align: center;
        background: rgba(255, 255, 255, 0.4);
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        z-index: 2; /* Ensures card appears above the graphic */
     }

    .wide-card h2 {
        font-size: 1.4rem;
        font-family: monospace;
    }


    .centered-card h1 {
        font-size: 3.2em;
        font-family: monospace;
        margin-bottom: 0px;
    }

     .centered-card h2 {
        margin-top: -20px;
        font-size: 1.5rem;
        font-family: monospace;
        color: #595959;
    }

    .centered-card p {
        font-size: 1rem;
        margin-bottom: 30px;
        color: #555;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# Card content
st.markdown(
    """
    <div class="parent-container">
    <div class="centered-card">
        <h1>Polaris</h1>
        <h2>An Orbit Product</h2>
        <p>Welcome to Polaris, your guiding star as you navigate your early career and expanding network. Connect with mentors and mentees and explore job opportunities all in one place.</p>
    </div>
    <div class="wide-card">
        <h2>Who Would You Like To Explore As?</h2>
    </div>
      </div>
    """,
    unsafe_allow_html=True,
)

# Graphic
st.markdown('<div class="graphic">', unsafe_allow_html=True)
st.image("assets/star2.svg", use_container_width=True, width=50)


if st.button("Tyler, a Third Year Computer Science Mentee", 
            type='secondary', 
            use_container_width=True):
    # when user clicks the button, they are now considered authenticated
    st.session_state['authenticated'] = True
    # we set the role of the current user
    st.session_state['role'] = 'Mentee'
    # we add the first name of the user (so it can be displayed on 
    # subsequent pages). 
    st.session_state['first_name'] = 'Tyler'
    # finally, we ask streamlit to switch to another page, in this case, the 
    # landing page for this particular user type
    logger.info("Logging in as Mentee Persona")
    st.switch_page('pages/00_Mentee_Home.py')

if st.button('Sara, a Northeastern Alumni and Mentor, who works at McKinsey', 
            type='secondary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'Mentor'
    st.session_state['first_name'] = 'Sara'
    st.switch_page('pages/10_Mentor_Home.py')

if st.button('Billy, an Advisor at Northeastern', 
            type='secondary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'Administrator'
    st.session_state['first_name'] = 'Billy'
    st.switch_page('pages/20_Admin_Home.py')

if st.button('John, an Employer Looking to Fill Intern/Co-Op Roles', 
            type='secondary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'Employer'
    st.session_state['first_name'] = 'John'
    st.switch_page('pages/40_Employer_Home.py')