import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
image_path = 'https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png'
st.image(image_path)

st.title("Molar Mass Calculator")
st.subheader("A web application that allows you to quickly determine the mass")


def calculate_mass(concentration, volume, formula_weight):
    mass = concentration * volume * formula_weight
    return mass

# Set up the sidebar inputs
formula_weight = st.sidebar.number_input("Formula Weight (g/mol)")
concentration = st.sidebar.number_input("Concentration ", value=1.0)
# Allow the user to choose the concentration unit

concentration_unit = st.sidebar.radio(
    "Concentration Unit",
    options=["Molar (M)", "Millimolar (mM)", "Micromolar(µM)"],
    index=0  # Default to mol/L
)
volume = st.sidebar.number_input("Volume ", value =1)


# Allow the user to choose the volume unit
volume_unit = st.sidebar.radio("Volume Unit", options=["L", "mL"])



# Convert the volume to liters if the unit is mL
if volume_unit == "mL":
    volume /= 1000

# Convert the concentration to mol/L based on the chosen unit
if concentration_unit == "Millimolar (mM)":
    concentration /= 1000
elif concentration_unit == "Micromolar(µM)":
    concentration /= 1000000

# Calculate the mass
mass = calculate_mass(concentration, volume, formula_weight)
mass2 = round(mass,3)
# Display the result
st.write(f"The required mass is: {mass2} grams.")
