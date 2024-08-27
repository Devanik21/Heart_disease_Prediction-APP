import streamlit as st

def about_page():
    # Header
    st.markdown("<h1 style='text-align: center; color: #1f77b4;'>About This App <span style='font-size: 24px;'>🔍</span></h1>", unsafe_allow_html=True)
    
    st.write("""
        Welcome to the **Heart Disease Prediction Web App**! This tool is designed to help you assess your risk of heart disease based on various health metrics. Dive into your health insights and make informed decisions with our easy-to-use app.

        **How It Works:**
        Our app utilizes a state-of-the-art machine learning model trained on diverse health metrics. By inputting your data, you receive a prediction of your heart disease risk based on the latest research and data science techniques.

        **Features:**
        - 🌟 **Interactive Visualizations:** Engage with dynamic charts to explore data distributions.
        - 📊 **Advanced Data Analysis:** Get detailed statistical insights and correlation studies.
        - 🖥️ **User-Friendly Interface:** Quickly input your health metrics and view predictions.

        **Disclaimer:**
        While this app offers valuable predictions, it should not replace professional medical advice. Always consult a healthcare provider for personalized medical guidance.

        **Contact Us:**
        For questions or further information, connect with me on [LinkedIn](https://www.linkedin.com/in/devanik/).
    """)

    # How the Model Works
    st.markdown("<h2 style='color: #ff7f0e;'>📈 How the Model Works</h2>", unsafe_allow_html=True)
    st.write("""
        The heart disease prediction model involves several steps:
        
        - **Data Preprocessing:** Cleaning and normalizing the dataset.
        - **Model Training:** Using machine learning algorithms to build a predictive model.
        - **Prediction:** Evaluating new data to predict heart disease risk.

     st.image("ML_flowchart.png", caption="Model Flowchart", use_column_width=True)


    # Stay Updated
    st.markdown("<h2 style='color: #2ca02c;'>📩 Stay Updated</h2>", unsafe_allow_html=True)
    st.write("""
        Want to stay in the loop? Subscribe to our newsletter for the latest updates, health tips, and more! [Subscribe Here][LinkedIn](https://www.linkedin.com/in/devanik/) 
    """)

    # Acknowledgments
    st.markdown("<h2 style='color: #d62728;'>🙌 Acknowledgments</h2>", unsafe_allow_html=True)
    st.write("""
        Thank you to my mentors for teaching me machine learning concepts thoroughly. Grateful for the support from the open-source community and developers, we hope to further develop the app.
    """)

# Example usage
# about_page()
