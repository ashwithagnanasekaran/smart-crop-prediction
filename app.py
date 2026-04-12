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
    
<<<<<<< HEAD
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
    
=======
    with col1:
>>>>>>> e3f496714ab80c311ee06d121bc21117a3938908
        st.markdown("### Weather Details")
        st.write("Temperature:", temp)
        st.write("Humidity:", humidity)
        st.write("Rainfall:", rainfall)
<<<<<<< HEAD
=======

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
>>>>>>> e3f496714ab80c311ee06d121bc21117a3938908


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

def get_seasonal_note(season, temp, humidity):
    """Generate seasonal growing notes"""
    notes = {
        'Kharif': {
            'title': '🌧️ Kharif Season Notes',
            'tips': [
                'Monsoon season - ensure good drainage',
                'High humidity may increase pest risk',
                'Ideal for water-loving crops like Rice'
            ]
        },
        'Rabi': {
            'title': '❄️ Rabi Season Notes',
            'tips': [
                'Winter season - frost protection needed',
                'Lower water requirement',
                'Ideal for legumes and wheat'
            ]
        },
        'Zaid': {
            'title': '☀️ Zaid Season Notes',
            'tips': [
                'Summer season - irrigation critical',
                'Heat-tolerant crops recommended',
                'Short duration crops ideal'
            ]
        }
    }
    return notes.get(season, {'title': '', 'tips': []})

# SESSION STATE INITIALIZATION
defaults = {
    'nitrogen': 50.0,
    'phosphorus': 50.0,
    'potassium': 50.0,
    'ph': 6.5,
    'temperature': 26.0,
    'humidity': 70.0,
    'rainfall': 120.0,
    'has_previous': False,
    'previous_crop': 'Rice',
    'location': 'Chennai',
    'pred_made': False,
    'results': None,
    'selected': 'Crop Assessment'  # Add this

}

for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val
        
def fill_random():
    """Fill with random values"""
    st.session_state.nitrogen = round(random.uniform(20, 120), 1)
    st.session_state.phosphorus = round(random.uniform(15, 100), 1)
    st.session_state.potassium = round(random.uniform(15, 150), 1)
    st.session_state.ph = round(random.uniform(5.5, 8.0), 1)
    st.session_state.temperature = round(random.uniform(15, 38), 1)
    st.session_state.humidity = round(random.uniform(40, 90), 1)
    st.session_state.rainfall = round(random.uniform(50, 250), 1)
    st.session_state.has_previous = random.choice([True, False])
    st.session_state.previous_crop = random.choice(all_crops)
    st.session_state.location = random.choice(["Chennai","Coimbatore","Madurai","Trichy","Salem","Erode","Tirunelveli","Pollachi","Kinathukadavu","Tiruppur","Karur","Dindigul","Thanjavur"])
    st.session_state.pred_made = False

# SIDEBAR NAVIGATION
with st.sidebar:
    st.title("🌾 Smart Crop Rotation")
    
    selected = option_menu(
        menu_title=None,
        options=["Home", "Crop Assessment", "Results"],
        icons=["house", "search", "bar-chart"],
        default_index=1,
        styles={
            "container": {"padding": "0!important"},
            "nav-link": {"font-size": "14px", "text-align": "left"},
        }
    )
    
    st.markdown("---")
    
    # Model info
    st.markdown("### Model Info")
    st.info(f"🎯 **Accuracy:** 99.32%\n🌱 **Crops:** {len(all_crops)} ")
    
    # Quick tips
    with st.expander("💡 Quick Tips"):
        st.markdown("""
        **Soil Ranges:**
        - N: 20-120
        - P: 15-100  
        - K: 15-150
        - pH: 5.5-8.0
        
        **Season Guide:**
        - 🌧️ Kharif: Jun-Oct
        - ❄️ Rabi: Oct-Mar
        - ☀️ Zaid: Apr-Jun
        """)
# HOME PAGE
if selected == "Home":
    st.title("🌾 Smart Crop Rotation Recommendation System")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
        ### Welcome to Smart Crop Rotation
        
        This AI-powered system helps farmers make **intelligent crop rotation decisions** 
        based on soil conditions, climate data, and agricultural science.
        
        ### How It Works
        
        **1. Enter Soil Conditions**  
        Input your soil's N, P, K levels, pH, and current climate data
        
        **2. Tell Us Your Previous Crop**  
        Let us know what you planted last season
        
        **3. Get Rotation Recommendations**  
        Receive personalized recommendations for the next two seasons with:
        - Top crop choices with confidence scores
        - Rotation benefits and soil health insights
        - Complete crop rotation cycle planning
        
        ### Why Crop Rotation Matters
        
        - 🌱 **Soil Health:** Prevents nutrient depletion
        - 🐛 **Pest Control:** Breaks pest and disease cycles
        - 🌾 **Higher Yields:** Better long-term productivity
        - 💰 **Profit:** Diversified income streams
        """)
    
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/2917/2917995.png", width=180)
    
    st.markdown("---")