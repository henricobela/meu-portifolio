import streamlit as st
from utils.config_page import default_set_page_config, localize_path_logo
from streamlit_navigation_bar import st_navbar
from page_functions.home_page import home
from page_functions.about_me_page import about_page
from page_functions.model_breast_page import breast_page
from page_functions.model_cv_page import cv_page
from page_functions.model_rentals_page import rentals_page
from page_functions.contact_page import contact_me_page
from page_functions.settings_page import settings


path_logo = localize_path_logo()
default_set_page_config(path_icon = path_logo)



selected = st_navbar(["Home", "About me", "Model 1", "Model 2", "Model 3", 'Settings', 'Contact'], logo_path = path_logo)


col_p, col_s, _ = st.columns([1, 2, 3])

with col_p:
        st.image(path_logo)

with col_s:
        if selected == "Home":
                home()
        elif selected == "About me":
                about_page()
        elif selected == "Model 1":
                breast_page()
        elif selected == "Model 2":
                cv_page()
        elif selected == "Model 3":
                rentals_page()
        elif selected == "Settings":
                settings()
        elif selected == "Contact":
                contact_me_page()


st.button("Dummy Button")






