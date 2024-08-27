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

    # Let the user choose the column to visualize
    selected_column = st.selectbox("Select a column to visualize", numeric_df.columns)

    if selected_column:
        st.subheader(f"Distribution of {selected_column}")
        fig, ax = plt.subplots()
        sns.histplot(numeric_df[selected_column], bins=30, kde=True, ax=ax)
        st.pyplot(fig)

    st.subheader("Correlation Heatmap")
    # Allow users to select columns for correlation heatmap
    selected_columns = st.multiselect("Select columns for correlation heatmap", numeric_df.columns, default=numeric_df.columns.tolist())

    if selected_columns:
        fig, ax = plt.subplots()
        corr = numeric_df[selected_columns].corr()
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
        st.pyplot(fig)

# Example usage with a sample DataFrame
# df = pd.read_csv('your_dataset.csv')
# visualize_page(df)
