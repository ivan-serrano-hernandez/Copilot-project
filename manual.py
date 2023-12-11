import streamlit as st

def main():
    # Título del manual de usuario
    st.title('Manual de Usuario')

    # Sección 1: Introducción
    st.header('1. Introducció')
    st.write("""
    Benvingut al manual d'usuari de ChatPittot 
    Un Copilot pensat per maximitzar la teva eficiència!.
    """)

    # Sección 2: Funcionalidades Avanzadas
    st.header('2. Funcionalitats')
    st.write("""
    - **Chatbott:** Demana qualsevol dubte o pregunta que tenguis sobre .
    - **Faqs:** Les preguntes més freqüents.
    - **Base de dades d'incidències:** Accedeix a les incidències que s'han produït anteriorment per veure com han estat solucionades i les notes dels tècnics.
    """)

    # Sección 3: Preguntas Frecuentes
    st.header('3. Preguntas Frecuentes')
    st.write("""
    A la barra lateral podras accedeir a les preguntes més freqüents que han fet altres tècnics i que poden portar més preguntes.
              Clica a sobre d'una de les preguntes perquè ChatPittot t'ajudi a resoldre-la. A més, podras anar indagant sobre el tema per si tens més dubtes.
    """)

    # Sección 4: Incidències
    st.header('4. Incidències')
    st.write("""
    Visualitza les incidències que s'han produït anteriorment per veure com han estat solucionades i les notes dels tècnics.
             Filtra per departament i per estat de la incidència i obtendras l'informació que necessites, també pots preguntar-li a ChatPittot que busqui per tu.
    """)

if __name__ == '__main__':
    main()
