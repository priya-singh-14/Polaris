import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
import requests
from modules.nav import SideBarLinks


SideBarLinks()

add_logo("assets/logo.svg", height=400)

st.title("Chat With Your Mentor")


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
menteeId = fetch_mentee().get("MAX(menteeId)")
recipientId = fetch_matched_mentor(menteeId)

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

chat_history = fetch_chats(menteeId, recipientId)

if chat_history is not None:
  for chat in chat_history:
      senderId = chat['senderId']
      role = "user" if menteeId == senderId else "assistant"
  with st.chat_message(role):
       st.markdown(chat["text"])

else :
    st.warning("You Don't Have a Mentor to Chat with Yet")

# st.write(chat_history)

if chat := st.chat_input("Type Here"):
  with st.chat_message("user"):
    st.markdown(chat)
  
  chat_data = {
     "senderId" : menteeId,
     "recipientId" : recipientId,
     "text" : chat,
  }

  # st.write(chat_data)

  try:
            create_new_chat = requests.post('http://web-api:4000/o/createNewChat', json=chat_data)
            if create_new_chat.status_code == 200:
                st.info("View Profile Details on the Previous Page")
            else:
                st.error("Error creating user profile. Please try again later.")

  except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")


