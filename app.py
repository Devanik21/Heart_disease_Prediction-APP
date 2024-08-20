import streamlit as st
import pandas as pd
import joblib

# Load the dataset
df = pd.read_csv("Heart_Disease_Prediction.csv")  # Adjust the path if necessary

# Load the trained model (adjust the path to where your model is saved)
model = joblib.load("RF_heart_disease_model.pkl")  # Replace with your actual model path

# Title of the web app
st.title("Heart Disease Prediction Web App")

# Sidebar for user input
st.sidebar.header("Input Features")

def user_input_features():
    # Adjust sliders for each feature with practical ranges
    features = {}
    features['Age'] = st.sidebar.slider("Age", 0, 100, 50)
    features['Sex'] = st.sidebar.selectbox("Sex", [0, 1], index=0)  # 0: Female, 1: Male
    features['Chest pain type'] = st.sidebar.slider("Chest pain type", 1, 4, 3)
    features['BP'] = st.sidebar.slider("BP", 80, 200, 130)  # Blood pressure
    features['Cholesterol'] = st.sidebar.slider("Cholesterol", 100, 400, 200)
    features['FBS over 120'] = st.sidebar.selectbox("FBS over 120", [0, 1], index=0)  # 0: <120, 1: >120
    features['EKG results'] = st.sidebar.slider("EKG results", 0, 2, 1)
    features['Max HR'] = st.sidebar.slider("Max HR", 60, 200, 150)
    features['Exercise angina'] = st.sidebar.selectbox("Exercise angina", [0, 1], index=0)  # 0: No, 1: Yes
    features['ST depression'] = st.sidebar.slider("ST depression", 0.0, 6.2, 1.0)
    features['Slope of ST'] = st.sidebar.slider("Slope of ST", 1, 3, 2)
    features['Number of vessels fluro'] = st.sidebar.slider("Number of vessels fluro", 0, 3, 1)
    features['Thallium'] = st.sidebar.slider("Thallium", 3, 7, 3)
    
    input_df = pd.DataFrame(features, index=[0])
    return input_df

# Get user input
input_df = user_input_features()

# Display user input
st.subheader('User Input Features')
st.write(input_df)

# Make prediction
prediction = model.predict(input_df)

# Display the prediction result
st.subheader('Prediction Result')

# Customize the prediction message
if prediction[0] == 'Warning ! Anomaly  detected in your heart.':
    st.error("⚠️ Warning - there is a risk of heart disease!")
else:
    st.success("😊 You are safe. There is no significant risk of heart disease.")

# Optionally, you can add more details or a description below the result
st.markdown("""
<div style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
    <strong>Note:</strong> The prediction is based on the model's analysis of health factors. 
    Please consult a healthcare professional for personalized advice.
</div>
""", unsafe_allow_html=True)
