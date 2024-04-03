import streamlit as st
import numpy as np
import pandas as pd
from utils.config_page import default_set_page_config
from streamlit_option_menu import option_menu



default_set_page_config()


selected = option_menu("Main Menu", ["Home", "About me", "Model 1", "Model 2", "Model 3", 'Settings', 'Contact', ], 
        icons=['house', 'terminal', 'activity', 'eye', 'currency-dollar', 'gear', 'telephone-forward'], menu_icon="cast", default_index=1,
        orientation="horizontal")


if selected == "Home":
        st.header(selected)
        st.subheader("Here we are Home")

elif selected == "About me":
        st.header(selected)
        st.subheader("Here we are about me")

elif selected == "Model 1":
        st.header(selected)
        st.subheader("Here we are Model 1")

elif selected == "Model 2":
        st.header(selected)
        st.subheader("Here we are Model 2")

elif selected == "Model 3":
        st.header(selected)
        st.subheader("Here we are Model 3")

elif selected == "Settings":
        st.header(selected)
        st.subheader("Here we are Settings")

elif selected == "Contact":
        st.header(selected)
        st.subheader("Here we are Contact")






