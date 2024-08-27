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

    # Additional Visualizations

    # 1. Boxplot for Outliers
    st.subheader("Boxplot for Outliers")
    boxplot_column = st.selectbox("Select a column for Boxplot", numeric_df.columns)
    if boxplot_column:
        fig, ax = plt.subplots()
        sns.boxplot(x=numeric_df[boxplot_column], ax=ax)
        st.pyplot(fig)

# 2. Pairplot for Feature Relationships
st.subheader("Pairplot for Feature Relationships")
pairplot_columns = st.multiselect("Select columns for Pairplot", numeric_df.columns, default=numeric_df.columns[:3])

if len(pairplot_columns) > 1:
    pairplot_df = numeric_df[pairplot_columns]
    if not pairplot_df.empty:
        fig = sns.pairplot(pairplot_df)
        st.pyplot(fig)


    # 3. Violin Plot for Data Distribution
    st.subheader("Violin Plot for Data Distribution")
    violinplot_column = st.selectbox("Select a column for Violin Plot", numeric_df.columns)
    if violinplot_column:
        fig, ax = plt.subplots()
        sns.violinplot(x=numeric_df[violinplot_column], ax=ax)
        st.pyplot(fig)

    # 4. Count Plot for Categorical Data
    st.subheader("Count Plot for Categorical Data")
    categorical_columns = df.select_dtypes(include=['object']).columns
    countplot_column = st.selectbox("Select a categorical column for Count Plot", categorical_columns)
    if countplot_column:
        fig, ax = plt.subplots()
        sns.countplot(x=df[countplot_column], ax=ax)
        st.pyplot(fig)

    # 5. Scatter Plot for Two Variables
    st.subheader("Scatter Plot for Two Variables")
    scatter_x = st.selectbox("Select X-axis for Scatter Plot", numeric_df.columns, index=0)
    scatter_y = st.selectbox("Select Y-axis for Scatter Plot", numeric_df.columns, index=1)
    if scatter_x and scatter_y:
        fig, ax = plt.subplots()
        sns.scatterplot(x=numeric_df[scatter_x], y=numeric_df[scatter_y], ax=ax)
        st.pyplot(fig)

# Example usage with a sample DataFrame
# df = pd.read_csv('your_dataset.csv')
# visualize_page(df)
