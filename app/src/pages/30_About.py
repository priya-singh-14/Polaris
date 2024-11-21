import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# You just found Your North Star.")

star_img = '''
<style>
.stApp {
    background-image: url(https://studyfinds.org/wp-content/uploads/2024/08/Polaris-North-Star-1200x808.jpg);
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

button:hover {
    transform: scale(1.1);
    transition: 0.2s;
}
</style>
'''

st.markdown (star_img, unsafe_allow_html=True)

st.markdown (
    """
    Orbit Polaris is a dynamic networking platform designed to guide Northeastern students toward career success by connecting them with student mentors and industry professionals based on their career-interests and experience. Like the North Star, Orbit Polaris provides direction and support, helping students navigate their career journeys with confidence. This data-driven app is important because it helps young professionals establish their network early, so they can develop better career habits under the guidance of the Northeastern Student Network. Unlike other platforms like LinkedIn or Northeastern MentorHub, Polaris is both confined to the Northeastern academic network, and aims to help students improve their communication skills as they delve into experiential learning. By storing data such as major, career interest, organizations, academic standing, and career materials like resumes and portfolios-- Polaris allows mentees to be paired with mentors that are tailored to their interests. Unlike other platforms that provide connections at face value, our data-driven networking tool eliminates pain points such as uncomfortable cold-messaging, incompatible mentor-mentee relationships, and the struggle that comes with breaking into an industry for the first time. The primary users are student mentees, student/alumni mentors, advisors/admins, and potential employers. With mentor-mentee relationship recommendations, detailed user profiles, and real-time communication, Orbit Polaris lights the way to meaningful mentor-mentee relationships and collective professional growth.

    """
        )
