import streamlit as st

def main():
    # Título del manual de usuario
    st.title('Manual de Usuario')

    # Sección 1: Introducción
    st.header('1. Introducció')
    st.write("""
    Benvingut al manual d'usuari de CoWorkMate 
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
              Clica a sobre d'una de les preguntes perquè CoWorkMate t'ajudi a resoldre-la. A més, podras anar indagant sobre el tema per si tens més dubtes.
    """)

    # Sección 4: Incidències
    st.header('4. Incidències')
    st.write("""
    Visualitza les incidències que s'han produït anteriorment per veure com han estat solucionades i les notes dels tècnics.
             Filtra per departament i per estat de la incidència i obtendras l'informació que necessites, també pots preguntar-li a CoWorkMate que busqui per tu.
    """)

    # Sección 5: Incidències
    st.header('5. ChattBot')
    st.write("""
    Millora les teves consultes amb el chatbot personalitzat. El chatbot s'adapta al teu context per oferir respostes precises. Des de resoldre dubtes fins a realitzar consultes a bases de dades,
              fes que la teva interacció sigui més eficient i personalitzada.
    """)

if __name__ == '__main__':
    main()
