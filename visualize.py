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
    
    # Set the global seaborn style
    sns.set_theme(style="whitegrid", context="talk")
    
    st.title("Advanced Data Visualization")
    st.write("Explore the visualizations of the heart disease dataset with advanced features.")

    # Let the user choose the column to visualize
    selected_column = st.selectbox("Select a column to visualize", numeric_df.columns)

    if selected_column:
        st.subheader(f"Distribution of {selected_column}")
        
        # Slider for bins and checkbox for KDE
        bins = st.slider("Select number of bins", min_value=10, max_value=50, value=30)
        kde = st.checkbox("Overlay Kernel Density Estimate (KDE)", value=True)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(numeric_df[selected_column], bins=bins, kde=kde, ax=ax, color='mediumseagreen', edgecolor='black')
        ax.set_facecolor('whitesmoke')
        ax.set_title(f'Distribution of {selected_column}', fontsize=16)
        ax.set_xlabel(f'{selected_column}', fontsize=14)
        ax.set_ylabel('Frequency', fontsize=14)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        st.pyplot(fig)

    st.subheader("Correlation Heatmap")
    # Allow users to select columns and color palette for correlation heatmap
    selected_columns = st.multiselect("Select columns for correlation heatmap", numeric_df.columns, default=numeric_df.columns.tolist())
    cmap_option = st.selectbox("Select Heatmap Color Palette", options=['coolwarm', 'viridis', 'magma', 'Spectral'], index=0)

    if selected_columns:
        fig, ax = plt.subplots(figsize=(16, 12))
        corr = numeric_df[selected_columns].corr()
        sns.heatmap(corr, annot=True, fmt='.2f', cmap=cmap_option, ax=ax, linewidths=1, linecolor='black')
        ax.set_facecolor('whitesmoke')
        ax.set_title('Correlation Heatmap', fontsize=16)
        st.pyplot(fig)

    # Additional Visualizations

    # 1. Boxplot for Outliers
    st.subheader("Boxplot for Outliers")
    boxplot_column = st.selectbox("Select a column for Boxplot", numeric_df.columns)
    if boxplot_column:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(x=numeric_df[boxplot_column], ax=ax, palette='muted', fliersize=5, linewidth=2)
        ax.set_facecolor('whitesmoke')
        ax.set_title(f'Boxplot of {boxplot_column}', fontsize=16)
        ax.set_xlabel(f'{boxplot_column}', fontsize=14)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        st.pyplot(fig)

    # 2. Violin Plot for Data Distribution
    st.subheader("Violin Plot for Data Distribution")
    violinplot_column = st.selectbox("Select a column for Violin Plot", numeric_df.columns)
    if violinplot_column:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.violinplot(x=numeric_df[violinplot_column], ax=ax, palette='deep', linewidth=2)
        ax.set_facecolor('whitesmoke')
        ax.set_title(f'Violin Plot of {violinplot_column}', fontsize=16)
        ax.set_xlabel(f'{violinplot_column}', fontsize=14)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        st.pyplot(fig)

    # 3. Count Plot for Categorical Data
    st.subheader("Count Plot for Categorical Data")
    categorical_columns = df.select_dtypes(include=['object']).columns
    countplot_column = st.selectbox("Select a categorical column for Count Plot", categorical_columns)
    if countplot_column:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(x=df[countplot_column], ax=ax, palette='Set2', edgecolor='black')
        ax.set_facecolor('whitesmoke')
        ax.set_title(f'Count Plot of {countplot_column}', fontsize=16)
        ax.set_xlabel(f'{countplot_column}', fontsize=14)
        ax.set_ylabel('Count', fontsize=14)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        st.pyplot(fig)

    # 4. Scatter Plot for Two Variables
    st.subheader("Scatter Plot for Two Variables")
    scatter_x = st.selectbox("Select X-axis for Scatter Plot", numeric_df.columns, index=0)
    scatter_y = st.selectbox("Select Y-axis for Scatter Plot", numeric_df.columns, index=1)
    scatter_hue = st.selectbox("Select a column for color (hue) in Scatter Plot", options=[None] + list(numeric_df.columns), index=0)
    
    if scatter_x and scatter_y:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x=numeric_df[scatter_x], y=numeric_df[scatter_y], ax=ax, hue=numeric_df[scatter_hue] if scatter_hue else None, palette='cool', s=100, edgecolor='black')
        ax.set_facecolor('whitesmoke')
        ax.set_title(f'Scatter Plot of {scatter_x} vs {scatter_y}', fontsize=16)
        ax.set_xlabel(f'{scatter_x}', fontsize=14)
        ax.set_ylabel(f'{scatter_y}', fontsize=14)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        st.pyplot(fig)
    
    # 5. Pair Plot for Multi-Variable Relationships
    st.subheader("Pair Plot for Multi-Variable Relationships")
    pairplot_columns = st.multiselect("Select columns for Pair Plot", numeric_df.columns, default=numeric_df.columns[:4].tolist())
    if pairplot_columns:
        pairplot_hue = st.selectbox("Select a column for color (hue) in Pair Plot", options=[None] + list(df.columns), index=0)
        pairplot_kind = st.selectbox("Select the type of plot in Pair Plot", options=['scatter', 'reg', 'kde'], index=0)
        
        if pairplot_hue:
            sns.pairplot(df[pairplot_columns], hue=pairplot_hue, palette='coolwarm', kind=pairplot_kind)
        else:
            sns.pairplot(df[pairplot_columns], kind=pairplot_kind)
        st.pyplot(plt)

# Example usage with a sample DataFrame
# df = pd.read_csv('your_dataset.csv')
# visualize_page(df)
