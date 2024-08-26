import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_page(df):
    # Ensure the correct data types for numeric columns
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df['Cholesterol'] = pd.to_numeric(df['Cholesterol'], errors='coerce')
    df.dropna(subset=['Age', 'Cholesterol'], inplace=True)
    
    # Filter to include only numeric columns
    numeric_df = df.select_dtypes(include=['number'])
    
    st.title("Visualize Data")
    st.write("Explore the visualizations of the heart disease dataset.")

    st.subheader("Distribution of Ages")
    fig, ax = plt.subplots()
    sns.histplot(numeric_df['Age'], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("Distribution of Cholesterol Levels")
    fig, ax = plt.subplots()
    sns.histplot(numeric_df['Cholesterol'], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots()
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
    st.pyplot(fig)
