import streamlit as st

st.set_page_config(page_title="Smart Crop Prediction", layout="wide")

page = st.sidebar.radio("Navigate", ["Home", "Crop Assessment", "Result"])

if page == "Home":
    st.title("🌱 Smart Crop Prediction System")
    st.subheader("Welcome to the Crop Prediction Application")
    st.write("This system helps predict suitable crops using soil and weather details.")