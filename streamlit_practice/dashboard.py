import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Title
st.title("📊 Real-Time Sales Performance")

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Options")
region = st.sidebar.multiselect(
    "Select Regions:",
    options=["North", "South", "East", "West"],
    default=["North", "South", "East", "West"]
)

target_goal = st.sidebar.slider("Half-Year Target ($)", 100000, 1000000, 250000)

# --- DATA GENERATION (Simulated) ---
# Simulating a dataset based on selected regions
np.random.seed(42)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
data = {"Month": months}

for r in region:
    data[r] = np.random.randint(10000, 25000, size=6)

df = pd.DataFrame(data)
df.set_index("Month", inplace=True)

# --- MAIN DASHBOARD ---
# Layout: 2 Key Metrics at the top
total_sales = df.sum().sum() if not df.empty else 0

metric_col1, metric_col2 = st.columns(2)
with metric_col1:
    st.metric(label="Total Sales Overall", value=f"${total_sales:,}")
with metric_col2:
    status = "Target Met 🎉" if total_sales >= target_goal else "Below Target 📉"
    st.metric(label="Target Status", value=status, delta=f"{total_sales - target_goal:,}")

st.markdown("---")

# Layout: Chart and Table side-by-side
if not df.empty:
    chart_col, table_col = st.columns([2, 1]) # 2:1 width ratio
    
    with chart_col:
        st.subheader("Sales Trends by Region")
        st.line_chart(df)
        
    with table_col:
        st.subheader("Raw Figures")
        st.dataframe(df)
else:
    st.warning("Please select at least one region in the sidebar to view data.")