import streamlit as st

def about_page():
    st.header("About")
    st.write("""
        This Heart Disease Prediction Web App is designed to help users understand their risk of heart disease
        based on various health factors. It uses a machine learning model to predict the likelihood of heart disease.
        However, please note that this tool is not a substitute for professional medical advice.
    """)
    st.subheader("How It Works")
    st.write("""
        The prediction model was trained on a dataset containing various health metrics like age, cholesterol levels, and more.
        Users can input their data, and the model will output the likelihood of having heart disease.
    """)
    st.subheader("Contact")
    st.write("For any inquiries, please contact us at example@example.com.")
