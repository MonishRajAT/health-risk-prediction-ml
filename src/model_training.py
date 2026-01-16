import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score

MODELS_PATH = "models"
os.makedirs(MODELS_PATH, exist_ok=True)


def train_model(csv_path, target_col, model_name, model_params):
    df = pd.read_csv(csv_path)

    X = df.drop(columns=[target_col])
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        **model_params,
        random_state=42,
        class_weight="balanced"
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"\n📌 {model_name.upper()} MODEL")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))

    joblib.dump(model, f"{MODELS_PATH}/{model_name}_model.pkl")
    print(f"✅ {model_name}_model.pkl saved")



# Train all models (TUNED)
if __name__ == "__main__":

    # Diabetes 
    train_model(
        csv_path="data/processed/diabetes_clean.csv",
        target_col="Outcome",
        model_name="diabetes",
        model_params={
            "n_estimators": 400,
            "max_depth": 10,
            "min_samples_split": 5,
            "min_samples_leaf": 2
        }
    )

    # Heart 
    train_model(
        csv_path="data/processed/heart_clean.csv",
        target_col="target",
        model_name="heart",
        model_params={
            "n_estimators": 200,
            "max_depth": None
        }
    )

    # Liver 
    train_model(
        csv_path="data/processed/liver_clean.csv",
        target_col="target",
        model_name="liver",
        model_params={
            "n_estimators": 500,
            "max_depth": 8,
            "min_samples_split": 10,
            "min_samples_leaf": 4
        }
    )
