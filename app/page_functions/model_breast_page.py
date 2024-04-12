import streamlit as st
import pandas as pd
from models.breast.breast_model import *


def breast_page():

    feature_names_path = "app/models/breast/feature_names.txt"
    feature_names = []
    data = []
    df = pd.read_csv("app/models/breast/values_min_max.csv")
    
    with open(feature_names_path, 'r') as f:
        for line in f:
            feature_name = line.strip()
            feature_names.append(feature_name)
    for f_name in feature_names:
        value = st.slider(f"Please select a value for {f_name}: ", min_value = df[f_name].min(), max_value = df[f_name].max())
        data.append(value)

    model = Model("app/models/breast/svc_model.pkl")
    y_pred = model.predict(data)
    st.header(y_pred)