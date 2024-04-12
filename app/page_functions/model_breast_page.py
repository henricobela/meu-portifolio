import streamlit as st
from models.breast.breast_model import *

def breast_page():
    data = (11.76,21.6,74.72,427.9,0.08637,0.04966,0.01657,0.01115,0.1495,0.05888,0.4062,1.21,2.635,28.47,0.005857,0.009758,0.01168,0.007445,0.02406,0.001769,12.98,25.72,82.98,516.5,0.1085,0.08615,0.05523,0.03715,0.2433,0.06563)
    model = Model("app/models/breast/svc_model.pkl")
    y_pred = model.predict(data)
    st.header(y_pred)