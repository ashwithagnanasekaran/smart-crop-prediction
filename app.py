import streamlit as st

st.title("🌱 Smart Crop Prediction System")

st.subheader("Enter Soil and Weather Details")

temp = st.slider("Temperature", 0, 50, 25)
humidity = st.slider("Humidity", 0, 100, 60)
rainfall = st.slider("Rainfall", 0, 300, 100)

st.write("Selected Values:")
st.write("Temperature:", temp)
st.write("Humidity:", humidity)
st.write("Rainfall:", rainfall)

if st.button("Predict Crop"):
    st.success("Prediction will be shown here")

st.markdown("### Results Section")

st.set_page_config(page_title="Smart Crop Prediction", layout="wide")

st.title("🌱 Smart Crop Prediction System")

st.sidebar.header("Enter Soil Details")

nitrogen = st.sidebar.number_input("Nitrogen (N)", min_value=0, value=50)
phosphorus = st.sidebar.number_input("Phosphorus (P)", min_value=0, value=50)
potassium = st.sidebar.number_input("Potassium (K)", min_value=0, value=50)
ph = st.sidebar.slider("Soil pH", 0.0, 14.0, 6.5)

import shap
import matplotlib.pyplot as plt

input_data = [nitrogen, phosphorus, potassium, ph]

explainer = shap.Explainer(model)
shap_values = explainer([input_data])

st.subheader("📊 SHAP Explanation")
fig, ax = plt.subplots()
shap.plots.bar(shap_values[0], show=False)
st.pyplot(fig)
