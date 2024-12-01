import logging
import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

SideBarLinks()

if "mentee_data" not in st.session_state:
    st.session_state["mentee_data"] = None  

st.title("Your Profile")

if st.session_state["mentee_data"] is None:
    st.warning("Profile has not been created.")
    if st.button('Create Your Profile', 
                 type='primary', 
                 use_container_width=True):
        st.switch_page('pages/07_Mentee_Create_Profile.py')  
else:

    mentee_data = st.session_state["mentee_data"]

    st.subheader("Your Profile Details")
    st.text(f"{mentee_data['name']}")
    st.text(f"{mentee_data['email']}")
    st.text(f"Major: {mentee_data['major']}")
    if mentee_data["minor"]:
        st.text(f"Minor: {mentee_data['minor']}")
    st.text(f"College: {mentee_data['college']}")

    if mentee_data["profile_pic"]:
        img = Image.open(mentee_data["profile_pic"])
        st.image(img, caption="Profile Picture", use_column_width=True)
    else:
        st.warning("No profile picture uploaded.")


    if st.button('Edit Profile', 
                 type='primary', 
                 use_container_width=True):
        st.switch_page('pages/08_Mentee_Edit_Profile.py') 
