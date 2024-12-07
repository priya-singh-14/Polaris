import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
import requests
from modules.nav import SideBarLinks


SideBarLinks()

add_logo("assets/logo.svg", height=400)
st.title("Chat With Your Mentee")


# st.write(st.session_state['recipientId'])
# write routes to set these vals to the max menteeID and mentorID, consider limiting behavior to those two tables only
mentorId = 28
recipientId = st.session_state['recipientId']

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
  
chat_history = fetch_chats(mentorId, recipientId)

for chat in chat_history:
    senderId = chat['senderId']
    role = "user" if mentorId == senderId else "assistant"
    with st.chat_message(role):
        st.markdown(chat["text"])

# st.write(chat_history)

if chat := st.chat_input("Type Here"):
  with st.chat_message("user"):
    st.markdown(chat)
  
  chat_data = {
     "senderId" : mentorId,
     "recipientId" : recipientId,
     "text" : chat,
  }

  # st.write(chat_data)

  try:
            create_new_chat = requests.post('http://web-api:4000/o/createNewChat', json=chat_data)
            if create_new_chat.status_code == 200:
                st.info("Chat Sent")
            else:
                st.error("Error sending Chat. Please try again later.")

  except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")


