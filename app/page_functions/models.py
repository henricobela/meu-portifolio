import streamlit as st
from page_functions.model_breast_page import breast_page
from page_functions.model_cv_page import cv_page
from page_functions.model_rentals_page import rentals_page


def models_page():

    st.info("Info: Here we have a sidebar to select which model to use, feel free to test every model. They was developed by me, using some libs like sklearn and tensorflow.")    

    st.sidebar.title("Models")
    page = st.sidebar.selectbox("Select the model", ["Breast", "Computer Vision", "Rentals"])

    if page == "Breast":
        breast_page()
    elif page == "Computer Vision":
        cv_page()
    elif page == "Rentals":
        rentals_page()

