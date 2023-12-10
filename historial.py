import streamlit as st

buttons_names = []
buttons = []


def main():
    for but in buttons:
        if but: return "hola"
    return None

def add_question(label):
    buttons_names.append(label)

def show_buttons():
    for but in buttons_names:
        b = st.button(but)
        buttons.append(b)



if __name__ == '__main__':
    main()