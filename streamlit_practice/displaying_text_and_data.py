import streamlit as st
import pandas as pd

# 1. App Titles and Headers
st.title("My First Streamlit App 🚀")
st.header("Welcome to the data dashboard")
st.write("This is a simple paragraph explaining what this app does.")

# 2. Displaying Data
st.subheader("Raw Data View")

df = pd.DataFrame({
    'Project Name': ['App Alpha', 'Beta Analytics', 'Gamma Dev'],
    'Budget ($)': [12000, 45000, 23000],
    'Status': ['Completed', 'In Progress', 'In Progress']
})

# st.dataframe makes a beautiful, interactive, sortable table
st.dataframe(df)