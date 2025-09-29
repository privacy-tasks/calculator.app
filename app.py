import streamlit as st

# Streamlit app title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮")
st.title("🧮 Simple Calculator")

# User input
num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number", value=0.0, format="%.2f")

# Operation selection
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation
result = None
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Error: Cannot divide by zero.")

# Show result
if result is not None:
    st.success(f"Result: {result}")
