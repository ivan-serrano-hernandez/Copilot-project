import streamlit as st

def main():
    # Título del manual de usuario
    st.title('Manual de Usuario')

    # Sección 1: Introducción
    st.header('1. Introducción')
    st.write("""
    Bienvenido al manual de usuario de nuestra aplicación. 
    Esta aplicación está diseñada para ayudarte en diferentes tareas.
    """)

    # Sección 2: Cómo Empezar
    st.header('2. Cómo Empezar')
    st.write("""
    Para comenzar, sigue estos pasos:
    1. **Paso 1:** Abre la aplicación.
    2. **Paso 2:** Selecciona las opciones deseadas.
    3. **Paso 3:** Haz clic en el botón "Ejecutar".

    ¡Y eso es todo! La aplicación hará el resto por ti.
    """)

    # Sección 3: Funcionalidades Avanzadas
    st.header('3. Funcionalidades Avanzadas')
    st.write("""
    Esta aplicación también incluye algunas funcionalidades avanzadas:
    - **Función A:** Descripción de la función A.
    - **Función B:** Descripción de la función B.
    """)

    # Sección 4: Preguntas Frecuentes
    st.header('4. Preguntas Frecuentes')
    st.write("""
    **Pregunta 1:** ¿Cómo puedo personalizar mi perfil?
    **Respuesta:** Para personalizar tu perfil, ve a la sección de configuración y sigue las instrucciones.

    **Pregunta 2:** ¿Cómo puedo contactar al soporte técnico?
    **Respuesta:** Puedes contactar al soporte técnico a través del formulario de contacto en nuestra página web.
    """)

    # Sección 5: Conclusión
    st.header('5. Conclusión')
    st.write("""
    Gracias por utilizar nuestra aplicación. Si tienes alguna pregunta adicional, no dudes en ponerte en contacto con nosotros.
    """)

if __name__ == '__main__':
    main()
