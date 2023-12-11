import streamlit as st

buttons_names = []
buttons = []


def main():
    for (label, but) in buttons:
        if but: 
            buttons.remove((label, but))
            return str(label)
            
    return None

def add_question(label, button):
    if not button: buttons_names.append(label)

def show_buttons():
    for but in buttons_names:
        b = st.button(but)
        buttons.append((but, b))



if __name__ == '__main__':
    main()