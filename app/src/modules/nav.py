# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ Mentee ------------------------
def MenteeHomeNav():
    st.sidebar.page_link("00_Mentee_Home.py", label="Home", icon="🏠")



def MenteeProfileNav():
    st.sidebar.page_link("01_Mentee_Profile.py", label="Profile", icon="📒")

 #### ------------------------ Mentor ------------------------
def MentorHomeNav():
    st.sidebar.page_link("10_Mentor_Home.py", label="Home", icon="🏠")



def MentorProfileNav():
    st.sidebar.page_link("11_Mentor_Profile.py", label="Profile", icon="📒")

 #### ------------------------ Employer ------------------------
def EmployerHomeNav():
    st.sidebar.page_link("40_Employer_Home.py", label="Home", icon="🏠")




#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")





#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon="🖥️")
    st.sidebar.page_link(
        "pages/21_ML_Model_Mgmt.py", label="ML Model Management", icon="🏢"
    )


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.svg", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:
        

        # Show appropriate pages if you are a mentee.
        if st.session_state["role"] == "mentee":
            MenteeHomeNav()
            MenteeProfileNav()



        # If the user role is usaid worker, show the Api Testing page
        if st.session_state["role"] == "mentor":
            MentorHomeNav()
            MentorProfileNav()

        # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "administrator":
            AdminPageNav()

        if st.session_state["role"] == "employer":
            MentorHomeNav()


    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
