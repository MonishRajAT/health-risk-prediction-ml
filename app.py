import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from src.prediction import (
    predict_diabetes,
    predict_heart,
    predict_liver
)

from src.utils import (
    risk_message,
    risk_color
)

# PAGE CONFIG
st.set_page_config(
    page_title="HealthGuard AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CUSTOM CSS
st.markdown("""
<style>

/* Main Background */
.stApp{
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e293b 50%,
        #0f172a 100%
    );
}

/* Remove default padding */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1400px;
}

/* Main Title */
.main-title{
    text-align:center;
    font-size:3.5rem;
    font-weight:700;
    color:white;
    margin-bottom:0;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:1.2rem;
    margin-bottom:2rem;
}

/* Glass Card */
.glass-card{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.15);

    border-radius:20px;
    padding:25px;
    margin-bottom:20px;

    transition:0.3s;
}

.glass-card:hover{
    transform:translateY(-5px);
}

/* KPI Cards */
.metric-card{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border-radius:18px;
    padding:20px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.12);
}

.metric-number{
    color:#38bdf8;
    font-size:2rem;
    font-weight:bold;
}

.metric-label{
    color:white;
    font-size:1rem;
}

/* Disease Cards */
.disease-card{
    background: rgba(255,255,255,0.08);
    border-radius:20px;
    padding:25px;
    border:1px solid rgba(255,255,255,0.12);
    text-align:center;
}

.disease-title{
    color:white;
    font-size:1.5rem;
    font-weight:600;
}

.disease-text{
    color:#cbd5e1;
}

/* Result Card */
.result-card{
    border-radius:20px;
    padding:25px;
    text-align:center;
    color:white;
    font-weight:bold;
    font-size:1.2rem;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#111827;
}

/* Headers */
h1,h2,h3,h4{
    color:white !important;
}

p,li{
    color:#e2e8f0;
}

/* Input labels */
label{
    color:white !important;
}

/* Buttons */
.stButton>button{
    width:100%;
    border-radius:12px;
    height:50px;
    font-size:18px;
    font-weight:600;

    background:#0ea5e9;
    color:white;

    border:none;
}

.stButton>button:hover{
    background:#0284c7;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.markdown("# 🏥 HealthGuard AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🩸 Diabetes",
        "❤️ Heart Disease",
        "🫀 Liver Disease",
        "ℹ️ About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    AI Powered Health Risk Assessment

    ✔ Diabetes Prediction

    ✔ Heart Disease Prediction

    ✔ Liver Disease Prediction

    Built using Machine Learning
    """
)


# DASHBOARD PAGE
if page == "🏠 Dashboard":

    # Hero Section

    st.markdown("""
    <div style='text-align:center;padding:30px;'>

    <h1 class='main-title'>
    🏥 HealthGuard AI
    </h1>

    <p class='subtitle'>
    Intelligent Multi-Disease Risk Assessment Platform
    <br>
    Powered by Machine Learning
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # KPI CARDS
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-number'>3</div>
            <div class='metric-label'>Diseases</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-number'>3</div>
            <div class='metric-label'>ML Models</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-number'>95%+</div>
            <div class='metric-label'>Accuracy</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-number'>30+</div>
            <div class='metric-label'>Health Features</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ABOUT SECTION
    st.markdown("""
    <div class='glass-card'>

    <h2>🚀 About HealthGuard AI</h2>

    HealthGuard AI is an intelligent healthcare decision-support platform
    that predicts disease risks using Machine Learning models trained on
    real-world medical datasets.

    The platform currently supports:

    ✔ Diabetes Risk Prediction

    ✔ Heart Disease Risk Prediction

    ✔ Liver Disease Risk Prediction

    Users can enter clinical parameters and instantly receive
    a risk probability score along with health recommendations.

    </div>
    """, unsafe_allow_html=True)

    # DISEASE CARDS
    st.markdown("## 🩺 Disease Assessment Modules")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='disease-card'>

        <div class='disease-title'>
        🩸 Diabetes
        </div>

        <br>

        <div class='disease-text'>
        Assess diabetes risk using glucose,
        BMI, insulin levels and other
        clinical indicators.
        </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='disease-card'>

        <div class='disease-title'>
        ❤️ Heart Disease
        </div>

        <br>

        <div class='disease-text'>
        Evaluate cardiovascular risk
        using patient health parameters
        and cardiac indicators.
        </div>

        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='disease-card'>

        <div class='disease-title'>
        🫀 Liver Disease
        </div>

        <br>

        <div class='disease-text'>
        Predict liver disease risk
        using biochemical and
        diagnostic markers.
        </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # FEATURES SECTION
    st.markdown("""
    <div class='glass-card'>

    <h2>✨ Key Features</h2>

    ✅ Machine Learning Powered Predictions

    ✅ Instant Risk Assessment

    ✅ Multi-Disease Support

    ✅ Interactive Dashboard

    ✅ Healthcare Analytics

    ✅ User-Friendly Interface

    ✅ Real-Time Prediction Results

    </div>
    """, unsafe_allow_html=True)

    # WORKFLOW SECTION
    st.markdown("""
    <div class='glass-card'>

    <h2>⚙️ How It Works</h2>

    1️⃣ Select a disease prediction module

    2️⃣ Enter clinical health parameters

    3️⃣ Run AI-powered prediction

    4️⃣ Receive risk probability score

    5️⃣ View personalized recommendations

    </div>
    """, unsafe_allow_html=True)

    # DISCLAIMER
    st.warning(
        "⚠️ This platform is intended for educational and decision-support purposes only and should not replace professional medical advice."
    )


# DIABETES PAGE
elif page == "🩸 Diabetes":

    st.markdown("""
    <h1 style='text-align:center;'>
    🩸 Diabetes Risk Assessment
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='glass-card'>
    Predict diabetes risk using clinical and diagnostic parameters.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # INPUT SECTIONS
    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 👤 Patient Information")

        pregnancies = st.number_input(
            "Pregnancies",
            min_value=0,
            max_value=20,
            value=1
        )

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=30
        )

        bmi = st.number_input(
            "BMI",
            min_value=0.0,
            max_value=70.0,
            value=25.0
        )

        dpf = st.number_input(
            "Diabetes Pedigree Function",
            min_value=0.0,
            max_value=3.0,
            value=0.5
        )

    with col2:

        st.markdown("### 🧪 Clinical Parameters")

        glucose = st.number_input(
            "Glucose Level",
            min_value=0,
            max_value=300,
            value=120
        )

        bp = st.number_input(
            "Blood Pressure",
            min_value=0,
            max_value=200,
            value=70
        )

        skin = st.number_input(
            "Skin Thickness",
            min_value=0,
            max_value=100,
            value=20
        )

        insulin = st.number_input(
            "Insulin Level",
            min_value=0,
            max_value=900,
            value=80
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # PREDICT BUTTON
    if st.button(
        "🔍 Analyze Diabetes Risk",
        use_container_width=True
    ):

        pred, prob = predict_diabetes([
            pregnancies,
            glucose,
            bp,
            skin,
            insulin,
            bmi,
            dpf,
            age
        ])

        risk_percent = round(prob * 100, 2)

        st.markdown("---")

        # KPI RESULTS
        r1, r2, r3 = st.columns(3)

        with r1:
            st.metric(
                "Risk Score",
                f"{risk_percent}%"
            )

        with r2:
            st.metric(
                "Prediction",
                "Positive" if pred == 1 else "Negative"
            )

        with r3:
            if prob < 0.3:
                st.metric(
                    "Risk Level",
                    "Low"
                )
            elif prob < 0.6:
                st.metric(
                    "Risk Level",
                    "Moderate"
                )
            else:
                st.metric(
                    "Risk Level",
                    "High"
                )

        st.markdown("<br>", unsafe_allow_html=True)

        # PROGRESS BAR
        st.markdown("### 📊 Risk Probability")

        st.progress(float(prob))

        st.write(f"Risk Probability: **{risk_percent}%**")

        st.markdown("<br>", unsafe_allow_html=True)

        # RESULT CARD
        if prob < 0.3:

            st.success(
                "🟢 Low Risk Detected"
            )

        elif prob < 0.6:

            st.warning(
                "🟡 Moderate Risk Detected"
            )

        else:

            st.error(
                "🔴 High Risk Detected"
            )

        st.info(
            risk_message(prob)
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # RECOMMENDATIONS
        st.markdown("""
        <div class='glass-card'>
        <h3>💡 Health Recommendations</h3>
        </div>
        """, unsafe_allow_html=True)

        if prob < 0.3:

            st.markdown("""
            ✅ Maintain healthy diet

            ✅ Continue regular exercise

            ✅ Monitor health annually

            ✅ Maintain healthy BMI
            """)

        elif prob < 0.6:

            st.markdown("""
            ⚠ Reduce sugar intake

            ⚠ Increase physical activity

            ⚠ Monitor glucose regularly

            ⚠ Maintain balanced nutrition
            """)

        else:

            st.markdown("""
            🚨 Consult a healthcare professional

            🚨 Monitor blood glucose frequently

            🚨 Follow a diabetes-friendly diet

            🚨 Begin lifestyle intervention immediately

            🚨 Seek medical evaluation
            """)

        # RISK GAUGE
        st.markdown("### 🎯 Risk Gauge")

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_percent,
            title={'text': "Diabetes Risk (%)"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "red"},
                'steps': [
                    {'range': [0, 30], 'color': "green"},
                    {'range': [30, 60], 'color': "orange"},
                    {'range': [60, 100], 'color': "red"}
                ]
            }
        ))

        fig.update_layout(
            height=400,
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# HEART DISEASE PAGE
elif page == "❤️ Heart Disease":

    st.markdown("""
    <h1 style='text-align:center;'>
    ❤️ Heart Disease Risk Assessment
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='glass-card'>
    Assess cardiovascular disease risk using clinical and cardiac parameters.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # INPUTS
    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### 👤 Patient Information")

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=45,
            key="heart_age"
        )

        sex = st.selectbox(
            "Gender",
            [0, 1],
            format_func=lambda x: "Female" if x == 0 else "Male"
        )

        cp = st.selectbox(
            "Chest Pain Type",
            [0, 1, 2, 3]
        )

        trestbps = st.number_input(
            "Resting Blood Pressure",
            min_value=80,
            max_value=250,
            value=120
        )

    with col2:

        st.markdown("### ❤️ Cardiac Parameters")

        chol = st.number_input(
            "Cholesterol",
            min_value=100,
            max_value=700,
            value=200
        )

        fbs = st.selectbox(
            "Fasting Blood Sugar > 120",
            [0, 1]
        )

        restecg = st.selectbox(
            "Rest ECG",
            [0, 1, 2]
        )

        thalach = st.number_input(
            "Maximum Heart Rate",
            min_value=60,
            max_value=250,
            value=150
        )

    with col3:

        st.markdown("### 🧪 Diagnostic Parameters")

        exang = st.selectbox(
            "Exercise Induced Angina",
            [0, 1]
        )

        oldpeak = st.number_input(
            "ST Depression",
            min_value=0.0,
            max_value=10.0,
            value=1.0
        )

        slope = st.selectbox(
            "Slope",
            [0, 1, 2]
        )

        ca = st.selectbox(
            "Major Vessels",
            [0, 1, 2, 3]
        )

        thal = st.selectbox(
            "Thalassemia",
            [0, 1, 2, 3]
        )

    st.markdown("<br>", unsafe_allow_html=True)


    # PREDICTION
    if st.button(
        "🔍 Analyze Heart Disease Risk",
        use_container_width=True
    ):

        pred, prob = predict_heart([
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        ])

        risk_percent = round(prob * 100, 2)

        st.markdown("---")

        # KPI METRICS
        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric(
                "Risk Score",
                f"{risk_percent}%"
            )

        with m2:
            st.metric(
                "Prediction",
                "Positive" if pred == 1 else "Negative"
            )

        with m3:

            if prob < 0.3:
                level = "Low"

            elif prob < 0.6:
                level = "Moderate"

            else:
                level = "High"

            st.metric(
                "Risk Level",
                level
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # PROGRESS BAR
        st.markdown("### 📊 Risk Probability")

        st.progress(float(prob))

        st.write(
            f"Heart Disease Risk Probability: **{risk_percent}%**"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # ALERTS
        if prob < 0.3:

            st.success(
                "🟢 Low Cardiovascular Risk"
            )

        elif prob < 0.6:

            st.warning(
                "🟡 Moderate Cardiovascular Risk"
            )

        else:

            st.error(
                "🔴 High Cardiovascular Risk"
            )

        st.info(
            risk_message(prob)
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # RECOMMENDATIONS
        st.markdown("""
        <div class='glass-card'>
        <h3>💡 Cardiac Health Recommendations</h3>
        </div>
        """, unsafe_allow_html=True)

        if prob < 0.3:

            st.markdown("""
            ✅ Continue regular physical activity

            ✅ Maintain healthy cholesterol levels

            ✅ Follow a balanced diet

            ✅ Annual health checkups
            """)

        elif prob < 0.6:

            st.markdown("""
            ⚠ Reduce saturated fat intake

            ⚠ Monitor blood pressure regularly

            ⚠ Increase aerobic exercise

            ⚠ Improve dietary habits
            """)

        else:

            st.markdown("""
            🚨 Consult a cardiologist

            🚨 Monitor cardiovascular health

            🚨 Follow prescribed treatment plans

            🚨 Reduce cardiovascular risk factors

            🚨 Seek medical evaluation immediately
            """)

        # HEART RISK GAUGE
        st.markdown("### 🎯 Cardiac Risk Gauge")

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_percent,
            title={"text": "Heart Disease Risk (%)"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "red"},
                "steps": [
                    {"range": [0, 30], "color": "green"},
                    {"range": [30, 60], "color": "orange"},
                    {"range": [60, 100], "color": "red"}
                ]
            }
        ))

        fig.update_layout(
            height=400,
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# LIVER DISEASE PAGE
elif page == "🫀 Liver Disease":

    st.markdown("""
    <h1 style='text-align:center;'>
    🫀 Liver Disease Risk Assessment
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='glass-card'>
    Assess liver disease risk using biochemical and diagnostic health parameters.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # INPUT SECTION
    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 👤 Patient Information")

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=40,
            key="liver_age"
        )

        gender = st.selectbox(
            "Gender",
            [1, 0],
            format_func=lambda x: "Male" if x == 1 else "Female"
        )

        tb = st.number_input(
            "Total Bilirubin",
            min_value=0.0,
            max_value=30.0,
            value=1.0
        )

        db = st.number_input(
            "Direct Bilirubin",
            min_value=0.0,
            max_value=10.0,
            value=0.3
        )

        alkphos = st.number_input(
            "Alkaline Phosphotase",
            min_value=50,
            max_value=3000,
            value=200
        )

    with col2:

        st.markdown("### 🧪 Liver Function Parameters")

        sgpt = st.number_input(
            "SGPT",
            min_value=0,
            max_value=2000,
            value=30
        )

        sgot = st.number_input(
            "SGOT",
            min_value=0,
            max_value=2000,
            value=35
        )

        tp = st.number_input(
            "Total Proteins",
            min_value=2.0,
            max_value=10.0,
            value=6.5
        )

        alb = st.number_input(
            "Albumin",
            min_value=1.0,
            max_value=6.0,
            value=3.5
        )

        agr = st.number_input(
            "Albumin / Globulin Ratio",
            min_value=0.1,
            max_value=3.0,
            value=1.0
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # PREDICTION BUTTON
    if st.button(
        "🔍 Analyze Liver Disease Risk",
        use_container_width=True
    ):

        pred, prob = predict_liver([
            age,
            gender,
            tb,
            db,
            alkphos,
            sgpt,
            sgot,
            tp,
            alb,
            agr
        ])

        risk_percent = round(prob * 100, 2)

        st.markdown("---")

        # KPI CARDS
        k1, k2, k3 = st.columns(3)

        with k1:
            st.metric(
                "Risk Score",
                f"{risk_percent}%"
            )

        with k2:
            st.metric(
                "Prediction",
                "Positive" if pred == 1 else "Negative"
            )

        with k3:

            if prob < 0.3:
                level = "Low"

            elif prob < 0.6:
                level = "Moderate"

            else:
                level = "High"

            st.metric(
                "Risk Level",
                level
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # PROGRESS BAR
        st.markdown("### 📊 Risk Probability")

        st.progress(float(prob))

        st.write(
            f"Liver Disease Risk Probability: **{risk_percent}%**"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # ALERTS
        if prob < 0.3:

            st.success(
                "🟢 Low Liver Disease Risk"
            )

        elif prob < 0.6:

            st.warning(
                "🟡 Moderate Liver Disease Risk"
            )

        else:

            st.error(
                "🔴 High Liver Disease Risk"
            )

        st.info(
            risk_message(prob)
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # RECOMMENDATIONS
        st.markdown("""
        <div class='glass-card'>
        <h3>💡 Liver Health Recommendations</h3>
        </div>
        """, unsafe_allow_html=True)

        if prob < 0.3:

            st.markdown("""
            ✅ Maintain healthy eating habits

            ✅ Stay hydrated

            ✅ Exercise regularly

            ✅ Periodic health monitoring
            """)

        elif prob < 0.6:

            st.markdown("""
            ⚠ Reduce processed foods

            ⚠ Monitor liver function regularly

            ⚠ Limit unhealthy dietary habits

            ⚠ Improve overall lifestyle
            """)

        else:

            st.markdown("""
            🚨 Consult a hepatologist immediately

            🚨 Monitor liver enzymes regularly

            🚨 Follow medical guidance

            🚨 Avoid liver stress factors

            🚨 Seek professional evaluation
            """)

        # LIVER RISK GAUGE
        st.markdown("### 🎯 Liver Risk Gauge")

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_percent,
            title={"text": "Liver Disease Risk (%)"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "red"},
                "steps": [
                    {"range": [0, 30], "color": "green"},
                    {"range": [30, 60], "color": "orange"},
                    {"range": [60, 100], "color": "red"}
                ]
            }
        ))

        fig.update_layout(
            height=400,
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ABOUT PAGE
elif page == "ℹ️ About":

    st.markdown("""
    <h1 style='text-align:center;'>
    ℹ️ About HealthGuard AI
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # PROJECT OVERVIEW
    st.markdown("""
    <div class='glass-card'>

    <h2>🏥 Project Overview</h2>

    HealthGuard AI is an intelligent healthcare
    decision-support system that leverages
    Machine Learning models to assess the risk
    of multiple diseases based on patient
    clinical and diagnostic parameters.

    The platform enables users to perform
    quick health risk assessments and receive
    instant probability-based predictions.

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # DISEASE MODULES
    st.markdown("## 🩺 Supported Disease Modules")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class='disease-card'>

        <h3>🩸 Diabetes</h3>

        Predicts diabetes risk using:

        • Glucose

        • BMI

        • Insulin

        • Blood Pressure

        • Age

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class='disease-card'>

        <h3>❤️ Heart Disease</h3>

        Predicts cardiovascular risk using:

        • Cholesterol

        • ECG Results

        • Heart Rate

        • Chest Pain Type

        • Blood Pressure

        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class='disease-card'>

        <h3>🫀 Liver Disease</h3>

        Predicts liver disease risk using:

        • Bilirubin

        • SGOT

        • SGPT

        • Albumin

        • Protein Levels

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # MACHINE LEARNING
    st.markdown("""
    <div class='glass-card'>

    <h2>🤖 Machine Learning Models</h2>

    This project utilizes Random Forest
    Classification models trained on
    healthcare datasets.

    Why Random Forest?

    ✔ High Accuracy

    ✔ Handles Non-Linear Relationships

    ✔ Robust Against Overfitting

    ✔ Works Well With Medical Data

    ✔ Probability-Based Predictions

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)


    # TECHNOLOGY STACK
    st.markdown("""
    <div class='glass-card'>

    <h2>⚙️ Technology Stack</h2>

    🐍 Python

    🎨 Streamlit

    📊 Pandas

    🔢 NumPy

    🤖 Scikit-Learn

    📈 Plotly

    💾 Joblib

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # SYSTEM WORKFLOW
    st.markdown("""
    <div class='glass-card'>

    <h2>🔄 System Workflow</h2>

    User Inputs

    ⬇

    Data Processing

    ⬇

    Random Forest Model

    ⬇

    Risk Probability Calculation

    ⬇

    Risk Classification

    ⬇

    Health Recommendations

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # PROJECT HIGHLIGHTS
    st.markdown("""
    <div class='glass-card'>

    <h2>🚀 Key Highlights</h2>

    ✅ Multi-Disease Prediction Platform

    ✅ Probability-Based Risk Assessment

    ✅ Interactive Modern Dashboard

    ✅ Machine Learning Integration

    ✅ Healthcare Decision Support

    ✅ Real-Time Prediction Engine

    ✅ Recruiter-Friendly Project Design

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # DISCLAIMER
    st.warning(
        """
        ⚠️ Disclaimer:
        This application is intended for educational
        and decision-support purposes only.
        It should not replace professional medical
        diagnosis or treatment.
        """
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # FOOTER
    st.markdown("""
    <div style='text-align:center;'>

    Developed using Machine Learning & Streamlit

    HealthGuard AI © 2026

    </div>
    """, unsafe_allow_html=True)