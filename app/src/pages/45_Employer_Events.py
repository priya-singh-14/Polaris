import logging
import requests
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.subheader(f"Welcome to Your Event Management Dashboard, {st.session_state['first_name']}.")
st.write('')
st.write('')

empId = 1
def get_pending_invites(empId):

    try:
        response = requests.get(f"http://web-api:4000/c/PendingEvents/{empId}") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving invites: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    
    return None

def get_confirmed_events(empId):

    try:
        response = requests.get(f"http://web-api:4000/c/Events/{empId}") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving invites: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    
    return None

pending_invites = get_pending_invites(empId)
confirmed_events = get_confirmed_events(empId)

if pending_invites:
    st.write("You have pending invites:")
    
    for invite in pending_invites:
        with st.container(border=True) :
            st.write(f"{invite['name']} has invited you to speak at {invite['industry']} on {invite['when']}")
            if st.button("Accept Invite") :
                    event_data = {
                        "inviteAccepted": True
                }
                    try:
                        update_event = requests.put('http://web-api:4000/c/updateEvent', json=event_data)

                        if update_event.status_code == 200:
                            st.success("Invite Accepted!")
                        else:
                            st.error("Error accepting invite. Please try again later.")
                            
                    except requests.exceptions.RequestException as e:
                            st.error(f"Error connecting to server: {str(e)}")
            if st.button("Decline Invite", type='primary') :
                    event_data = {
                            "eventId": invite['eventId']
                    }
                    
                    try:
                        update_event = requests.delete('http://web-api:4000/c/DeleteEvent', json=event_data)

                        if update_event.status_code == 200:
                            st.success("Invite Declined!")
                        else:
                            st.error("Error declining invite. Please try again later.")
                            
                    except requests.exceptions.RequestException as e:
                            st.error(f"Error connecting to server: {str(e)}")
else :
     st.info("You Have No Pending Invites At The Moment")

st.markdown('---')


st.subheader("Your Upcoming Events:")
if confirmed_events:
    st.write("You have pending invites:")
    for event in confirmed_events:
        with st.container(border=True) :
            st.write(f"{event['industry']} Event on {event['when']}")
            if st.button("Cancel Event", type='primary', key=event['eventId']) :
                            event_data = {
                                    "eventId": event['eventId']
                            }
                            
                            try:
                                update_event = requests.delete('http://web-api:4000/c/DeleteEvent', json=event_data)

                                if update_event.status_code == 200:
                                    st.success("Event Canceled.")
                                else:
                                    st.error("Error declining invite. Please try again later.")
                                    
                            except requests.exceptions.RequestException as e:
                                    st.error(f"Error connecting to server: {str(e)}")