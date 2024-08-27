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
    summary_stat = st.selectbox(
        "Select summary statistics to display",
        ["Basic Statistics", "All Statistics"]
    )
    
    if summary_stat == "Basic Statistics":
        st.write(df.describe())
    else:
        st.write(df.describe(include='all'))

    # Missing Data Visualization
    st.subheader("Missing Data Analysis")
    missing_data = df.isnull().sum()
    st.write(missing_data)

    if missing_data.sum() > 0:
        colormap = st.selectbox(
            "Choose color map for missing data heatmap",
            ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
        )
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.isnull(), cbar=False, cmap=colormap, ax=ax)
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
        corr_columns = st.multiselect(
            "Select columns for correlation heatmap",
            numeric_df.columns,
            default=numeric_df.columns
        )
        
        if corr_columns:
            corr = numeric_df[corr_columns].corr()
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax, linewidths=1, linecolor='black')
            ax.set_title('Correlation Heatmap', fontsize=16)
            st.pyplot(fig)
        else:
            st.write("No columns selected for correlation analysis.")
    else:
        st.write("No numeric columns available for correlation analysis.")

    # Interactive Analysis: Select and Analyze Columns
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
            
            # Optionally show unique value counts
            if st.checkbox(f"Show unique value counts for {col}"):
                st.write(df[col].value_counts())

    # Distribution of Numeric Columns
    st.subheader("Distribution of Numeric Columns")
    numeric_columns = numeric_df.columns
    dist_column = st.selectbox("Select a column to view its distribution", numeric_columns)
    
    if dist_column:
        bins = st.slider("Select number of bins for histogram", min_value=10, max_value=100, value=30)
        kde = st.checkbox("Show KDE plot", value=True)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(df[dist_column], bins=bins, kde=kde, color='mediumseagreen', edgecolor='black', ax=ax)
        ax.set_title(f'Distribution of {dist_column}', fontsize=16)
        ax.set_xlabel(f'{dist_column}', fontsize=14)
        ax.set_ylabel('Frequency', fontsize=14)
        st.pyplot(fig)

# Example usage with a sample DataFrame
# df = pd.read_csv('your_dataset.csv')
# analyze_page(df)
