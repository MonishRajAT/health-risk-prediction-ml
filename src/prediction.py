import joblib
import numpy as np


def _predict(model_path, scaler_path, input_data):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    input_array = np.array(input_data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)

    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    return prediction, probability


def predict_diabetes(input_data):
    return _predict(
        "models/diabetes_model.pkl",
        "models/diabetes_scaler.pkl",
        input_data
    )


def predict_heart(input_data):
    return _predict(
        "models/heart_model.pkl",
        "models/heart_scaler.pkl",
        input_data
    )


def predict_liver(input_data):
    return _predict(
        "models/liver_model.pkl",
        "models/liver_scaler.pkl",
        input_data
    )
