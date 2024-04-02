import streamlit as st
import numpy as np
import pandas as pd
from utils.config_page import default_set_page_config
from streamlit_option_menu import option_menu



default_set_page_config()


selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1,
        orientation="horizontal")

st.header(selected)

#todo: listagem das opções do menu


