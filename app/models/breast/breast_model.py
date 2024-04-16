import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from utils.config_page import *


class Model:
    
    def __init__(self, model_path):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
        

        scaler_path = localize_right_path({"scaler_path": "app/models/breast/scaler.pkl",
                                           "scaler_path2": "models/breast/scaler.pkl"})

        with open(scaler_path, 'rb') as f:
            self.scaler = pickle.load(f)

    def predict(self, input_data):
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        input_data_std = self.scaler.transform(input_data_reshaped)
        prediction = self.model.predict(input_data_std)
        if prediction == 0:
            return True
        else:
            return False