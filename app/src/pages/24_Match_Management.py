import streamlit as st
from streamlit_extras.app_logo import add_logo
import requests

from modules.nav import SideBarLinks

SideBarLinks()


# Add Logo
add_logo("assets/logo.png", height=400)

# Page title
st.title("Match Management Dashboard 🔗")

# Description
st.markdown("""
This page allows advisors to manage mentor-mentee matches effectively. You can view, add, edit, and remove matches to ensure the best connections.
""")

advisorId = 1

def get_all_matches(advisorId) :
    response = requests.get(f"http://web-api:4000/o/AdvisorMatch/{advisorId}",)
    
    if response.status_code == 200:
        return response.json() 
    else:
        st.error(f"Error fetching mentees: Please Build Profile First{response.json().get('error')}")
        return []


advisorMatches = get_all_matches(advisorId)
# st.write(advisorMatches)
# Display existing matches

st.subheader("Current Matches")
if advisorMatches :
    for idx, match in enumerate(advisorMatches):
        st.markdown(f"**Mentor:** {match['name']}")
        st.markdown(f"**Mentee:** {match['MenteeUser.name']}")
        match_data = {
             'menteeId' : match['Mentee.menteeId'],
             'mentorId' : match['Mentor.mentorId'],
        }
        if st.button(f"Remove Match #{idx + 1}", key=f"remove_{idx}"):
            try:
                response = requests.delete(f"http://web-api:4000/o/DeleteMatch", json=match_data) 
                if response.status_code == 200:
                        st.success("Match Deleted")
                else:
                        st.error(f"Error withdrawing Applicaton: {response.json().get('error', 'Unknown error')}")
            except requests.exceptions.RequestException as e:
                        st.error(f"Error connecting to server: {str(e)}")
        st.markdown("---")
else:
    st.write("No matches available.")


def fetch_all_mentees():
     try:
        response = requests.get(f"http://web-api:4000/o/AllMentees") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving profile: {response.json().get('error', 'Unknown error')}")
     except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    
     return None

def fetch_advisor_mentors(advisorId):
     try:
        response = requests.get(f"http://web-api:4000/o/Mentors/{advisorId}") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error retrieving profile: {response.json().get('error', 'Unknown error')}")
     except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {str(e)}")
    
     return None
     
all_mentees = fetch_all_mentees()    
advisor_mentors = fetch_advisor_mentors(advisorId)


# Add a new match
st.subheader("Manually Add a New Match")
mentor_names = [mentor['name'] for mentor in advisor_mentors] 
selected_mentor_name = st.selectbox('Choose Mentor', mentor_names) 
mentor = next((mentor for mentor in advisor_mentors if mentor['name'] == selected_mentor_name), None)


mentee_names = [mentee['name'] for mentee in all_mentees] 
selected_name = st.selectbox('Choose Mentee', mentee_names) 
mentee = next((mentee for mentee in all_mentees if mentee['name'] == selected_name), None)

if st.button("Add Match"):
    if mentor and mentee:

        match_data = {
             'menteeId' : mentee['menteeId'],
             'mentorId' : mentor['mentorId']
        }

        # st.write(match_data)

        try:
            create_new_job = requests.post('http://web-api:4000/o/MatchMentees', json=match_data)
            if create_new_job.status_code == 200:
                 st.success(f"Match between {mentor['name'],} and {mentee['name'],} added successfully!")
            else:
                st.error("Error creating this match. Please try again later.") 
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to server: {str(e)}")
       
    else:
        st.error("Please fill in both the mentor and mentee names.")

st.markdown("---")

# Edit an existing match
st.subheader("Edit an Existing Match")
match_to_edit = st.selectbox("Select a match to edit", options=range(len(advisorMatches)), format_func=lambda i: f"{advisorMatches[i]['name']} ↔ {advisorMatches[i]['MenteeUser.name']}")

if match_to_edit is not None:
    selected_match = advisorMatches[match_to_edit]

    ogMentorId = selected_match['Mentor.mentorId'],
    ogMenteeId = selected_match['Mentee.menteeId'],

    with st.expander('Edit Details'):
        mentor_names2 = [mentor["name"] for mentor in advisor_mentors]
        selected_mentor_name2 = st.selectbox(
            "Change Mentor",
            mentor_names2,
            index=mentor_names2.index(selected_match["name"]),
        )

        mentee_names2 = [mentee["name"] for mentee in all_mentees]
        selected_mentee_name2 = st.selectbox(
            "Change Mentee",
            mentee_names2,
            index=mentee_names2.index(selected_match["MenteeUser.name"]),
        )

        replacement_mentor = next(mentor for mentor in advisor_mentors if mentor["name"] == selected_mentor_name2)
        replacement_mentee = next(mentee for mentee in all_mentees if mentee["name"] == selected_mentee_name2)

        match_data = {
            'ogMentorId' : ogMentorId,
            'ogMenteeId' : ogMenteeId,
            'newMenteeId' : replacement_mentee['menteeId'],
            'newMentorId' : replacement_mentor['mentorId']
        }

        if st.button("Save Changes to Match"):
            try:
                create_new_job = requests.put('http://web-api:4000/o/UpdateMatch', json=match_data)
                
                if create_new_job.status_code == 200:
                    st.success("Match Updated")
                else:
                    st.error("Error editing this Match. Please try again later.") 
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")

    