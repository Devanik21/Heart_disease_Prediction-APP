import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def insights_page():
    st.header("🔍 Key Insights & Analysis")
    st.write("Discover the key insights from the dataset with vibrant visualizations and detailed analysis.")

    # Insight 1: Age Distribution
    st.subheader("📊 Insight 1: Age Distribution")
    st.write("The age distribution provides insights into the population most affected by heart disease.")

    # Plot the distribution of age with vibrant colors
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['Age'].dropna(), bins=30, kde=True, color='royalblue', edgecolor='white', ax=ax)
    ax.set_facecolor('aliceblue')
    ax.set_title('Age Distribution of Patients', fontsize=18, color='darkblue')
    ax.set_xlabel('Age', fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    st.pyplot(fig)

    # Detailed statistics
    age_mean = df['Age'].mean()
    age_median = df['Age'].median()
    age_mode = df['Age'].mode()[0]
    st.write(f"**Age Statistics:**")
    st.write(f"- **Mean Age:** {age_mean:.2f} years")
    st.write(f"- **Median Age:** {age_median} years")
    st.write(f"- **Most Common Age:** {age_mode} years")

    # Insight 2: Cholesterol Levels
    st.subheader("💔 Insight 2: Cholesterol Levels")
    st.write("Cholesterol levels are a major factor in heart disease risk. Here's how they are distributed.")

    # Plot the distribution of cholesterol levels
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['Cholesterol'].dropna(), bins=30, kde=True, color='tomato', edgecolor='white', ax=ax)
    ax.set_facecolor('mistyrose')
    ax.set_title('Cholesterol Levels of Patients', fontsize=18, color='darkred')
    ax.set_xlabel('Cholesterol Level', fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    st.pyplot(fig)

    # Detailed statistics
    chol_mean = df['Cholesterol'].mean()
    chol_median = df['Cholesterol'].median()
    chol_mode = df['Cholesterol'].mode()[0]
    st.write(f"**Cholesterol Statistics:**")
    st.write(f"- **Mean Cholesterol Level:** {chol_mean:.2f}")
    st.write(f"- **Median Cholesterol Level:** {chol_median}")
    st.write(f"- **Most Common Cholesterol Level:** {chol_mode}")

    # Correlation Analysis
    st.subheader("🔗 Correlation Analysis")
    st.write("Examining the relationship between age and cholesterol levels.")

    # Calculate correlation
    correlation = df[['Age', 'Cholesterol']].corr().iloc[0, 1]
    st.write(f"**Correlation between Age and Cholesterol:** {correlation:.2f}")

    # Scatter plot for correlation
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='Age', y='Cholesterol', data=df, color='darkgreen', edgecolor='white', ax=ax, s=100, alpha=0.7)
    ax.set_facecolor('honeydew')
    ax.set_title('Correlation between Age and Cholesterol Levels', fontsize=18, color='darkgreen')
    ax.set_xlabel('Age', fontsize=14)
    ax.set_ylabel('Cholesterol Level', fontsize=14)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    st.pyplot(fig)

    # Summary
    st.subheader("📈 Summary")
    st.write("These insights shed light on important factors related to heart disease risk. The analysis emphasizes the significance of age and cholesterol levels.")

    # Interactive Widgets for Further Exploration
    st.sidebar.header("🔍 Explore Further")
    st.sidebar.write("Use these options to filter and explore the dataset further.")
    
    min_age, max_age = st.sidebar.slider("Select Age Range", min_value=int(df['Age'].min()), max_value=int(df['Age'].max()), value=(30, 70))
    min_cholesterol, max_cholesterol = st.sidebar.slider("Select Cholesterol Range", min_value=int(df['Cholesterol'].min()), max_value=int(df['Cholesterol'].max()), value=(100, 300))
    
    filtered_df = df[(df['Age'] >= min_age) & (df['Age'] <= max_age) & (df['Cholesterol'] >= min_cholesterol) & (df['Cholesterol'] <= max_cholesterol)]
    st.sidebar.write(f"**Filtered Data Preview:**")
    st.sidebar.write(filtered_df.head())

# Example usage with a sample DataFrame
# df = pd.read_csv('your_dataset.csv')
# insights_page(df)
