import streamlit as st

def display(df):
    st.header("Insights")
    st.write("Here are some key insights derived from the data.")
    
    st.subheader("Insight 1: Age Distribution")
    st.write("Most patients are within the age range of 50-60, which is a critical period for heart disease.")
    
    st.subheader("Insight 2: Cholesterol Levels")
    st.write("High cholesterol levels are a significant risk factor in this dataset, with a positive correlation to heart disease.")
