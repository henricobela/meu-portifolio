

def predict_on_new_data(input_data):
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array as we are predicting for one data point
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standardizing the input data
    input_data_std = scaler.transform(input_data_reshaped)

    prediction = model.predict(input_data_std)
    print(prediction)

    prediction_label = [np.argmax(prediction)]
    print(prediction_label)

    if(prediction_label[0] == 0):
        print('The tumor is Malignant')

    else:
        print('The tumor is Benign')