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

# Add custom CSS
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
        .tile {
            background-color: #f1f1f1;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            margin-bottom: 15px;
            transition: transform 0.2s;
        }
        .tile:hover {
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation with tiles
st.sidebar.title("Navigation")

nav_options = {
    "Prediction": "🔍 Prediction",
    "Visualize Data": "📊 Visualize Data",
    "Analyze Data": "🛰️ Analyze Data",
    "Insights": "💡 Insights",
    "About": "ℹ️ About"
}

selected_page = st.sidebar.selectbox(
    "Go to", 
    options=list(nav_options.keys()),
    index=0,
    format_func=lambda x: nav_options[x],
    help="Scroll through to select the page."
)

# Load page based on selection
if selected_page == "Prediction":
    st.markdown(
        "<h1 style='text-align: center; color: #4280f5; font-weight: bold;'>Heart Disease Prediction Web App</h1>", 
        unsafe_allow_html=True
    )
    st.image("heart.jpg", use_column_width=True)  # Replace with your image path

    # Sidebar images
    st.sidebar.image("AI.jpg", use_column_width=True)  # Add another image

    # Sidebar for user input
    st.sidebar.header("Input Features")
    
    
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

    # Optionally, add a detailed explanation or note
    st.markdown(
    """
    <div class="prediction-result" style="
        background-color: #2c3e50;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        color: #ecf0f1;
    ">
        <h4 style="color: #1abc9c;">Important Note:</h4>
        <p>This prediction is based on the model's analysis of your health data. It should not replace professional medical advice. Always consult with a healthcare provider for personalized advice and further evaluation.</p>
    </div>
    """, unsafe_allow_html=True
)


    # Add footer or additional content
    st.markdown(
        """
        <footer class='custom-footer' style='text-align: center; padding: 10px; margin-top: 30px;'>
            Handcrafted by <strong>Devanik</strong> | <em>2024</em>
        </footer>
        """, unsafe_allow_html=True
    )
    # Add Credits with selectbox and scroll feature
credits_option = st.sidebar.selectbox(
    "More Info",
    ["📜 Credits", "🤝 Acknowledgments", "📧 Contact"],
    index=0,
    format_func=lambda x: x,
    help="Select to view more details."
)


# Conditional display based on selectbox choice
if credits_option == "Credits":
    st.sidebar.markdown(
        """
        <div style="overflow-y: auto; max-height: 500px; border-top: 2px solid #ddd; margin-top: 20px; padding-top: 10px;">
            <h5 style="color: #888;">Credits</h5>
            <p>Developed by <a href="https://www.linkedin.com/in/devanik/" target="_blank" style="color: #1e90ff; text-decoration: none;"><strong>Devanik</strong></a> | AI Enthusiast & Data Scientist</p>
        </div>
        """, unsafe_allow_html=True
    )
elif credits_option == "Acknowledgments":
    st.sidebar.markdown(
        """
        <div style="overflow-y: auto; max-height: 500px; border-top: 2px solid #ddd; margin-top: 20px; padding-top: 10px;">
            <h5 style="color: #888;">Acknowledgments</h5>
            <p>Special thanks to the mentors who have supported me to grasp ML concepts.</p>
        </div>
        """, unsafe_allow_html=True
    )
elif credits_option == "Contact":
    st.sidebar.markdown(
        """
        <div style="overflow-y: auto; max-height: 500px; border-top: 2px solid #ddd; margin-top: 20px; padding-top: 10px;">
            <h5 style="color: #888;">Contact</h5>
            <p>For inquiries, reach out to <a href="mailto:devanik2005@gmail.com" style="color: #1e90ff; text-decoration: none;"><strong>Devanik</strong></a> at <a href="mailto:devanik2005@gmail.com">devanik@example.com</a></p>
        </div>
        """, unsafe_allow_html=True
    )
    # Add a third image to the sidebar
    st.sidebar.image("AI_heart.jpg", use_column_width=True)  # Add a third image
    




elif selected_page == "Visualize Data":
    # Code for Visualize Data page
    st.title("Visualize Data")
    st.write("Data visualization content goes here...")

elif selected_page == "Analyze Data":
    # Code for Analyze Data page
    st.title("Analyze Data")
    st.write("Data analysis content goes here...")

elif selected_page == "Insights":
    # Code for Insights page
    st.title("Insights")
    st.write("Insights content goes here...")

elif selected_page == "About":
    # Code for About page
    st.title("About")
    st.write("Information about the app goes here...")


   
