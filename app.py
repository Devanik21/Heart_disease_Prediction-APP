import streamlit as st
import pandas as pd
import joblib

# Set custom Streamlit theme
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load the dataset
df = pd.read_csv("Heart_Disease_Prediction.csv")

# Load the trained model
model = joblib.load("RF_heart_disease_model.pkl")

# Add a header image or logo (optional)
st.image("heart.jpg", use_column_width=True)  # Replace with your image path

# Title of the web app with a colorful header
st.markdown(
    "<h1 style='text-align: center; color: #ff4b4b;'>Heart Disease Prediction Web App</h1>", 
    unsafe_allow_html=True
)

# Sidebar for user input
st.sidebar.header("Input Features")
st.sidebar.markdown("Adjust the sliders or select options to input your health data.")

# User input function
def user_input_features():
    features = {
        'Age': st.sidebar.slider("Age", 0, 100, 50),
        'Sex': st.sidebar.selectbox("Sex", ["Female", "Male"], index=0),
        'Chest pain type': st.sidebar.slider("Chest pain type", 1, 4, 3),
        'BP': st.sidebar.slider("Blood Pressure (BP)", 80, 200, 130),
        'Cholesterol': st.sidebar.slider("Cholesterol", 100, 400, 200),
        'FBS over 120': st.sidebar.selectbox("FBS over 120 mg/dl", ["<120", ">120"], index=0),
        'EKG results': st.sidebar.slider("EKG results", 0, 2, 1),
        'Max HR': st.sidebar.slider("Max Heart Rate (HR)", 60, 200, 150),
        'Exercise angina': st.sidebar.selectbox("Exercise-induced Angina", ["No", "Yes"], index=0),
        'ST depression': st.sidebar.slider("ST depression", 0.0, 6.2, 1.0),
        'Slope of ST': st.sidebar.slider("Slope of ST", 1, 3, 2),
        'Number of vessels fluro': st.sidebar.slider("Number of vessels detected by Fluoroscopy", 0, 3, 1),
        'Thallium': st.sidebar.slider("Thallium Stress Test Result", 3, 7, 3)
    }
    
    # Convert categorical features to numerical
    features['Sex'] = 1 if features['Sex'] == "Male" else 0
    features['FBS over 120'] = 1 if features['FBS over 120'] == ">120" else 0
    features['Exercise angina'] = 1 if features['Exercise angina'] == "Yes" else 0
    
    return pd.DataFrame(features, index=[0])

# Get user input
input_df = user_input_features()

# Display user input
st.subheader('User Input Features')
st.write(input_df)

# Make prediction
prediction = model.predict(input_df)

# Display the prediction result with custom messages
st.subheader('Prediction Result')

if prediction[0] == 1:
    st.error("⚠️ Warning: Anomaly detected in your heart. There is a risk of heart disease.")
else:
    st.success("😊 You are safe. No significant risk of heart disease detected.")

# Optionally, add a detailed explanation or note
st.markdown(
    """
    <div style="background-color: #000000; padding: 20px; border-radius: 10px; margin-top: 20px;">
        <h4 style="color: #0f57a3;">Important Note:</h4>
        <p>This prediction is based on the model's analysis of your health data. It should not replace professional medical advice. Always consult with a healthcare provider for personalized advice and further evaluation.</p>
    </div>
    """, unsafe_allow_html=True
)

# Add footer or additional content
st.markdown(
    """
    <footer style='text-align: center; padding: 10px; margin-top: 30px; color: #666;'>
        Powered by <strong>AI </strong> | <em>2024</em>
    </footer>
    """, unsafe_allow_html=True
)
