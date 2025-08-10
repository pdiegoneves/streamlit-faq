import streamlit as st


def question(question:str, answer:str):
    with st.expander(question):
        st.text(answer)
    