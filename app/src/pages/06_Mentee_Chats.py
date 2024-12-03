import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
import requests
import random
import time
from modules.nav import SideBarLinks

SideBarLinks()

add_logo("assets/logo.svg", height=400)

st.title("Chat with your mentor?")

# write routes to set these vals to the max menteeID and mentorID, consider limiting behavior to those two tables only
senderId = 2
recipientId = 1

def fetch_chats(senderId, recipientId):
  try:
        response = requests.get(f"http://web-api:4000/o/Chats/{senderId}/{recipientId}") 
        if response.status_code == 200:
            st.write("chats returned")
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

# if prompt := st.chat_input("What is up?"):
#   # Display user message in chat message container
#   with st.chat_message("user"):
#     st.markdown(prompt)
  
#   # Add user message to chat history
#   st.session_state.messages.append({"role": "user", "content": prompt})

#   response = f"Echo: {prompt}"

#   # Display assistant response in chat message container
#   with st.chat_message("assistant"):
#     # st.markdown(response)
#     response = st.write_stream(response_generator())

#   # Add assistant response to chat history
#   st.session_state.messages.append({"role": "assistant", "content": response})

