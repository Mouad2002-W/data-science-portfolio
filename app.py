

from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np
app = Flask(__name__)

model = joblib.load('MLR_model.pkl')
scaler_loaded = joblib.load('scaler.pkl')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Extract and validate features y
    features = [
        data.get('area'),
        data.get('mainroad', 0),
        data.get('guestroom', 0),
        data.get('basement', 0),
        data.get('hotwaterheating', 0),
        data.get('airconditioning', 0),
        data.get('prefarea', 0),
        data.get('furnishingstatus_semi_furnished', 0),
        data.get('furnishingstatus_unfurnished', 0),
        data.get('bathrooms_2', 0),
        data.get('bathrooms_3', 0),
        data.get('bathrooms_4', 0),
        data.get('stories_2', 0),
        data.get('stories_3', 0),
        data.get('stories_4', 0),
        data.get('parking_1', 0),
        data.get('parking_2', 0),
        data.get('parking_3', 0),
        data.get('bedrooms_2', 0),
        data.get('bedrooms_3', 0),
        data.get('bedrooms_4', 0),
        data.get('bedrooms_5', 0),
        data.get('bedrooms_6', 0)
    ]



    # Convert features to a DataFrame
    features_df = pd.DataFrame([features], columns=[
        'area', 'mainroad', 'guestroom', 'basement', 'hotwaterheating',
        'airconditioning', 'prefarea', 'furnishingstatus_semi_furnished',
        'furnishingstatus_unfurnished', 'bathrooms_2', 'bathrooms_3',
        'bathrooms_4', 'stories_2', 'stories_3', 'stories_4', 'parking_1',
        'parking_2', 'parking_3', 'bedrooms_2', 'bedrooms_3', 'bedrooms_4',
        'bedrooms_5', 'bedrooms_6'
    ])

    # Scale the features using the loaded scaler
    features_scaled = scaler_loaded.transform(features_df)

    # Get the prediction from the regressor
    prediction = model.predict(features_scaled)[0]

   
    return jsonify({"prediction": prediction})


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
