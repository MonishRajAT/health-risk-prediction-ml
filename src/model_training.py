import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score

MODELS_PATH = "models"
os.makedirs(MODELS_PATH, exist_ok = True)

# Generic training function (REUSABLE)
def train_model(csv_path, target_col, model_name):
    df = pd.read_csv(csv_path)

    X = df.drop(columns = [target_col])
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size = 0.2, random_state = 42, stratify = y
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = RandomForestClassifier(
        n_estimators = 200,
        random_state = 40,
        class_weight = 'balanced'
    )
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    print(f"\n📌 {model_name.upper()} MODEL")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))

    joblib.dump(model, f"{MODELS_PATH}/{model_name}_model.pkl")
    joblib.dump(scaler, f"{MODELS_PATH}/{model_name}_scaler.pkl")

    print(f"✅ {model_name}_model.pkl saved")


# Train all the models
if __name__ == "__main__":
    train_model(
        csv_path = "data/processed/diabetes_clean.csv",
        target_col = "Outcome",
        model_name = "diabetes"
    )
    train_model(
        csv_path = "data/processed/heart_clean.csv",
        target_col = "target",
        model_name = "heart"
    )
    train_model(
        csv_path = "data/processed/liver_clean.csv",
        target_col = "target",
        model_name = "liver"
    )