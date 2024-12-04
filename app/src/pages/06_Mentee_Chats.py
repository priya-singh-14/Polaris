import logging
import streamlit as st
from streamlit_extras.app_logo import add_logo
import requests
from modules.nav import SideBarLinks

# Logging setup
logger = logging.getLogger(__name__)

# Add Sidebar Links
SideBarLinks()

# Add Logo
add_logo("assets/logo.png", height=400)

# Page title
st.title("Mentee Chat Dashboard 💬")


def fetch_mentee():
    response = requests.get("http://web-api:4000/o/mostRecentMentee")
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: {response.json().get('error')}")
        return []
    
def fetch_matched_mentor(menteeId):
    response = requests.get(f"http://web-api:4000/o/Match/{menteeId}")
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: {response.json().get('error')}")
        return []

# write routes to set these vals to the max menteeID and mentorID, consider limiting behavior to those two tables only
menteeId = 4
# recipientId = fetch_matched_mentor(menteeId)

if len(fetch_matched_mentor(menteeId)) == 0 :
    recipientId = 0
else :
    recipientId = fetch_matched_mentor(menteeId)[0].get("mentorId")

st.write(recipientId)

def fetch_chats(senderId, recipientId):
  try:
        response = requests.get(f"http://web-api:4000/o/Chats/{senderId}/{recipientId}") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving chats: {response.json().get('error', 'Unknown error')}")
  except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
        return None
  
if "messages" not in st.session_state:
   st.session_state.messages = []

# st.write(recipientId)
   
if recipientId is 0:
    st.warning("You Don't Have a Mentor to Chat with Yet")

else :
    chat_history = fetch_chats(menteeId, recipientId)

    for chat in chat_history:
        senderId = chat['senderId']
        role = "user" if menteeId == senderId else "assistant"
    with st.chat_message(role):
            st.markdown(chat["text"])

# Handle User Input
if prompt := st.chat_input("Ask your mentor or peers a question..."):
    # Display user's message
    with st.chat_message("user"):
        st.markdown(f"**You:** {prompt}")
        st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate bot response
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
        st.session_state.messages.append({"role": "assistant", "content": response})