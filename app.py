import streamlit as st
from src.prediction import (
    predict_diabetes,
    predict_heart,
    predict_liver
)
from src.utils import risk_message



# Page Config
st.set_page_config(
    page_title="Health Risk Prediction System",
    page_icon="🩺",
    layout="wide"
)



# Sidebar
st.sidebar.title("🧠 Health ML System")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Diabetes", "Heart Disease", "Liver Disease"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "⚕️ This application uses Machine Learning models\n"
    "to predict disease risk based on clinical inputs.\n\n"
    "📌 Educational & decision-support purpose only."
)



# Header 
st.markdown(
    "<h1 style='text-align: center;'>🩺 Intelligent Health Risk Prediction</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>ML Models-powered health risk assessment using Machine Learning</p>",
    unsafe_allow_html=True
)
st.markdown("---")



# HOME PAGE
if page == "Home":
    st.subheader("🏠 Welcome to the Health Risk Prediction System")

    st.markdown("""
    ### 📌 About This Project
    This web application is an **Healthcare decision-support system**
    built using **Machine Learning and Streamlit**.

    The goal of this project is to help users **estimate potential health risks**
    based on clinical and lifestyle parameters.
    """)

    st.markdown("""
    ### 🧠 Diseases Covered
    - 🩸 **Diabetes Risk Prediction**
    - ❤️ **Heart Disease Risk Prediction**
    - 🧪 **Liver Disease Risk Prediction**
    """)

    st.markdown("""
    ### ⚙️ How It Works
    1. Select a disease from the **sidebar menu**
    2. Enter the required health parameters
    3. Click on **Predict Risk**
    4. Get an instant **risk probability and interpretation**
    """)

    st.markdown("""
    ### 👉 How to Navigate
    Use the **left sidebar** to switch between:
    - Home (this page)
    - Diabetes test
    - Heart disease test
    - Liver disease test
    """)

    st.success("✅ Start by selecting a disease from the sidebar to begin your assessment.")

    st.markdown("---")
    st.info(
        "⚠️ Disclaimer: This tool is for educational purposes only and "
        "should not be considered a medical diagnosis."
    )



# DIABETES PAGE
elif page == "Diabetes":
    st.subheader("🩸 Diabetes Risk Assessment")

    col1, col2 = st.columns(2)

    with col1:
        pregnancies = st.number_input("Pregnancies", 0, 20, 1)
        glucose = st.number_input("Glucose Level", 0, 300, 120)
        bp = st.number_input("Blood Pressure", 0, 200, 70)
        skin = st.number_input("Skin Thickness", 0, 100, 20)

    with col2:
        insulin = st.number_input("Insulin Level", 0, 900, 80)
        bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
        dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
        age = st.number_input("Age", 1, 120, 30)

    if st.button("🔍 Predict Diabetes Risk", use_container_width=True):
        pred, prob = predict_diabetes(
            [pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]
        )

        st.markdown("---")
        st.metric("Risk Probability", f"{prob * 100:.2f}%")
        st.info(risk_message(prob))



# HEART DISEASE PAGE
elif page == "Heart Disease":
    st.subheader("❤️ Heart Disease Risk Assessment")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", 1, 120, 45)
        sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
        cp = st.number_input("Chest Pain Type (0–3)", 0, 3, 1)
        trestbps = st.number_input("Resting BP", 80, 200, 120)
        chol = st.number_input("Cholesterol", 100, 600, 200)

    with col2:
        fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
        restecg = st.number_input("Rest ECG (0–2)", 0, 2, 1)
        thalach = st.number_input("Max Heart Rate", 60, 220, 150)
        exang = st.selectbox("Exercise Induced Angina", [0, 1])

    with col3:
        oldpeak = st.number_input("ST Depression", 0.0, 6.0, 1.0)
        slope = st.number_input("Slope (0–2)", 0, 2, 1)
        ca = st.number_input("Major Vessels (0–3)", 0, 3, 0)
        thal = st.number_input("Thalassemia (0–3)", 0, 3, 1)

    if st.button("🔍 Predict Heart Disease Risk", use_container_width=True):
        pred, prob = predict_heart([
            age, sex, cp, trestbps, chol,
            fbs, restecg, thalach, exang,
            oldpeak, slope, ca, thal
        ])

        st.markdown("---")
        st.metric("Risk Probability", f"{prob * 100:.2f}%")
        st.info(risk_message(prob))



# LIVER DISEASE PAGE
elif page == "Liver Disease":
    st.subheader("🧪 Liver Disease Risk Assessment")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 1, 120, 40)
        gender = st.selectbox("Gender", [1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
        tb = st.number_input("Total Bilirubin", 0.0, 30.0, 1.0)
        db = st.number_input("Direct Bilirubin", 0.0, 10.0, 0.3)

    with col2:
        alkphos = st.number_input("Alkaline Phosphotase", 50, 3000, 200)
        sgpt = st.number_input("SGPT", 0, 2000, 30)
        sgot = st.number_input("SGOT", 0, 2000, 35)
        tp = st.number_input("Total Proteins", 2.0, 10.0, 6.5)
        alb = st.number_input("Albumin", 1.0, 6.0, 3.5)
        agr = st.number_input("Albumin/Globulin Ratio", 0.1, 3.0, 1.0)

    if st.button("🔍 Predict Liver Disease Risk", use_container_width=True):
        pred, prob = predict_liver(
            [age, gender, tb, db, alkphos, sgpt, sgot, tp, alb, agr]
        )

        st.markdown("---")
        st.metric("Risk Probability", f"{prob * 100:.2f}%")
        st.info(risk_message(prob))



# Footer
st.markdown("---")
st.caption("⚕️ Built with Machine Learning | Educational & Decision-Support Use Only")
