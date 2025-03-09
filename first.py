import streamlit as st

st.title("Unit Converter")

# Define conversion factors
conversion_factors = {
    "meters": 1,
    "kilometers": 0.001,
    "centimeters": 100,
    "millimeters": 1000,
    "inches": 39.3701,
    "feet": 3.28084,
    "yards": 1.09361,
    "miles": 0.000621371
}

# User input
value = st.number_input("Enter the value to convert:", min_value=0.0)
from_unit = st.selectbox("Select the unit to convert from:", list(conversion_factors.keys()))
to_unit = st.selectbox("Select the unit to convert to:", list(conversion_factors.keys()))

# Perform conversion
if st.button("Convert"):
    if from_unit != to_unit:
        converted_value = value * (conversion_factors[to_unit] / conversion_factors[from_unit])
        st.success(f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit}")
    else:
        st.warning("Please select different units for conversion.")
