import streamlit as st

st.title("Advanced Layouts")

# 1. Sidebar - Great for global controls and filters
st.sidebar.header("Global Settings")
theme = st.sidebar.radio("Choose App Theme", ["Light Mode", "Dark Mode", "Cyberpunk"])
st.sidebar.write(f"Selected Theme: {theme}")

# 2. Columns - Side-by-side elements
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

with col2:
    st.metric(label="Wind Speed", value="9 mph", delta="-2 mph")

with col3:
    st.metric(label="Humidity", value="86%", delta="5%")

# 3. Tabs - Clean switching between views
tab1, tab2 = st.sidebar.tabs(["Overview", "Deep Dive"])

with tab1:
    st.write("This is the main dashboard overview.")
    
with tab2:
    st.write("Here you would put dense data, logs, or technical specs.")