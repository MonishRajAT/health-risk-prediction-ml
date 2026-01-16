import joblib
import numpy as np


def _predict(model_path, input_data):
    model = joblib.load(model_path)

    input_array = np.array(input_data).reshape(1, -1)

    prediction = model.predict(input_array)[0]
    probability = model.predict_proba(input_array)[0][1]

    return prediction, probability


def predict_diabetes(input_data):
    return _predict(
        "models/diabetes_model.pkl",
        input_data
    )


def predict_heart(input_data):
    return _predict(
        "models/heart_model.pkl",
        input_data
    )


def predict_liver(input_data):
    return _predict(
        "models/liver_model.pkl",
        input_data
    )
