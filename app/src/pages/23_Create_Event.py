## Create Events
## route not working yet

import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
import os

SideBarLinks()

directory = "assets/"

st.title('Schedule a Networking Event')

def fetch_employers():
    response = requests.get(f"http://web-api:4000/o/Employers")
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching employers")
        return []
    
employers = fetch_employers()

with st.form(key="create_event_form"):
    speakerId = st.selectbox("Employers", employers)
    speakerName = st.text_input("Speaker Name")
    industry = st.text_input("Industry")
    when = st.date_input("When")

    submit_button = st.form_submit_button(label="Submit")


if submit_button:
     if not speakerId: 
         st.error("Speaker ID is required.")
     elif not speakerName:
        st.error("Speaker name is required.")
     elif not industry:
        st.error("Industry is required.")
     elif not when:
        st.error("Day of event is required.")
     else:
        generate_eventid_response = requests.get('http://web-api:4000/o/createEvent')
        if generate_eventid_response.status_code == 200:
                new_eventId = generate_eventid_response.json().get("new_eventId")
                st.info(f"Generated eventId: {new_eventId}")
                
        else:
                st.error("Error generating eventID. Please try again later.")

        event_data = {
            "eventId": new_eventId,
            "speakerId": speakerId, 
            "speakerName": speakerName,
            "industry": industry,
            "when": when
        }

        st.session_state["event_scheduled"] = True
        
        try:
            create_user_response = requests.post('http://web-api:4000/o/createEvent', json=event_data)
             
            if create_user_response.status_code == 200:
                st.info("View Event Details on the Previous Page")
                st.session_state['event_scheduled'] = True
            else:
                st.error("Error creating event. Please try again later.")

            create_mentee_response = requests.post('http://web-api:4000/o/createEvent', json=event_data)

            if create_mentee_response.status_code == 200:
                st.success("Event successfully scheduled!")
                st.session_state['event_scheduled'] = True
            else:
                st.error("Error creating event. Please try again later.")
                
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")