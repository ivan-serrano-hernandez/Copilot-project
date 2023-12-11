import streamlit as st

buttons_names = []
buttons = []

def read_faqs_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

def main():
    faqs = read_faqs_from_file('faqs/manteniment.txt') 

    for faq in faqs:
        button = st.button(faq)
        buttons.append((faq, button))

def m_check_button():
    for (label, but) in buttons:
        if but: 
            buttons.remove((label, but))
            return str(label)
            
    return None

if __name__ == '__main__':
    main()
