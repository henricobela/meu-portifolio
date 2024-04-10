import streamlit as st


def models_page():

    st.info("Welcome to the page that contains all models built by me!"+
                 "\nThese models was developed using some algorithms libraries, such as "+
                 "OpenCV, Scikit Learn, Tensorflow, Keras, Pytorch, and more! "+
                 "\nFeel free to contact me to ask questions and chat!")

    tab_breast, tab_cv, tab_rentals = st.tabs(["Breast", "Computer Vision", "Rentals"])

    with tab_breast:
        st.text("Breast")
    with tab_cv:
        st.text("Computer Vision")
    with tab_rentals:
        st.text("Rentals")        


