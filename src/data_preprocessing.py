import pandas as pd
import os

PROCESSED_PATH = "data/processed"
os.makedirs(PROCESSED_PATH, exist_ok=True)

# --------------------------------------------------
# Diabetes dataset preprocessing
# --------------------------------------------------
def clean_diabetes_data():
    df = pd.read_csv("data/raw/diabetes.csv")

    zero_columns = [
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI"
    ]

    for col in zero_columns:
        df[col] = df[col].replace(0, df[col].median())

    df.to_csv(f"{PROCESSED_PATH}/diabetes_clean.csv", index=False)
    print("✅ Diabetes data cleaned and saved.")


# --------------------------------------------------
# Heart Disease dataset preprocessing
# --------------------------------------------------
def clean_heart_disease_data():
    df = pd.read_csv("data/raw/heart_disease.csv")

    df = df.drop_duplicates()

    df["target"] = df["target"].apply(lambda x: 1 if x > 0 else 0)

    df.to_csv(f"{PROCESSED_PATH}/heart_clean.csv", index=False)
    print("✅ Heart Disease data cleaned and saved.")


# --------------------------------------------------
# Liver Disease dataset preprocessing (FIXED)
# --------------------------------------------------
def clean_liver_disease_data():
    df = pd.read_csv("data/raw/liver.csv")

    # Encode gender (lowercase column name)
    df["gender"] = df["gender"].map({"Male": 1, "Female": 0})

    # Target column already binary (1 = patient, 0 = no disease)
    df.rename(columns={"is_patient": "target"}, inplace=True)

    # Fill missing numerical values
    df = df.fillna(df.median(numeric_only=True))

    df.to_csv(f"{PROCESSED_PATH}/liver_clean.csv", index=False)
    print("✅ Liver Disease data cleaned and saved.")


# --------------------------------------------------
# Run all preprocessing steps
# --------------------------------------------------
if __name__ == "__main__":
    clean_diabetes_data()
    clean_heart_disease_data()
    clean_liver_disease_data()
