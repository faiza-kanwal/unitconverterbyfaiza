import streamlit as st

# App title
st.title("Unit Converter")

# Conversion types
conversion_types = ["Length", "Weight", "Temperature"]

# User chooses conversion type
conversion_choice = st.selectbox("Choose conversion type", conversion_types)

# Length Conversion
def convert_length(value, from_unit, to_unit):
    length_conversion = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Inches": 0.0254,
        "Centimeters": 0.01
    }
    if from_unit in length_conversion and to_unit in length_conversion:
        return value * (length_conversion[from_unit] / length_conversion[to_unit])
    return None

if conversion_choice == "Length":
    length_units = ["Meters", "Kilometers", "Feet", "Inches", "Centimeters"]
    input_value = st.number_input("Enter Length value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From unit:", length_units, key="length_from")
    to_unit = st.selectbox("To unit:", length_units, key="length_to")

    if st.button("Convert Length", key="convert_length"):
        result = convert_length(input_value, from_unit, to_unit)
        if result is not None:
            st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')
        else:
            st.error("Invalid conversion.")

# Weight Conversion
def convert_weight(value, from_unit, to_unit):
    weight_conversion = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }
    if from_unit in weight_conversion and to_unit in weight_conversion:
        return value * (weight_conversion[from_unit] / weight_conversion[to_unit])
    return None

if conversion_choice == "Weight":
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    input_value = st.number_input("Enter Weight value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From unit:", weight_units, key="weight_from")
    to_unit = st.selectbox("To unit:", weight_units, key="weight_to")

    if st.button("Convert Weight", key="convert_weight"):
        result = convert_weight(input_value, from_unit, to_unit)
        if result is not None:
            st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')
        else:
            st.error("Invalid conversion.")

# Temperature Conversion
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return None

if conversion_choice == "Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    input_value = st.number_input("Enter Temperature value:", format="%.2f")
    from_unit = st.selectbox("From unit:", temperature_units, key="temp_from")
    to_unit = st.selectbox("To unit:", temperature_units, key="temp_to")

    if st.button("Convert Temperature", key="convert_temp"):
        result = convert_temperature(input_value, from_unit, to_unit)
        if result is not None:
            st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')
        else:
            st.error("Invalid conversion.")