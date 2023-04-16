import streamlit as st

def largest(num1, num2, num3):
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    return largest

st.title("Number Comparison App")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

if st.button("Find the largest number"):
    largest = largest(num1, num2, num3)
    st.write("The largest number is:", largest)
