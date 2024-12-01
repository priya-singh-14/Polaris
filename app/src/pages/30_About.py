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
        background: rgba(255, 255, 255, 0.7);
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        z-index: 2;
    } 

    .centered-card h1 {
        font-size: 2.9em;
        font-family: monospace;
        margin-bottom: 0px;
    }

    .centered-card p {
        font-size: 0.9rem;
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
        <h1>You Just Found Your North Star</h1>
        <p>Orbit Polaris is a dynamic networking platform designed to guide Northeastern students toward career success by connecting them with student mentors and industry professionals based on their career-interests and experience. Like the North Star, Orbit Polaris provides direction and support, helping students navigate their career journeys with confidence. This data-driven app is important because it helps young professionals establish their network early, so they can develop better career habits under the guidance of the Northeastern Student Network. Unlike other platforms like LinkedIn or Northeastern MentorHub, Polaris is both confined to the Northeastern academic network, and aims to help students improve their communication skills as they delve into experiential learning. By storing data such as major, career interest, organizations, academic standing, and career materials like resumes and portfolios-- Polaris allows mentees to be paired with mentors that are tailored to their interests. Unlike other platforms that provide connections at face value, our data-driven networking tool eliminates pain points such as uncomfortable cold-messaging, incompatible mentor-mentee relationships, and the struggle that comes with breaking into an industry for the first time. The primary users are student mentees, student/alumni mentors, advisors/admins, and potential employers. With mentor-mentee relationship recommendations, detailed user profiles, and real-time communication, Orbit Polaris lights the way to meaningful mentor-mentee relationships and collective professional growth.
</p>
    """,
    unsafe_allow_html=True,
)

st.image("assets/about.jpg", use_container_width=True, width=50)

