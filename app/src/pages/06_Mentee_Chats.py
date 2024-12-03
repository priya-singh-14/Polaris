import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
import requests
import time
from modules.nav import SideBarLinks
from datetime import datetime, timezone

now_utc = datetime.now(timezone.utc)
formatted_datetime = now_utc.strftime("%a, %d %b %Y %H:%M:%S GMT")


SideBarLinks()

add_logo("assets/logo.svg", height=400)

st.title("Chat With Your Mentor")

# write routes to set these vals to the max menteeID and mentorID, consider limiting behavior to those two tables only
senderId = 1 
recipientId = 2

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
  
chat_history = fetch_chats(senderId, recipientId)

for chat in chat_history:
   st.markdown(chat["text"])

if chat := st.chat_input("Type Here"):
  with st.chat_message("user"):
    st.markdown(chat)
  
  chat_data = {
     "senderId" : senderId,
     "recipientId" : recipientId,
     "text" : chat,
     "timestamp": formatted_datetime
  }

  st.write(chat_data)

