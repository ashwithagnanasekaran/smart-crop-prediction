import streamlit as st
import pandas as pd
import numpy as np
import joblib
import random
import requests
import shap
from datetime import datetime
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# PAGE CONFIG - CLEAN & PROFESSIONAL
st.set_page_config(
    page_title="Smart Crop Rotation System",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CUSTOM CSS - Complete Green Nature Theme
st.markdown("""
    <style>
    /* ========== MAIN BACKGROUND - FRESH FARM FIELD ========== */
    .stApp {
        background: linear-gradient(135deg, 
            #0d2b1f 0%,
            #1a4d2e 50%,
            #0d2b1f 100%
        );
    }
    
    /* Main content area */
    .main > div {
        background: transparent;
    }
    
    /* ========== SIDEBAR - DEEP FOREST THEME ========== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, 
            #0d2b1f 0%,
            #1a4d2e 40%,
            #2d6a4f 70%,
            #1a4d2e 100%
        ) !important;
        border-right: 3px solid #f5c542 !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #fef3c7 !important;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #f5c542 !important;
        border-left: 4px solid #f5c542;
        padding-left: 12px;
    }
    
    [data-testid="stSidebar"] button {
        background: linear-gradient(135deg, #2d6a4f 0%, #40916c 100%) !important;
        border: 1px solid #f5c542 !important;
    }
    
    [data-testid="stSidebar"] button:hover {
        background: linear-gradient(135deg, #40916c 0%, #52b788 100%) !important;
        transform: translateX(5px);
    }
    
    /* ========== INFO CARDS - LIGHT GREEN ========== */
    .info-card {
        background: linear-gradient(135deg, #f0f7e8 0%, #e6f0da 100%);
        border-radius: 20px;
        padding: 24px;
        margin: 16px 0;
        border: 1px solid #a8d08d;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 28px rgba(0,0,0,0.12);
        border-color: #6bb83e;
    }
    
    .info-card::before {
        content: "🌿";
        position: absolute;
        bottom: -10px;
        right: -10px;
        font-size: 60px;
        opacity: 0.1;
    }
    
    .info-card * {
        color: #1a4d2e !important;
    }
    
        st.markdown("### Weather Details")
        st.write("Temperature:", temp)
        st.write("Humidity:", humidity)
        st.write("Rainfall:", rainfall)

    with col2:
        st.markdown("### Soil Details")
        st.write("Nitrogen:", nitrogen)
        st.write("Phosphorus:", phosphorus)
        st.write("Potassium:", potassium)
        st.write("pH:", ph)

    st.session_state["input_data"] = [nitrogen, phosphorus, potassium, ph]

elif page == "Result":
    st.title("📊 Result")

    if "input_data" not in st.session_state:
        st.warning("Please navigate to Crop Assessment page and enter values first.")
    else:
        input_data = st.session_state["input_data"]

        if st.button("Predict Crop"):
            with st.spinner("Predicting crop..."):
                prediction = model.predict([input_data])

            st.success(f"🌾 Predicted Crop: {prediction[0]}")

            st.markdown("### Recommendation")
            st.info(f"The system suggests **{prediction[0]}** based on the current soil values.")

            explainer = shap.Explainer(model)
            shap_values = explainer([input_data])

            st.markdown("---")
            st.markdown("### Explainable AI Analysis")

            st.subheader("📊 SHAP Explanation")
            fig, ax = plt.subplots()
            shap.plots.bar(shap_values[0], show=False)
            st.pyplot(fig)

            st.caption("This chart shows which soil features contributed more to the prediction.")

            st.session_state["history"].append(prediction[0])

            if st.button("Go to Result Page"):
            st.session_state["go_result"] = True
            st.experimental_rerun()

            if any(v is None for v in input_data):
            st.error("Please enter all input values before prediction.")

            st.markdown("### Feature Impact")

            feature_names = ["Nitrogen", "Phosphorus", "Potassium", "pH"]

            for i, val in enumerate(input_data):
                st.write(f"{feature_names[i]}: {val}")

            if st.button("Reset Inputs"):
            st.session_state.clear()
            st.experimental_rerun()

            if "history" not in st.session_state:
            st.session_state["history"] = []

            st.markdown("### Prediction History")

            for i, item in enumerate(st.session_state["history"]):
            st.write(f"{i+1}. {item}")

            st.markdown("### Result Summary")
            st.write({
                "Predicted Crop": prediction[0],
                "Input Count": len(input_data),
                "Status": "Prediction Completed"
            })
            st.success("Use the sidebar to navigate through Home, Crop Assessment, and Result pages.")

            st.info("Fill all soil and weather values carefully before moving to the Result page.")

            st.markdown("---")
            st.caption("Smart Crop Prediction System | Streamlit UI | SHAP Explainable AI")
            col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🌦 Weather Input")
    st.write("Temperature, humidity, and rainfall are collected for assessment.")

with col2:
    st.markdown("### 🌱 Soil Input")
    st.write("Nitrogen, phosphorus, potassium, and pH are used for analysis.")

with col3:
    st.markdown("### 🤖 AI Result")
    st.write("Prediction, recommendation, and SHAP explanation are shown.")

    st.write("Prediction Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    st.markdown("### Prediction Status")
    st.success("Assessment completed successfully")

    st.write("Total Predictions:", len(st.session_state["history"]))

    st.info("Review the prediction, recommendation, and SHAP analysis before making agricultural decisions.")

    st.markdown("### Key Insights")
st.write("The model analyzed the given soil values to identify a suitable crop.")
st.write("Prediction is based on the relationship between nutrient values and crop patterns.")
st.markdown("### Summary Recommendation")
st.info("Use the predicted crop as a guidance result and verify soil conditions before cultivation.")
st.info("Balanced nutrients and correct pH can improve better crop suitability."
st.markdown("### Explanation in Words")
st.write(
    f"The system predicted **{prediction[0]}** because the entered soil features "
    "are closer to the conditions usually suitable for this crop."
)
st.write(
    "The SHAP chart above shows which features contributed more to the final prediction."
)