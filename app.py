import streamlit as st
import os
from streamlit_chat import message
from PIL import Image 
import time
from manual import main as show_manual
from client import main as show_client
from seguretat import main as show_seguretat
from manteniment import main as show_manteniment
from formacio import main as show_formacio 
import openai
from streamlit_lottie import st_lottie 
import json
import requests
from historial import add_question, show_buttons, main as main_h


def load_gif(filepath:str):
    with open(filepath, "r") as f:
              return json.load(f) 


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
    st.session_state["messages"] = [{"role": "assistant", "content": "Hola, soy ChatPittot, ¿En qué puedo ayudarte?"}]


# SIDEBAR ----------------------------------------------------------------------
gif = load_gif("gif.json")
with st.sidebar:
    st_lottie(gif,
          speed=1,
          reverse=False,
          loop = True,
          height=150,
          width=150,
        )
    logo = Image.open('logo.png')
    ancho_logo = 195
    eslogan = "<p style='font-weight: bold; font-style: italic;'>La Màgia de ChatPittot: Feina Fàcil, Resultats Increïbles.</p>"
    #st.image(logo, width=ancho_logo)
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
        show_buttons()
        res = main_h() 
        print(res)

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


prompt = st.chat_input("Say something")
if user_input := prompt or res != None:
    if res != None: 
        user_input = res
        
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    loading_placeholder = st.empty() 

    # Display a GIF while waiting for the response
    gif_path = "loading.gif"  # Replace with the actual path to your GIF
    loading_placeholder.chat_message("assistant").image(gif_path) 
    add_question(user_input)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state["messages"],
    )
    responseMessage = response['choices'][0]['message']['content']

    loading_placeholder.empty() 

    st.session_state["messages"].append({"role": "assistant", "content": responseMessage})
    st.chat_message("assistant").write(responseMessage)