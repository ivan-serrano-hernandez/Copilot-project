import streamlit as st
import os
from streamlit_chat import message
from PIL import Image
import random
import time


def first10char(msg):
    newMsg = ""
    for i, c in enumerate(msg):
        if i == 20:
            return newMsg + "..."
        newMsg +=c
    return newMsg

def emptySessionState():
    for k in st.session_state.keys():
        del st.session_state[k]

# Page setup
st.set_page_config(
    page_title="coWorkMate",
    layout="wide",  # Use "wide" layout to make the main page wider
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# SIDEBAR ----------------------------------------------------------------------
with st.sidebar:
    st.title('[coWorkMate logo]')
    st.markdown("---")
    st.markdown("**coWorkMate is a GPT-3 based AI model specifically fine-tunned for day to day interactions within a security operations center.**")



# MAIN PAGE ---------------------------------------------------------------------
logo = Image.open('company_heading.jpg')
st.image(logo)
st.markdown("### A NLP tool to enhance your workspace")
st.markdown("---")

# set of welcome prompts 
welcome_msgs = [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?"
        ]

# display assistant's initial text
with st.chat_message("assistant"):
    message_placeholder = st.empty()
    full_response = ""
    assistant_welcome_msg = random.choice(welcome_msgs)
    for chunk in assistant_welcome_msg.split():
        full_response += chunk + " "
        time.sleep(0.1)
        # Add a blinking cursor to simulate typing
        message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)

# conversation itself ------

firstPrompt = True
if prompt := st.chat_input("Introduce your prompt"):
    # Display user message in chat message container
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display updated chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


