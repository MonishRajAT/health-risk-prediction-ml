# 🩺 Intelligent Health Risk Prediction System

This project is an **AI-powered healthcare risk prediction web application** built using **Machine Learning and Streamlit**.  
It allows users to estimate the **risk of Diabetes, Heart Disease, and Liver Disease** by entering basic clinical and lifestyle parameters.

The aim of this project is to demonstrate how machine learning models can be trained, deployed, and used in a clean, user-friendly web application to solve real-world problems.

> ⚠️ This application is intended for **educational and decision-support purposes only** and should not be considered a medical diagnosis.

---

## 🚀 About the Project

Healthcare data is complex, and interpreting medical parameters is not always straightforward for non-experts.  
This project tries to bridge that gap by providing a simple interface where users can input health details and instantly receive a **risk estimate with clear interpretation**.

The application follows a complete **end-to-end machine learning workflow**, starting from data preprocessing and model training to deployment through a web interface.

---

## Diseases Covered

The system currently supports risk prediction for:

- 🩸 **Diabetes**
- ❤️ **Heart Disease**
- 🧪 **Liver Disease**

Each disease is handled using a **separate machine learning model**, making the system modular and easy to extend in the future.

---

## ⚙️ How the Application Works

1. The user selects a disease from the sidebar.
2. Relevant health parameters are entered through the form.
3. A trained machine learning model processes the inputs.
4. The application displays:
   - A **risk probability**
   - A **simple risk interpretation** (Low / Moderate / High)

The entire prediction happens in real time.

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit** for the web interface
- **Scikit-learn** for machine learning models
- **Pandas & NumPy** for data processing
- **Joblib** for saving and loading trained models

---

## Machine Learning Approach

- **Algorithm Used**: Random Forest Classifier  
- **Reason for Choosing Random Forest**:
  - Works well with structured medical data
  - Handles non-linear relationships effectively
  - Provides stable performance without heavy tuning

- **Evaluation Focus**:
  - Special importance was given to **recall**
  - In healthcare applications, missing a disease case is more critical than false alarms

---

## Application Features

- Clean and intuitive user interface
- Dedicated **Home page** explaining the project and navigation
- Sidebar-based navigation for ease of use
- Separate prediction pages for each disease
- Real-time prediction results
- Clear and understandable risk messages

---
