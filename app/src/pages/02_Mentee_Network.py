import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests

SideBarLinks()


st.title("Event Calendar")

selected_date = st.date_input("Select a date (leave blank for all events):", value=None)


def get_all_events() :
    try:
            response = requests.get("http://web-api:4000/o/Events") 
            if response.status_code == 200:
                return response.json()
            else:
                st.error(f"Error retrieving jobs: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")
    return None

def get_event(date) :
    try:
            response = requests.get(f"http://web-api:4000/o/Events/{date}") 
            if response.status_code == 200:
                return response.json()
            else:
                st.error(f"Error retrieving jobs: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")
    return None

if selected_date is not None:
    events = get_event(selected_date.strftime("%Y-%m-%d"))
else:
    events = get_all_events()

if events:
     for event in events:
            with st.container(border=True):
                st.write(f"**Industry:** {event['industry']}")
                st.write(f"**Speaker:** {event['speakerName']}")
                st.write(f"**Date:** {event['when']}")
else:
    st.write("No events found.")