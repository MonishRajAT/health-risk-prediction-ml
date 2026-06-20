import streamlit as st
import pandas as pd
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

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="HealthGuard AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

/* Main App */

.stApp{
    background:
    linear-gradient(
    135deg,
    #0f172a,
    #16213e,
    #0f172a
    );
}

/* Page Width */

.block-container{
    max-width:1400px;
    padding-top:2rem;
    padding-bottom:2rem;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#1e2433;
}

/* Sidebar Buttons */

section[data-testid="stSidebar"] button{

    height:65px !important;

    border:none !important;

    border-radius:16px !important;

    margin-bottom:12px !important;

    color:white !important;

    font-size:16px !important;

    font-weight:600 !important;

    background:
    linear-gradient(
    90deg,
    #6d28d9,
    #3b82f6,
    #22c55e
    ) !important;
}

section[data-testid="stSidebar"] button:hover{

    transform:translateY(-2px);

    box-shadow:
    0px 6px 20px rgba(0,0,0,0.35);
}

/* Glass Card */

.glass-card{

    background:
    rgba(255,255,255,0.08);

    backdrop-filter:blur(12px);

    border-radius:20px;

    padding:25px;

    border:
    1px solid rgba(255,255,255,0.12);

    margin-bottom:20px;
}

/* Metric Cards */

.metric-card{

    background:
    rgba(255,255,255,0.08);

    border-radius:20px;

    padding:20px;

    text-align:center;

    border:
    1px solid rgba(255,255,255,0.12);
}

.metric-number{

    font-size:3rem;

    text-align:center;
}

.metric-label{

    color:white;

    font-size:1rem;

    font-weight:600;
}

/* Disease Cards */

.disease-card{

    background:
    linear-gradient(
    135deg,
    rgba(109,40,217,0.15),
    rgba(59,130,246,0.15),
    rgba(34,197,94,0.15)
    );

    border-radius:20px;

    padding:25px;

    border:
    1px solid rgba(255,255,255,0.1);

    min-height:250px;
}

.disease-card:hover{

    transform:translateY(-5px);
}

/* Headers */

h1,h2,h3,h4{

    color:white !important;
}

p,li{

    color:#cbd5e1;
}

/* Inputs */

label{

    color:white !important;
}

/* Buttons */

.stButton > button{

    width:100%;

    border-radius:12px;

    height:50px;

    font-size:16px;

    font-weight:600;
}

/* Metrics */

[data-testid="metric-container"]{

    background:
    rgba(255,255,255,0.08);

    border-radius:15px;

    padding:15px;

    border:
    1px solid rgba(255,255,255,0.1);
}
            
/* Progress Bar */
            
.stProgress > div > div > div > div{
    background:#38bdf8;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR NAVIGATION
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

st.sidebar.image(
    "logo.png",
    use_container_width=True
)

st.sidebar.markdown("---")

# HOME
if st.sidebar.button(
    "🏠 HOME",
    use_container_width=True
):
    st.session_state.page = "home"

# DIABETES

if st.sidebar.button(
    "🩸 DIABETES",
    use_container_width=True
):
    st.session_state.page = "diabetes"

# HEART

if st.sidebar.button(
    "❤️ HEART DISEASE",
    use_container_width=True
):
    st.session_state.page = "heart"

# LIVER

if st.sidebar.button(
    "🫀 LIVER DISEASE",
    use_container_width=True
):
    st.session_state.page = "liver"

# ABOUT

if st.sidebar.button(
    "ℹ️ ABOUT PROJECT",
    use_container_width=True
):
    st.session_state.page = "about"

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div style="
    text-align:center;
    color:#94a3b8;
    font-size:13px;
    ">

    Version 1.0

    <br><br>

    Machine Learning Powered

    <br>

    Healthcare Decision Support

    </div>
    """,
    unsafe_allow_html=True
)

page = st.session_state.page

# ==================================================
# HOME PAGE
# ==================================================

if page == "home":

    hero_left, hero_right = st.columns([1.5, 1])

    with hero_left:

        st.markdown(
            """
            # 🏥 HealthGuard AI

            ### Intelligent Multi-Disease Risk Assessment Platform

            Predict the risk of Diabetes, Heart Disease and Liver Disease
            using Machine Learning powered healthcare analytics.

            Get instant probability scores, risk categorization
            and personalized health recommendations.
            """
        )

    with hero_right:

        st.info(
            """
            ### AI Healthcare Platform

            ✔ Diabetes Prediction

            ✔ Heart Disease Prediction

            ✔ Liver Disease Prediction

            ✔ Instant Risk Analysis

            ✔ Personalized Recommendations
            """
        )

    st.markdown("---")

    # ==================================================
    # KPI SECTION
    # ==================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div class='metric-card'>
                <div class='metric-number'>🩺</div>
                <div class='metric-label'>3 Diseases</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class='metric-card'>
                <div class='metric-number'>🤖</div>
                <div class='metric-label'>3 ML Models</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class='metric-card'>
                <div class='metric-number'>📈</div>
                <div class='metric-label'>95%+ Accuracy</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """
            <div class='metric-card'>
                <div class='metric-number'>⚡</div>
                <div class='metric-label'>Real-Time</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================================
    # DISEASE MODULES
    # ==================================================

    st.subheader("🩺 Disease Assessment Modules")

    d1, d2, d3 = st.columns(3)

    with d1:

        st.markdown(
            """
            <div class='disease-card'>

            <h2>Diabetes</h2>

            Assess diabetes risk using:

            • Glucose

            • BMI

            • Insulin

            • Blood Pressure

            • Age

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Open Diabetes Assessment",
            key="home_diabetes"
        ):
            st.session_state.page = "diabetes"
            st.rerun()

    with d2:

        st.markdown(
            """
            <div class='disease-card'>

            <h2>Heart Disease</h2>

            Assess heart disease risk using:

            • Cholesterol

            • ECG Results

            • Heart Rate

            • Chest Pain Type

            • Blood Pressure

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Open Heart Assessment",
            key="home_heart"
        ):
            st.session_state.page = "heart"
            st.rerun()

    with d3:

        st.markdown(
            """
            <div class='disease-card'>

            <h2>Liver Disease</h2>

            Assess liver disease risk using:

            • Bilirubin

            • SGOT

            • SGPT

            • Albumin

            • Protein Levels

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Open Liver Assessment",
            key="home_liver"
        ):
            st.session_state.page = "liver"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================================
    # ABOUT PLATFORM
    # ==================================================

    left, right = st.columns(2)

    with left:

        st.markdown(
            """
            <div class='glass-card'>

            <h2>🚀 About HealthGuard AI</h2>

            HealthGuard AI is a Machine Learning
            powered healthcare platform that helps
            users assess disease risks through
            predictive analytics.

            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        st.markdown(
            """
            <div class='glass-card'>

            <h2>⚙️ How It Works</h2>

            1. Select a disease module

            2. Enter health parameters

            3. Run AI prediction

            4. View risk score

            5. Get recommendations

            </div>
            """,
            unsafe_allow_html=True
        )

    st.warning(
        "⚠️ This platform is intended for educational purposes only and should not replace professional medical advice."
    )

# ==================================================
# DIABETES PAGE
# ==================================================

elif page == "diabetes":

    st.title("🩸 Diabetes Risk Assessment")

    st.markdown(
        """
        Assess diabetes risk using patient information
        and clinical health parameters.
        """
    )

    left_col, right_col = st.columns([1, 1])

    with left_col:

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

        predict_btn = st.button(
            "🔍 Analyze Diabetes Risk",
            use_container_width=True
        )

    with right_col:

        st.markdown("### 📊 Assessment Result")

        if predict_btn:

            prediction, probability = predict_diabetes([
                pregnancies,
                glucose,
                bp,
                skin,
                insulin,
                bmi,
                dpf,
                age
            ])

            risk_percent = round(probability * 100, 2)

            metric1, metric2 = st.columns(2)

            with metric1:
                st.metric(
                    "Risk Score",
                    f"{risk_percent}%"
                )

            with metric2:
                st.metric(
                    "Prediction",
                    "Positive" if prediction == 1 else "Negative"
                )

            st.markdown("---")

            st.subheader("Risk Probability")

            st.progress(float(probability))

            if probability < 0.3:

                st.success("🟢 Low Risk")

                risk_level = "Low"

            elif probability < 0.6:

                st.warning("🟡 Moderate Risk")

                risk_level = "Moderate"

            else:

                st.error("🔴 High Risk")

                risk_level = "High"

            st.info(
                f"Risk Level: {risk_level}"
            )

            st.info(
                risk_message(probability)
            )

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=risk_percent,
                    title={
                        "text": "Diabetes Risk (%)"
                    },
                    gauge={
                        "axis": {
                            "range": [0, 100]
                        },
                        "bar": {
                            "color": "#38bdf8",
                            "thickness": 0.25
                        },
                        "steps": [
                            {
                                "range": [0, 30],
                                "color": "green"
                            },
                            {
                                "range": [30, 60],
                                "color": "orange"
                            },
                            {
                                "range": [60, 100],
                                "color": "red"
                            }
                        ]
                    }
                )
            )

            fig.update_layout(
                height=350,
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white")
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.markdown("### 💡 Recommendations")

            if probability < 0.3:

                st.success(
                    """
                    • Maintain healthy diet

                    • Exercise regularly

                    • Continue annual health checkups
                    """
                )

            elif probability < 0.6:

                st.warning(
                    """
                    • Reduce sugar intake

                    • Increase physical activity

                    • Monitor glucose levels
                    """
                )

            else:

                st.error(
                    """
                    • Consult a healthcare professional

                    • Monitor blood glucose frequently

                    • Follow a diabetes-friendly diet

                    • Seek medical evaluation
                    """
                )

        else:

            st.info(
                "Enter patient details and click Analyze Diabetes Risk."
            )

# ==================================================
# HEART DISEASE PAGE
# ==================================================

elif page == "heart":

    st.title("❤️ Heart Disease Risk Assessment")

    st.markdown(
        """
        Assess cardiovascular disease risk using
        patient information and cardiac parameters.
        """
    )

    left_col, right_col = st.columns([1, 1])

    with left_col:

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
            format_func=lambda x: "Female" if x == 0 else "Male",
            key="heart_gender"
        )

        cp = st.selectbox(
            "Chest Pain Type",
            [0, 1, 2, 3],
            key="heart_cp"
        )

        trestbps = st.number_input(
            "Resting Blood Pressure",
            min_value=80,
            max_value=250,
            value=120,
            key="heart_bp"
        )

        st.markdown("### ❤️ Cardiac Parameters")

        chol = st.number_input(
            "Cholesterol",
            min_value=100,
            max_value=700,
            value=200,
            key="heart_chol"
        )

        fbs = st.selectbox(
            "Fasting Blood Sugar > 120",
            [0, 1],
            key="heart_fbs"
        )

        restecg = st.selectbox(
            "Rest ECG",
            [0, 1, 2],
            key="heart_ecg"
        )

        thalach = st.number_input(
            "Maximum Heart Rate",
            min_value=60,
            max_value=250,
            value=150,
            key="heart_rate"
        )

        exang = st.selectbox(
            "Exercise Induced Angina",
            [0, 1],
            key="heart_exang"
        )

        oldpeak = st.number_input(
            "ST Depression",
            min_value=0.0,
            max_value=10.0,
            value=1.0,
            key="heart_oldpeak"
        )

        slope = st.selectbox(
            "Slope",
            [0, 1, 2],
            key="heart_slope"
        )

        ca = st.selectbox(
            "Major Vessels",
            [0, 1, 2, 3],
            key="heart_ca"
        )

        thal = st.selectbox(
            "Thalassemia",
            [0, 1, 2, 3],
            key="heart_thal"
        )

        predict_btn = st.button(
            "🔍 Analyze Heart Disease Risk",
            use_container_width=True
        )

    with right_col:

        st.markdown("### 📊 Assessment Result")

        if predict_btn:

            prediction, probability = predict_heart([
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

            risk_percent = round(probability * 100, 2)

            metric1, metric2 = st.columns(2)

            with metric1:
                st.metric(
                    "Risk Score",
                    f"{risk_percent}%"
                )

            with metric2:
                st.metric(
                    "Prediction",
                    "Positive" if prediction == 1 else "Negative"
                )

            st.markdown("---")

            st.subheader("Risk Probability")

            st.progress(float(probability))

            if probability < 0.3:

                st.success("🟢 Low Risk")

                risk_level = "Low"

            elif probability < 0.6:

                st.warning("🟡 Moderate Risk")

                risk_level = "Moderate"

            else:

                st.error("🔴 High Risk")

                risk_level = "High"

            st.info(
                f"Risk Level: {risk_level}"
            )

            st.info(
                risk_message(probability)
            )

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=risk_percent,
                    title={
                        "text": "Heart Disease Risk (%)"
                    },
                    gauge={
                        "axis": {
                            "range": [0, 100]
                        },
                        "bar": {
                            "color": "#38bdf8",
                            "thickness": 0.25
                        },
                        "steps": [
                            {
                                "range": [0, 30],
                                "color": "green"
                            },
                            {
                                "range": [30, 60],
                                "color": "orange"
                            },
                            {
                                "range": [60, 100],
                                "color": "red"
                            }
                        ]
                    }
                )
            )

            fig.update_layout(
                height=350,
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white")
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.markdown("### 💡 Recommendations")

            if probability < 0.3:

                st.success(
                    """
                    • Maintain healthy cholesterol levels

                    • Exercise regularly

                    • Continue annual health checkups
                    """
                )

            elif probability < 0.6:

                st.warning(
                    """
                    • Monitor blood pressure regularly

                    • Reduce saturated fats

                    • Increase physical activity
                    """
                )

            else:

                st.error(
                    """
                    • Consult a cardiologist

                    • Monitor cardiovascular health

                    • Follow medical advice

                    • Seek immediate evaluation
                    """
                )

        else:

            st.info(
                "Enter patient details and click Analyze Heart Disease Risk."
            )

# ==================================================
# LIVER DISEASE PAGE
# ==================================================

elif page == "liver":

    st.title("🫀 Liver Disease Risk Assessment")

    st.markdown(
        """
        Assess liver disease risk using
        patient information and liver function parameters.
        """
    )

    left_col, right_col = st.columns([1, 1])

    with left_col:

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
            format_func=lambda x: "Male" if x == 1 else "Female",
            key="liver_gender"
        )

        st.markdown("### 🧪 Liver Function Parameters")

        tb = st.number_input(
            "Total Bilirubin",
            min_value=0.0,
            max_value=30.0,
            value=1.0,
            key="liver_tb"
        )

        db = st.number_input(
            "Direct Bilirubin",
            min_value=0.0,
            max_value=10.0,
            value=0.3,
            key="liver_db"
        )

        alkphos = st.number_input(
            "Alkaline Phosphotase",
            min_value=50,
            max_value=3000,
            value=200,
            key="liver_alk"
        )

        sgpt = st.number_input(
            "SGPT",
            min_value=0,
            max_value=2000,
            value=30,
            key="liver_sgpt"
        )

        sgot = st.number_input(
            "SGOT",
            min_value=0,
            max_value=2000,
            value=35,
            key="liver_sgot"
        )

        tp = st.number_input(
            "Total Proteins",
            min_value=2.0,
            max_value=10.0,
            value=6.5,
            key="liver_tp"
        )

        alb = st.number_input(
            "Albumin",
            min_value=1.0,
            max_value=6.0,
            value=3.5,
            key="liver_alb"
        )

        agr = st.number_input(
            "Albumin / Globulin Ratio",
            min_value=0.1,
            max_value=3.0,
            value=1.0,
            key="liver_agr"
        )

        predict_btn = st.button(
            "🔍 Analyze Liver Disease Risk",
            use_container_width=True
        )

    with right_col:

        st.markdown("### 📊 Assessment Result")

        if predict_btn:

            prediction, probability = predict_liver([
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

            risk_percent = round(probability * 100, 2)

            metric1, metric2 = st.columns(2)

            with metric1:
                st.metric(
                    "Risk Score",
                    f"{risk_percent}%"
                )

            with metric2:
                st.metric(
                    "Prediction",
                    "Positive" if prediction == 1 else "Negative"
                )

            st.markdown("---")

            st.subheader("Risk Probability")

            st.progress(float(probability))

            if probability < 0.3:

                st.success("🟢 Low Risk")

                risk_level = "Low"

            elif probability < 0.6:

                st.warning("🟡 Moderate Risk")

                risk_level = "Moderate"

            else:

                st.error("🔴 High Risk")

                risk_level = "High"

            st.info(
                f"Risk Level: {risk_level}"
            )

            st.info(
                risk_message(probability)
            )

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=risk_percent,
                    title={
                        "text": "Liver Disease Risk (%)"
                    },
                    gauge={
                        "axis": {
                            "range": [0, 100]
                        },
                        "bar": {
                            "color": "#38bdf8",
                            "thickness": 0.25
                        },
                        "steps": [
                            {
                                "range": [0, 30],
                                "color": "green"
                            },
                            {
                                "range": [30, 60],
                                "color": "orange"
                            },
                            {
                                "range": [60, 100],
                                "color": "red"
                            }
                        ]
                    }
                )
            )

            fig.update_layout(
                height=350,
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white")
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.markdown("### 💡 Recommendations")

            if probability < 0.3:

                st.success(
                    """
                    • Maintain a healthy diet

                    • Stay physically active

                    • Continue routine health checkups
                    """
                )

            elif probability < 0.6:

                st.warning(
                    """
                    • Reduce processed foods

                    • Monitor liver health regularly

                    • Improve lifestyle habits
                    """
                )

            else:

                st.error(
                    """
                    • Consult a liver specialist

                    • Monitor liver function tests

                    • Follow medical advice

                    • Seek professional evaluation
                    """
                )

        else:

            st.info(
                "Enter patient details and click Analyze Liver Disease Risk."
            )

# ==================================================
# ABOUT PAGE
# ==================================================

elif page == "about":

    st.title("ℹ️ About HealthGuard AI")

    st.markdown(
        """
        HealthGuard AI is an AI-powered healthcare
        decision support platform designed to assess
        disease risk using Machine Learning models.
        """
    )

    st.markdown("---")

    # ==========================================
    # PROJECT OVERVIEW
    # ==========================================

    st.markdown(
        """
        <div class='glass-card'>

        <h2>🏥 Project Overview</h2>

        HealthGuard AI is a multi-disease prediction
        platform that helps users assess the likelihood
        of various health conditions using predictive
        Machine Learning models.

        The platform currently supports:

        • Diabetes Risk Prediction

        • Heart Disease Risk Prediction

        • Liver Disease Risk Prediction

        • Probability-Based Risk Assessment

        • Personalized Recommendations

        </div>
        """,
        unsafe_allow_html=True
    )

    # ==========================================
    # TECHNOLOGY STACK
    # ==========================================

    st.subheader("⚙️ Technology Stack")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Language",
            "Python"
        )

    with col2:
        st.metric(
            "Frontend",
            "Streamlit"
        )

    with col3:
        st.metric(
            "ML Library",
            "Scikit-Learn"
        )

    with col4:
        st.metric(
            "Visualization",
            "Plotly"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================
    # DISEASE MODULES
    # ==========================================

    st.subheader("🩺 Supported Disease Modules")

    d1, d2, d3 = st.columns(3)

    with d1:

        st.markdown(
            """
            <div class='disease-card'>

            <h2>Diabetes</h2>

            Uses:

            • Glucose

            • BMI

            • Insulin

            • Blood Pressure

            • Age

            </div>
            """,
            unsafe_allow_html=True
        )

    with d2:

        st.markdown(
            """
            <div class='disease-card'>

            <h2>Heart Disease</h2>

            Uses:

            • Cholesterol

            • ECG Results

            • Heart Rate

            • Chest Pain

            • Blood Pressure

            </div>
            """,
            unsafe_allow_html=True
        )

    with d3:

        st.markdown(
            """
            <div class='disease-card'>

            <h2>Liver Disease</h2>

            Uses:

            • Bilirubin

            • SGPT

            • SGOT

            • Albumin

            • Protein Levels

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================
    # MODEL DETAILS
    # ==========================================

    st.markdown(
        """
        <div class='glass-card'>

        <h2>🤖 Machine Learning Models</h2>

        Random Forest Classifier was selected
        because it provides:

        ✔ High Prediction Accuracy

        ✔ Better Generalization

        ✔ Reduced Overfitting

        ✔ Probability-Based Outputs

        ✔ Robust Performance on Medical Data

        </div>
        """,
        unsafe_allow_html=True
    )

    # ==========================================
    # PROJECT WORKFLOW
    # ==========================================

    st.markdown(
        """
        <div class='glass-card'>

        <h2>⚙️ System Workflow</h2>

        User Inputs

        ↓

        Data Processing

        ↓

        Random Forest Model

        ↓

        Probability Calculation

        ↓

        Risk Classification

        ↓

        Health Recommendations

        </div>
        """,
        unsafe_allow_html=True
    )

    # ==========================================
    # FEATURES
    # ==========================================

    st.markdown(
        """
        <div class='glass-card'>

        <h2>✨ Key Features</h2>

        ✅ Multi-Disease Prediction

        ✅ Interactive Dashboard

        ✅ Risk Probability Analysis

        ✅ AI-Powered Recommendations

        ✅ Real-Time Predictions

        ✅ Modern User Interface

        </div>
        """,
        unsafe_allow_html=True
    )

    # ==========================================
    # PROJECT STATS
    # ==========================================

    st.subheader("📊 Project Statistics")

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.metric(
            "Diseases",
            "3"
        )

    with s2:
        st.metric(
            "Models",
            "3"
        )

    with s3:
        st.metric(
            "Features",
            "30+"
        )

    with s4:
        st.metric(
            "Predictions",
            "Instant"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.success(
        "🚀 HealthGuard AI combines Machine Learning and Healthcare Analytics to provide intelligent disease risk assessment."
    )

    st.warning(
        "⚠️ This application is intended for educational purposes only and should not replace professional medical diagnosis."
    )