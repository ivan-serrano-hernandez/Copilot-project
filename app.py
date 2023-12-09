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
from historial import main as show_historial
from historial import actualiza_prompt
import openai


openai.api_key = "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"

def simulate_typing(text):
    time.sleep(0.5)
    message_placeholder = st.empty()
    full_response = ""
    assistant_welcome_msg = text
    for chunk in assistant_welcome_msg.split():
        full_response += chunk + " "
        time.sleep(0.15)
        # Add a blinking cursor to simulate typing
        message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)

def welcome():
    message_placeholder = st.empty()
    full_response = ""
    assistant_welcome_msg = random.choice(welcome_msgs)
    for chunk in assistant_welcome_msg.split():
        full_response += chunk + " "
        time.sleep(0.15)
        # Add a blinking cursor to simulate typing
        message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)

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
    st.session_state["messages"] = [{"role": "assistant", "content": "Hola, soy ChatGPT, ¿En qué puedo ayudarte?"}]


# SIDEBAR ----------------------------------------------------------------------
with st.sidebar:
    logo = Image.open('logo.png')
    ancho_logo = 195
    eslogan = "<p style='font-weight: bold; font-style: italic;'>La Màgia de ChatPittot: Feina Fàcil, Resultats Increïbles.</p>"
    st.image(logo, width=ancho_logo)
    st.markdown(eslogan, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("**LES TOP 10 PREGUNTES MÉS FREQÜENTS**")

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
        show_historial()  # Ejecuta la función principal del manual.py



# MAIN PAGE ---------------------------------------------------------------------
logo = Image.open('company_heading_blue.jpg')
ancho_logo = 1350
st.image(logo, width=ancho_logo)

# Manual usuari
with st.expander("Manual de Usuario"):  show_manual() 
 
st.markdown("---")

# Conversa amb GPT
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

if user_input := st.chat_input():
    st.session_state["messages"].append({"role": "user", "content" : user_input})
    st.chat_message("user").write(user_input)
    response = openai.Completion.create(
        engine="text-davinci-003",
        messages=st.session_state["messages"],
        temperature=0,
        max_token=150,
    )
    responseMessage=response['choices'][0]['text']
    st.session_state["messages"].append({"role":"assistant", "content": responseMessage})
    st.chat_message("assistant").write(responseMessage)