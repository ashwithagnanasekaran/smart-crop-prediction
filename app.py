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

