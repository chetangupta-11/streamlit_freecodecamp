import streamlit as st

st.title("Interactive Playground")

# 1. Text Input
user_name = st.text_input("What is your name?", "Stranger")

# 2. Slider (Min, Max, Default)
age = st.slider("Select your age", min_value=0, max_value=100, value=25)

# 3. Selectbox (Dropdown)
role = st.selectbox(
    "What is your primary role?",
    ["Data Scientist", "Developer", "Manager", "Student"]
)

#4 Number Input
height = st.number_input("Enter your height in cm", min_value=50, max_value=250, value=170)

#5 Multiselect (Multiple options)
hobby = st.multiselect(
    "Select your hobbies",
    ["Reading", "Traveling", "Cooking", "Sports", "Gaming"]
)

# 4. A conditional trigger using a Button
if st.button("Generate Summary"):
    st.write(f"### Hello, {height} cm tall amazing {user_name}!")
    st.write(f"You are **{age}** years old and work as a **{role}**.")
    st.write(f"Your hobbies include: {', '.join(hobby)}.")