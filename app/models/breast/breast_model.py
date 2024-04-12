import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler


class Model:
    
    def __init__(self, model_path):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
            
        with open("app/models/breast/scaler.pkl", 'rb') as f:
            self.scaler = pickle.load(f)

    def predict(self, input_data):
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        input_data_std = self.scaler.transform(input_data_reshaped)
        prediction = self.model.predict(input_data_std)
        return prediction