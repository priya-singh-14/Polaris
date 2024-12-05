import logging
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests

# Logging setup
logger = logging.getLogger(__name__)

# Add Sidebar Links
SideBarLinks()

# Add Logo
add_logo("assets/logo.png", height=400)

# Page title
st.title("Advisor Chat Dashboard 🎓")

# Page description
st.markdown("""
Welcome to your Advisor Chat Dashboard! Use this space monitor messages between your mentors and their mentees.
""")


advisorId = 1

def get_all_matches(advisorId) :
    response = requests.get(f"http://web-api:4000/o/AdvisorMatch/{advisorId}",)
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: Please Build Profile First{response.json().get('error')}")
        return []
    
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

advisorMatches = get_all_matches(advisorId)

match_to_edit = st.selectbox("Select a match to view messages", options=range(len(advisorMatches)), format_func=lambda i: f"{advisorMatches[i]['name']} ↔ {advisorMatches[i]['MenteeUser.name']}")

if match_to_edit is not None:
    selected_match = advisorMatches[match_to_edit]

    mentorId = selected_match['Mentor.mentorId']
    menteeId = selected_match['Mentee.menteeId']

    chat_history = fetch_chats(mentorId, menteeId)
    
    if chat_history :
        with st.container(border=True) :
            for chat in chat_history:
                senderId = chat['senderId']
                role = "user" if mentorId == senderId else "assistant"
                with st.chat_message(role):
                    st.markdown(chat["text"])
    else :
         st.info("No Chats Found")
else :
    st.info("Match Not Found")