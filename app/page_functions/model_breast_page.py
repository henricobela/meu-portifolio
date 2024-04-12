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
    # for f_name in feature_names:
    #     value = st.slider(f"Please select a value for {f_name}: ", min_value = df[f_name].min(), max_value = df[f_name].max())
    #     data.append(value)



    num_cols = 6
    num_features = len(feature_names)
    num_rows = -(-num_features // num_cols)  # Calcula o número de linhas necessárias

    # Determine o tamanho máximo do nome da característica
    max_name_length = max(len(name) for name in feature_names)

    for row in range(num_rows):
        cols = st.columns(num_cols)  # Cria uma linha com várias colunas
        for col_index, f_index in enumerate(range(row * num_cols, min((row + 1) * num_cols, num_features))):
            f_name = feature_names[f_index]
            padded_name = f_name.ljust(max_name_length)  # Alinhe o nome da característica com espaços
            value = cols[col_index].slider(f"Please select a value for {padded_name}: ", min_value=df[f_name].min(), max_value=df[f_name].max())
            data.append(value)

            

    # data = (11.76,21.6,74.72,427.9,0.08637,0.04966,0.01657,0.01115,0.1495,0.05888,0.4062,1.21,2.635,28.47,0.005857,0.009758,0.01168,0.007445,0.02406,0.001769,12.98,25.72,82.98,516.5,0.1085,0.08615,0.05523,0.03715,0.2433,0.06563)
    model = Model("app/models/breast/svc_model.pkl")
    y_pred = model.predict(data)
    st.header(y_pred)