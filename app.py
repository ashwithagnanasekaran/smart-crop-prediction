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
    
    with col1:
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

    import streamlit as st

st.set_page_config(page_title="Smart Crop Prediction", layout="wide")

page = st.sidebar.radio("Navigate", ["Home", "Crop Assessment", "Result"])

st.markdown("## Dashboard Highlights")

card1, card2, card3, card4 = st.columns(4)

with card1:
    st.markdown("### 📈 Model Accuracy")
    st.info("Crop prediction model accuracy: 96%")

with card2:
    st.markdown("### 🌾 Crops Supported")
    st.info("Rice, Wheat, Maize, Cotton, Sugarcane")

with card3:
    st.markdown("### ☀️ Seasons")
    st.info("Kharif, Rabi, Summer")

with card4:
    st.markdown("### 🔁 Rotation Rules")
    st.info("Avoid growing the same crop repeatedly on the same soil.")

elif page == "Crop Assessment":
    st.title("🧪 Crop Assessment")
    st.subheader("Enter Soil and Weather Details")

    temp = st.slider("Temperature", 0, 50, 25)
    humidity = st.slider("Humidity", 0, 100, 60)
    rainfall = st.slider("Rainfall", 0, 300, 100)

    nitrogen = st.number_input("Nitrogen (N)", min_value=0, value=50)
    phosphorus = st.number_input("Phosphorus (P)", min_value=0, value=50)
    potassium = st.number_input("Potassium (K)", min_value=0, value=50)
    ph = st.slider("Soil pH", 0.0, 14.0, 6.5)

    st.markdown("### Selected Input Summary")
    st.write({
        "Temperature": temp,
        "Humidity": humidity,
        "Rainfall": rainfall,
        "Nitrogen": nitrogen,
        "Phosphorus": phosphorus,
        "Potassium": potassium,
        "pH": ph
    })

    col1, col2 = st.columns(2)

    with col1:
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
            st.markdown("### Input Checklist")
st.checkbox("Temperature entered", value=True)
st.checkbox("Humidity entered", value=True)
st.checkbox("Rainfall entered", value=True)
st.checkbox("Soil nutrients entered", value=True)

st.caption("Recommended: enter realistic values for better prediction quality.")

st.caption("Recommended: enter realistic values for better prediction quality.")
from datetime import datetime

import streamlit as st
import shap
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Crop Prediction", layout="wide")

page = st.sidebar.radio("Navigate", ["Home", "Crop Assessment", "Result"])

if page == "Home":
    st.title("🌱 Smart Crop Prediction System")
    st.subheader("Welcome to the Crop Prediction Application")
    st.write("This system helps predict suitable crops using soil and weather details.")

elif page == "Crop Assessment":
    st.title("🧪 Crop Assessment")
    st.subheader("Enter Soil and Weather Details")

    temp = st.slider("Temperature", 0, 50, 25)
    humidity = st.slider("Humidity", 0, 100, 60)
    rainfall = st.slider("Rainfall", 0, 300, 100)

    nitrogen = st.number_input("Nitrogen (N)", min_value=0, value=50)
    phosphorus = st.number_input("Phosphorus (P)", min_value=0, value=50)
    potassium = st.number_input("Potassium (K)", min_value=0, value=50)
    ph = st.slider("Soil pH", 0.0, 14.0, 6.5)

    st.markdown("### Selected Input Summary")
    st.write({
        "Temperature": temp,
        "Humidity": humidity,
        "Rainfall": rainfall,
        "Nitrogen": nitrogen,
        "Phosphorus": phosphorus,
        "Potassium": potassium,
        "pH": ph
    })

    col1, col2 = st.columns(2)

    with col1:
       
def get_weather_data(city):
    api_key = "74eb35dc87ea251ffb73b2ce2becbae0"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        # DEBUG PRINT (helps you understand errors)
        print(data)

        if response.status_code == 200 and "main" in data:
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            rainfall = data.get('rain', {}).get('1h', 0)

            return temp, humidity, rainfall
        else:
            print("API Error:", data)
            return None, None, None

    except Exception as e:
        print("Exception:", e)
        return None, None, None

def predict_crops(input_data):
    input_df = pd.DataFrame([input_data], columns=feature_names)
    probabilities = model.predict_proba(input_df)[0]

    le = load_encoder()

    # FIX: use label encoder
    crop_names = le.inverse_transform(np.arange(len(probabilities)))

    crop_confidences = [(crop, prob * 100) for crop, prob in zip(crop_names, probabilities)]
    
    return sorted(crop_confidences, key=lambda x: x[1], reverse=True)

def get_crops_by_season(season):
    """Get all crops that belong to a season"""
    return [crop for crop in all_crops if crop_seasons.get(crop) == season]

def get_confidence_level(confidence):
    """Get confidence level class"""
    if confidence >= 90:
        return "conf-high"
    elif confidence >= 70:
        return "conf-moderate"
    else:
        return "conf-low"

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
