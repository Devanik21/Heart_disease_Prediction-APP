import streamlit as st
import pandas as pd
import joblib

# Import other modules
import visualize
import analyze
import insights
import about

# Set custom Streamlit theme
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Prediction", "Visualize Data", "Analyze Data", "Insights", "About"])

# Load the dataset and model
df = pd.read_csv("Heart_Disease_Prediction.csv")
model = joblib.load("RF_heart_disease_model.pkl")

# Custom CSS
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        h1 {
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .custom-footer {
            color: #666;
            font-size: 0.9em;
        }
        .prediction-result {
            background-color: #e7f2ff;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
        .prediction-result h4 {
            color: #0f57a3;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Images
st.markdown("<h1 style='text-align: center; color: #4280f5; font-weight: bold;'>Heart Disease Prediction Web App</h1>", unsafe_allow_html=True)
st.image("heart.jpg", use_column_width=True)  # Replace with your image path

# Conditional rendering based on the selected page
if page == "Prediction":
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

    if prediction[0] == 'Warning ! Anomaly  detected in your heart.':
        st.error("⚠️ Warning: Anomaly detected in your heart. There is a risk of heart disease.")
    else:
        st.success("😊 You are safe. No significant risk of heart disease detected.")

    # Add a detailed explanation or note
    st.markdown("""
        <div class="prediction-result">
            <h4>Important Note:</h4>
            <p>This prediction is based on the model's analysis of your health data. It should not replace professional medical advice. Always consult with a healthcare provider for personalized advice and further evaluation.</p>
        </div>
    """, unsafe_allow_html=True)

elif page == "Visualize Data":
    visualize.display(df)

elif page == "Analyze Data":
    analyze.display(df)

elif page == "Insights":
    insights.display(df)

elif page == "About":
    about.display()

# Add footer
st.markdown("""
    <footer class='custom-footer' style='text-align: center; padding: 10px; margin-top: 30px;'>
        Handcrafted by <strong>Devanik</strong> | <em>2024</em>
    </footer>
""", unsafe_allow_html=True)

st.sidebar.image("AI_heart.jpg", use_column_width=True)
