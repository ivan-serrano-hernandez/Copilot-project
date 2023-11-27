import streamlit as st
import os
from streamlit_chat import message

# App title
st.set_page_config(page_title="gSOC Copilot")

# Replicate Credentials
with st.sidebar:
    st.title('gSOC Copilot')
    st.markdown("---")
    st.markdown('About this project [blog](https://github.com/ivan-serrano-hernandez/Copilot-project)!')

st.markdown("# gSOC Copilot")
st.markdown("### El teu millor company de treball")

with st.chat_message("assistant"):
    st.write("Hola company! Com et puc ajudar?")

prompt = st.chat_input("Introdueix el teu prompt")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

