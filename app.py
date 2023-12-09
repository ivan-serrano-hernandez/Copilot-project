import streamlit as st
import os
from streamlit_chat import message
from PIL import Image
import random
import time
from manual import main as show_manual
from client import main as show_client
from seguretat import main as show_seguretat
from manteniment import main as show_manteniment
from formacio import main as show_formacio
import openai


openai.api_key = "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"

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


def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",  # or any other suitable GPT-3 model
        prompt=prompt,
        max_tokens=150  # adjust as needed
    )
    return response['choices'][0]['text'].strip()

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
    logo = Image.open('logo.png')
    ancho_logo = 195
    eslogan = "<p style='font-weight: bold; font-style: italic;'>La Màgia de ChatPittot: Feina Fàcil, Resultats Increïbles.</p>"
    st.image(logo, width=ancho_logo)
    st.markdown(eslogan, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("**LES TOP 10 PREGUNTES MÉS FREQÜENTS**")

    st.markdown(
    """
    <style>
    .stButton>button {
        float: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    # Utilizar st.expander para mostrar el manual directamente
    with st.expander("Seguretat"):
        show_seguretat()  # Ejecuta la función principal del manual.py
    with st.expander("Manteniment"):
        show_manteniment()  # Ejecuta la función principal del manual.py
    with st.expander("Atenció Client"):
        show_client()  # Ejecuta la función principal del manual.py
    with st.expander("Formació"):
        show_formacio()  # Ejecuta la función principal del manual.py

    st.markdown("---")

        # Utilizar st.expander para mostrar el manual directamente
    with st.expander("Historial Preguntes"):
        show_seguretat()  # Ejecuta la función principal del manual.py



# MAIN PAGE ---------------------------------------------------------------------
logo = Image.open('company_heading_blue.jpg')
ancho_logo = 1350
st.image(logo, width=ancho_logo)
st.markdown(
    """
    <style>
    .stButton>button {
        float: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Utilizar st.expander para mostrar el manual directamente
with st.expander("Manual de Usuario"):
    show_manual()  # Ejecuta la función principal del manual.py

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
    
    # Use GPT-3 to generate a response
    gpt_response = generate_response(prompt)
    
    # Display GPT-3 response in chat message container
    st.session_state.messages.append({"role": "assistant", "content": gpt_response})
    
    # Display updated chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


