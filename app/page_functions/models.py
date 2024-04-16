import streamlit as st
from page_functions.model_breast_page import breast_page
from page_functions.model_cv_page import cv_page
from page_functions.model_rentals_page import rentals_page


def models_page():

    st.info("Welcome to the page that contains all models built by me!"+
                 "\nThese models was developed using some algorithms libraries, such as "+
                 "OpenCV, Scikit Learn, Tensorflow, Keras, Pytorch, and more! "+
                 "\nFeel free to contact me to ask questions and chat!")    

    st.sidebar.title("Sidebar")
    page = st.sidebar.radio("Select Page", ["Breast", "Computer Vision", "Rentals"])

    if page == "Breast":
        breast_page()
    elif page == "Computer Vision":
        cv_page()
    elif page == "Rentals":
        rentals_page()

