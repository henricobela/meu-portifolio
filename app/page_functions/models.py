import streamlit as st
from page_functions.model_breast_page import breast_page
from page_functions.model_cv_page import cv_page
from page_functions.model_rentals_page import rentals_page


def models_page():

    st.info("Welcome to the page that contains all models built by me!"+
                 "\nThese models was developed using some algorithms libraries, such as "+
                 "OpenCV, Scikit Learn, Tensorflow, Keras, Pytorch, and more! "+
                 "\nFeel free to contact me to ask questions and chat!")

    # tab_breast, tab_cv, tab_rentals = st.tabs(["Breast", "Computer Vision", "Rentals"])

    # with tab_breast:
    #     if ("cv" in st.session_state) and ("rentals" in st.session_state):
    #         st.session_state.pop("cv")
    #         st.session_state.pop("rentals")
    #     st.session_state["breast"] = "new_breast_state"
    #     st.text("Dev")
    #     breast_page()
    # with tab_cv:
    #     if ("breast" in st.session_state) and ("rentals" in st.session_state):
    #         st.session_state.pop("breast")
    #         st.session_state.pop("rentals")
    #     st.session_state["cv"] = "new_cv_state"
    #     st.text("Dev")
    # with tab_rentals:
    #     if ("cv" in st.session_state) and ("breast" in st.session_state):
    #         st.session_state.pop("cv")
    #         st.session_state.pop("breast")
    #     st.session_state["breast"] = "new_rentals_state"
    #     st.text("Dev")        

    st.sidebar.title("Sidebar")
    page = st.sidebar.radio("Select Page", ["Breast", "Computer Vision", "Rentals"])

    if page == "Breast":
        breast_page()
    elif page == "Computer Vision":
        cv_page()
    elif page == "Rentals":
        rentals_page()

