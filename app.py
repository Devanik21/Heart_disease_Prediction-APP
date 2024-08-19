import streamlit as st
import pandas as pd
import joblib

# Load the dataset
df = pd.read_csv("Heart_Disease_Prediction.csv")

# Load the trained model (adjust the path to where your model is saved)
model = joblib.load("RF_heart_disease_model.pkl")  # Replace with your actual model path

# Title of the web app
st.title("Heart Disease Prediction Web App")

# Sidebar for user input
st.sidebar.header("Input Features")

def user_input_features():
    # Adjust sliders for each feature in the dataset
    features = {}
    for col in df.columns[:-1]:  # Exclude the label column
        min_value = float(df[col].min())
        max_value = float(df[col].max())
        default_value = float(df[col].mean())
        
        features[col] = st.sidebar.slider(f"{col}", min_value, max_value+100, default_value)

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
    st.error("⚠️ Warning - there is a risk of heart disease !")
else:
    st.success("😊You are safe . There is no significant risk of heart disease.")

# Optionally, you can add more details or a description below the result
st.markdown("""
<div style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
    <strong>Note:</strong> The prediction is based on the model's analysis of health factors. 
    Please consult a healthcare professional for personalized advice.
</div>
""", unsafe_allow_html=True)
