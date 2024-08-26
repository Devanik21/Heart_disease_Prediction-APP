import streamlit as st

def analyze_page(df):
    st.header("Analyze Data")
    st.write("Perform data analysis here.")
    
    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Missing Data")
    st.write(df.isnull().sum())
    
    st.subheader("Data Types")
    st.write(df.dtypes)
