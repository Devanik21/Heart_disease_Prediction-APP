import streamlit as st

def about_page():
    st.header("About This App 🔍")
    
    st.write("""
        Welcome to the **Heart Disease Prediction Web App**. This application is designed to assist users in understanding their risk of heart disease based on various health metrics.
        
        **⚙️ How It Works:**
        This app leverages a sophisticated machine learning model that has been trained on a comprehensive dataset containing a range of health metrics such as age, cholesterol levels, blood pressure, and more. By inputting your health information into the app, the model evaluates and predicts the likelihood of heart disease, offering valuable insights to help manage your health.

        **🔍 Features:**
        - **Interactive Visualizations:** Explore data distributions and relationships through dynamic visualizations.
        - **Advanced Data Analysis:** Gain insights from detailed statistical analyses and correlation studies.
        - **User-Friendly Interface:** Easily input your health metrics and view predictions in real-time.

        **🚀 Disclaimer:**
        While this tool provides useful predictions based on the input data, it is important to remember that the results are not a substitute for professional medical advice. Always consult with a healthcare professional for personalized guidance and diagnosis.

        **🔗 Contact Us:**
        For any inquiries or further information, please connect with me on [LinkedIn](https://www.linkedin.com/in/devanik/).
    """)

    # Add a section with visual elements
    st.subheader("📈 How the Model Works")
    st.write("""
        The heart disease prediction model uses a combination of features to estimate the risk of heart disease. The key steps in the process include:
        
        - **Data Preprocessing:** The dataset is cleaned and preprocessed to handle missing values and normalize features.
        - **Model Training:** Several machine learning algorithms are trained on the preprocessed data to find the best-performing model.
        - **Prediction:** The trained model uses new input data to predict the likelihood of heart disease based on historical patterns.
        
        ![Model Flowchart](https://example.com/flowchart.png)  # Replace with a real image URL or path

    """)

    # Add a section for user engagement
    st.subheader("📩 Stay Updated")
    st.write("""
        Subscribe to our newsletter to receive updates on new features, health tips, and more! [Subscribe Here](https://example.com/subscribe)  # Replace with a real subscription link
    """)

    # Add a section for acknowledgments
    st.subheader("🙌 Acknowledgments")
    st.write("""
        We would like to thank the contributors and developers who made this tool possible. Special thanks to the open-source community for providing resources and support.
    """)

# Example usage
# about_page()
