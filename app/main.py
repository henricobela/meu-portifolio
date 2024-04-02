import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu



selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)

st.header(selected)

