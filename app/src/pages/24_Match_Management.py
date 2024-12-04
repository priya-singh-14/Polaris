import streamlit as st
from streamlit_extras.app_logo import add_logo

# Add Logo
add_logo("assets/logo.png", height=400)

# Page title
st.title("Match Management Dashboard 🔗")

# Description
st.markdown("""
This page allows advisors to manage mentor-mentee matches effectively. You can view, add, edit, and remove matches to ensure the best connections.
""")

# Initialize session state for match data
if "matches" not in st.session_state:
    st.session_state.matches = [
        {"mentor": "Sarah Star", "mentee": "Tyler Dipper", "tags": ["Finance", "Career Change"]},
        {"mentor": "Alan Turing", "mentee": "Jane Doe", "tags": ["AI", "Research"]},
    ]

# Display existing matches
st.subheader("Current Matches")
if st.session_state.matches:
    for idx, match in enumerate(st.session_state.matches):
        st.markdown(f"**Mentor:** {match['mentor']}")
        st.markdown(f"**Mentee:** {match['mentee']}")
        st.markdown(f"**Tags:** {', '.join(match['tags'])}")
        if st.button(f"Remove Match #{idx + 1}", key=f"remove_{idx}"):
            st.session_state.matches.pop(idx)
            st.success(f"Removed Match #{idx + 1}")
        st.markdown("---")
else:
    st.write("No matches available.")

# Add a new match
st.subheader("Add a New Match")
mentor_name = st.text_input("Mentor Name")
mentee_name = st.text_input("Mentee Name")
match_tags = st.text_area("Tags (comma-separated)", placeholder="e.g., Finance, AI, Research")

if st.button("Add Match"):
    if mentor_name and mentee_name:
        tags_list = [tag.strip() for tag in match_tags.split(",")] if match_tags else []
        new_match = {"mentor": mentor_name, "mentee": mentee_name, "tags": tags_list}
        st.session_state.matches.append(new_match)
        st.success(f"Match between {mentor_name} and {mentee_name} added successfully!")
    else:
        st.error("Please fill in both the mentor and mentee names.")

# Edit an existing match
st.subheader("Edit an Existing Match")
match_to_edit = st.selectbox("Select a match to edit", options=range(len(st.session_state.matches)), format_func=lambda i: f"{st.session_state.matches[i]['mentor']} ↔ {st.session_state.matches[i]['mentee']}")

if match_to_edit is not None:
    selected_match = st.session_state.matches[match_to_edit]
    edited_mentor = st.text_input("Edit Mentor Name", value=selected_match["mentor"])
    edited_mentee = st.text_input("Edit Mentee Name", value=selected_match["mentee"])