import streamlit as st


def localize_path_logo():
    path_logo = ""
    path_to_logo = {
        "path_one": "app/utils/imgs/logotipo_sem_escrito.svg",
        "path_two": "utils/imgs/logotipo_sem_escrito.svg"}
    
    for path in path_to_logo.values():
        try:
            open(path)
            path_logo = path
        except:
            continue
    return path_logo


def default_set_page_config(path_icon):
    st.set_page_config(
        initial_sidebar_state = "collapsed",
        page_icon = path_icon,
        page_title = "Portfolio", layout = "wide")


def localize_right_path(path:dict):
    right_path = ""
    for epath in path.values():
        try:
            open(epath)
            right_path = epath
        except:
            continue
    return right_path