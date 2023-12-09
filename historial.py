import streamlit as st

historial = []

def actualiza_prompt(prompt):
    if len(historial) > 5: historial.pop(0)
    historial.append({'Usuari': prompt, 'Assistent': "hola"})

def main():  
    for entry in historial:
        question_button = st.button( label=f"{entry['Usuari']}", key=f"button_{entry['Usuari']}", use_container_width=True)


if __name__ == '__main__':
    main()