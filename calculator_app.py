import streamlit as st

# Define a function for addition
def add(x, y):
    return x + y

# Define a function for subtraction
def subtract(x, y):
    return x - y

# Define a function for multiplication
def multiply(x, y):
    return x * y

# Define a function for division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# Streamlit UI
st.title("Simple Calculator")

operation = st.selectbox("Select operation", ("Addition", "Subtraction", "Multiplication", "Division"))

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

if operation == "Addition":
    result = add(num1, num2)
elif operation == "Subtraction":
    result = subtract(num1, num2)
elif operation == "Multiplication":
    result = multiply(num1, num2)
elif operation == "Division":
    result = divide(num1, num2)

if st.button("Calculate"):
    st.success(f"Result: {result}")
