import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()
# Graphic

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
        background: rgba(255, 255, 255, 0.8);
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        z-index: 2;
    } 

    .centered-card h1 {
        font-size: 2.8em;
        font-family: monospace;
        margin-bottom: 20px;
    }

    .centered-card p {
        font-size: 0.9rem;
        margin-bottom: 30px;
        color: #555;
    }

    .centered-card ul {
        margin-bottom: 30px;
        color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="parent-container">
    <div class="centered-card">
        <h1>You Just Found Your North Star.</h1>

<h5>Orbit Polaris is a dynamic networking platform designed to guide Northeastern students toward career success through peer mentorship.</h5>
<hr/>

<h3>What is Polaris?</h3>
<p>Like the North Star, Polaris provides direction and support, helping students navigate their career journeys with confidence. This data-driven app is essential for young professionals looking to build their networks early and develop strong career habits within the Northeastern Student Network.</p>

<h3>Why Polaris Stands Out</h3>
<p>Unlike platforms like LinkedIn or Northeastern MentorHub, Polaris is tailored specifically for the Northeastern academic community. We focus on helping students enhance their communication skills while engaging in experiential learning.</p>

<h3>Key Features</h3>
<ul>
  <li>Data-driven mentor-mentee pairing based on major, career interests, organizations, academic standing, and materials like resumes.</li>
  <li>Eliminates challenges like cold-messaging, incompatible relationships, and barriers to industry entry.</li>
  <li>Built in job search and application functionality, and opportunities to find and attend networking events with employers.</li>
</ul>

<h5>With mentor-mentee relationship recommendations, detailed user profiles, and real-time communication, Orbit Polaris creates meaningful connections that foster professional growth for everyone.</h5>    
    """,
    unsafe_allow_html=True,
)

st.image("assets/about.png", use_container_width=True, width=50)

