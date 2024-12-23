import streamlit as st
from ChatBot import ai_chat_page
from Profile import profile_page
from Roadmaps_page import roadmaps_page
from style import Style

# Apply updated style
Style()

# Sidebar Navigation
st.sidebar.header("DevNavigator")
if "page" not in st.session_state:
    st.session_state["page"] = "home"

if st.sidebar.button("Home"):
    st.session_state["page"] = "home"
if st.sidebar.button("Roadmaps"):
    st.session_state["page"] = "roadmaps"
if st.sidebar.button("AI Chat"):
    st.session_state["page"] = "ai_chat"
if st.sidebar.button("Profile"):
    st.session_state["page"] = "profile"

# Main Page Logic
if st.session_state["page"] == "home":
    st.title("Welcome to DevNavigator")
    st.markdown("<p class='card'>Explore Roadmaps</p>", unsafe_allow_html=True)
    st.markdown("<p class='card'>Get Started</p>", unsafe_allow_html=True)

elif st.session_state["page"] == "roadmaps":
    roadmaps_page()

elif st.session_state["page"] == "ai_chat":
    ai_chat_page()

elif st.session_state["page"] == "profile":
    profile_page()
