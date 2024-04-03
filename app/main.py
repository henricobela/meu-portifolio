import streamlit as st
import numpy as np
import pandas as pd
from utils.config_page import default_set_page_config
from streamlit_option_menu import option_menu



default_set_page_config()


selected = option_menu("Main Menu", ["Home", "Model 1", "Model 2", "Model 3", 'Settings', ], 
        icons=['house', 'activity', 'cash-stack', 'currency-dollar','gear'], menu_icon="cast", default_index=1,
        orientation="horizontal")


if selected == "Home":
        st.header(selected)
        st.subheader("Here we are Home")

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

#todo: listagem das opções do menu




