import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def display(df):
    st.header("Visualize Data")
    st.write("Use the visualizations below to explore the dataset.")
    
    # Example visualization
    st.subheader("Correlation Heatmap")
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', square=True, linewidths=.5)
    st.pyplot(plt)
    
    st.subheader("Distribution of Age")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], kde=True)
    st.pyplot(plt)
