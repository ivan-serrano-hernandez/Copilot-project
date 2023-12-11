import streamlit as st
import pandas as pd
def main():
    # Título del manual de usuario
    st.title('Incidències')

    pd.set_option('display.max_columns', None)  # Display all columns without truncation
    pd.set_option('display.width', None)  # Display DataFrame with all possible width
    pd.set_option('display.max_colwidth', None)

    df = pd.read_csv('./data/incidencies.csv')
    search_text = st.text_input('Cerca...')
    department = st.radio('Departament', ['Tots','Manteniment', 'Seguretat', 'Atenció client', 'Formació'],index=0, horizontal=True)
    estat = st.radio('Departament', ['Tots','Solucionat', 'Fallit', 'Pendent'],index=0, horizontal=True)
    if estat == 'Tots' and department == 'Tots':
        st.write(df)
    elif estat == 'Tots' and department != 'Tots':
        filtered_df = df[df['Departament'] == department]
        st.write(filtered_df)
    elif estat != 'Tots' and department == 'Tots':
        filtered_df = df[df['Estat'] == estat]
        st.write(filtered_df)
    else:
        filtered_df = df[(df['Departament'] == department) & (df['Estat'] == estat)]
        st.write(filtered_df)
    

if __name__ == '__main__':
    main()
