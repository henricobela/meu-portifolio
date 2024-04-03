import streamlit as st

def default_set_page_config():
    st.set_page_config(
        initial_sidebar_state = "collapsed",
        page_icon = "utils/imgs/logotipo_sem_escrito.svg",
        page_title = "Portfolio", layout = "wide")