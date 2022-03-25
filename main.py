import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import pickle
from tensorflow import keras
from preprocessing import imput_missing, outlier

## make app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json
    data = pd.DataFrame(json_)
    data = outlier(data, data.columns)
    data = imput_missing(data)
    prediction = model.predict(data)
    predict = []
    for x in prediction:
        if x <= 0.5:
            predict.append("Default")
        else:
            predict.append("Not Default")    

    return jsonify({"Prediction": predict})

if __name__ == '__main__':
    model = keras.models.load_model('Model/classification.h5')
    app.run(debug=True, host='0.0.0.0')
