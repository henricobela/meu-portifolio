import streamlit as st
import pandas as pd
from models.breast.breast_model import *
from utils.config_page import *


def breast_page():

    feature_names_path = localize_right_path({"path_featurenames": "app/models/breast/feature_names.txt",
                                              "path_featurenames2": "models/breast/feature_names.txt"})
    base_path = localize_right_path({"path_database": "app/models/breast/values_min_max.csv",
                                     "path_database2": "models/breast/values_min_max.csv"})
    model_path = localize_right_path({"path_model": "app/models/breast/svc_model.pkl",
                                      "path_model2": "models/breast/svc_model.pkl"})
    feature_names = []
    data = []
    df = pd.read_csv(base_path)
    with open(feature_names_path, 'r') as f:
        for line in f:
            feature_name = line.strip()
            feature_names.append(feature_name)
    
    
    with st.sidebar:
        st.markdown("---")
        st.info("Here you found the caracteristics which can determinate if a breast cancer is Malign or Benign. Please use the sliders to send the informations to model and get the results.")
        for f_name in feature_names:
            string_f_name = f_name.title()
            value = st.slider(f"{string_f_name}: ", min_value = df[f_name].min(), max_value = df[f_name].max())
            data.append(value)

    model = Model(model_path)
    y_pred = model.predict(data)
    st.header(y_pred)