import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_page(df):
    st.header("Advanced Data Analysis")
    st.write("Perform comprehensive data analysis and explore key insights.")

    # Set the global seaborn style
    sns.set_theme(style="whitegrid", context="talk")

    # Data Summary
    st.subheader("Data Summary")
    st.write("Overview of the dataset's basic statistics.")
    st.write(df.describe())

    # Option to display full summary statistics or specific statistics
    if st.checkbox("Show more summary statistics"):
        st.write(df.describe(include='all'))

    # Missing Data Visualization
    st.subheader("Missing Data Analysis")
    missing_data = df.isnull().sum()
    st.write(missing_data)

    if missing_data.sum() > 0:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis', ax=ax)
        ax.set_title('Missing Data Heatmap', fontsize=16)
        st.pyplot(fig)
    else:
        st.write("No missing data in the dataset.")

    # Data Types
    st.subheader("Data Types")
    st.write(df.dtypes)

    # Correlation Analysis
    st.subheader("Correlation Analysis")
    st.write("Explore the correlation between numeric variables.")
    
    # Filter numeric columns
    numeric_df = df.select_dtypes(include=['number'])
    
    if not numeric_df.empty:
        corr = numeric_df.corr()

        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax, linewidths=1, linecolor='black')
        ax.set_title('Correlation Heatmap', fontsize=16)
        st.pyplot(fig)
    else:
        st.write("No numeric columns available for correlation analysis.")

    # Interactive Column Analysis: Select Columns
    st.subheader("Interactive Column Analysis")
    st.write("Select columns to analyze their summary statistics, data types, and unique values.")
    
    selected_columns = st.multiselect("Select columns to analyze", df.columns)
    
    if selected_columns:
        st.write("Summary Statistics:")
        st.write(df[selected_columns].describe())
        st.write("Data Types:")
        st.write(df[selected_columns].dtypes)
        
        for col in selected_columns:
            st.write(f"Unique values in {col}:")
            st.write(df[col].unique())
            
            if pd.api.types.is_numeric_dtype(df[col]):
                st.write(f"Distribution of {col}:")
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.histplot(df[col], bins=30, kde=True, color='mediumseagreen', edgecolor='black')
                ax.set_title(f'Distribution of {col}', fontsize=16)
                ax.set_xlabel(f'{col}', fontsize=14)
                ax.set_ylabel('Frequency', fontsize=14)
                st.pyplot(fig)

    # Distribution of Numeric Columns (Overall)
    st.subheader("Distribution of Numeric Columns")
    numeric_columns = numeric_df.columns
    dist_column = st.selectbox("Select a column to view its distribution", numeric_columns)
    
    if dist_column:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(df[dist_column], bins=30, kde=True, color='mediumseagreen', edgecolor='black')
        ax.set_title(f'Distribution of {dist_column}', fontsize=16)
        ax.set_xlabel(f'{dist_column}', fontsize=14)
        ax.set_ylabel('Frequency', fontsize=14)
        st.pyplot(fig)

    # Additional Analysis Plots

    # Box Plot
    st.subheader("Box Plot")
    box_column = st.selectbox("Select a numeric column for Box Plot", numeric_columns)
    if box_column:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(x=df[box_column], color='lightcoral', ax=ax)
        ax.set_title(f'Box Plot of {box_column}', fontsize=16)
        ax.set_xlabel(f'{box_column}', fontsize=14)
        st.pyplot(fig)

    # Violin Plot
    st.subheader("Violin Plot")
    violin_column = st.selectbox("Select a numeric column for Violin Plot", numeric_columns)
    if violin_column:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.violinplot(x=df[violin_column], color='skyblue', ax=ax)
        ax.set_title(f'Violin Plot of {violin_column}', fontsize=16)
        ax.set_xlabel(f'{violin_column}', fontsize=14)
        st.pyplot(fig)

    # Count Plot
    st.subheader("Count Plot")
    categorical_columns = df.select_dtypes(include=['object']).columns
    count_column = st.selectbox("Select a categorical column for Count Plot", categorical_columns)
    if count_column:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(x=df[count_column], palette='pastel', ax=ax)
        ax.set_title(f'Count Plot of {count_column}', fontsize=16)
        ax.set_xlabel(f'{count_column}', fontsize=14)
        ax.set_ylabel('Count', fontsize=14)
        st.pyplot(fig)

    # Joint Plot
    st.subheader("Joint Plot")
    joint_x = st.selectbox("Select the X column for Joint Plot", numeric_columns)
    joint_y = st.selectbox("Select the Y column for Joint Plot", numeric_columns)
    if joint_x and joint_y:
        fig = plt.figure(figsize=(10, 6))
        sns.jointplot(x=df[joint_x], y=df[joint_y], kind='scatter', color='purple')
        st.pyplot(fig)

    # Bar Plot
    st.subheader("Bar Plot")
    bar_column = st.selectbox("Select a categorical column for Bar Plot", categorical_columns)
    if bar_column:
        bar_data = df[bar_column].value_counts()
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.barplot(x=bar_data.index, y=bar_data.values, palette='viridis', ax=ax)
        ax.set_title(f'Bar Plot of {bar_column}', fontsize=16)
        ax.set_xlabel(f'{bar_column}', fontsize=12)
        ax.set_ylabel('Count', fontsize=14)
        st.pyplot(fig)
