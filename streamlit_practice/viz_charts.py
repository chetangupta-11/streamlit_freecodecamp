import streamlit as st
import pandas as pd
import numpy as np

st.title("Dynamic Charting")

# Let the user choose how many data points to visualize
num_points = st.slider("Number of data points", 10, 500, 100)

# Generate random data
chart_data = pd.DataFrame(
    np.random.randn(num_points, 4),
    columns=['Metric A', 'Metric B', 'Metric C', 'Metric D']
)

# Show the raw data for reference
st.dataframe(chart_data)  

# Display a native interactive line chart
st.subheader("Line Chart View")
st.line_chart(chart_data)

# Display a native bar chart
st.subheader("Bar Chart View")
st.bar_chart(chart_data)