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
    
    /* ========== SEASON CARDS ========== */
    .season-card {
        padding: 22px;
        margin: 18px 0;
        border-radius: 18px;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .season-card:hover {
        transform: translateY(-3px);
    }
    
    /* Kharif - Monsoon Green-Blue */
    .kharif-card {
        background: linear-gradient(135deg, #d4e6f1 0%, #b8d9e8 100%);
        border-left: 6px solid #1e6f5c;
    }
    .kharif-card .season-title {
        color: #0a4c3e !important;
    }
    .kharif-card::before {
        content: "🌧️";
        position: absolute;
        bottom: 5px;
        right: 10px;
        font-size: 45px;
        opacity: 0.15;
    }
    
    /* Rabi - Winter Green */
    .rabi-card {
        background: linear-gradient(135deg, #d5e8d4 0%, #c0dec0 100%);
        border-left: 6px solid #2d6a4f;
    }
    .rabi-card .season-title {
        color: #1b4d3d !important;
    }
    .rabi-card::before {
        content: "❄️";
        position: absolute;
        bottom: 5px;
        right: 10px;
        font-size: 45px;
        opacity: 0.15;
    }
    
    /* Zaid - Summer Golden-Green */
    .zaid-card {
        background: linear-gradient(135deg, #f5e6c8 0%, #ecd9a8 100%);
        border-left: 6px solid #c47a2e;
    }
    .zaid-card .season-title {
        color: #8b5a2b !important;
    }
    .zaid-card::before {
        content: "☀️";
        position: absolute;
        bottom: 5px;
        right: 10px;
        font-size: 45px;
        opacity: 0.15;
    }
    
    .season-title {
        font-size: 26px;
        font-weight: 800;
        margin-bottom: 18px;
        padding-bottom: 8px;
    }
    
    .season-months {
        font-size: 14px;
        font-weight: 500;
    }
    
    /* ========== SECTION HEADERS - GOLD ========== */
    .section-header {
        color: #f5c542 !important;
        font-weight: 800;
        font-size: 1.6rem;
        margin-top: 35px;
        margin-bottom: 25px;
        padding-bottom: 12px;
        border-bottom: 4px solid #f5c542;
        display: inline-block;
    }
    
    /* ========== CONFIDENCE BADGES ========== */
    .conf-high { 
        background: linear-gradient(135deg, #2d6a4f 0%, #40916c 100%);
        color: white !important; 
        font-weight: 700;
        padding: 6px 14px;
        border-radius: 25px;
        display: inline-block;
    }
    
    .conf-moderate { 
        background: linear-gradient(135deg, #f5c542 0%, #e9a23b 100%);
        color: #1a4d2e !important; 
        font-weight: 700;
        padding: 6px 14px;
        border-radius: 25px;
        display: inline-block;
    }
    
    .conf-low { 
        background: linear-gradient(135deg, #e76f51 0%, #e63946 100%);
        color: white !important; 
        font-weight: 700;
        padding: 6px 14px;
        border-radius: 25px;
        display: inline-block;
    }
    
    /* ========== ROTATION CARDS ========== */
    .rotation-card {
        margin: 16px 0;
        padding: 22px;
        background: linear-gradient(135deg, #f5faf0 0%, #eef5e6 100%);
        border-radius: 18px;
        border-left: 8px solid #52b788;
        box-shadow: 0 6px 14px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
    }
    
    .rotation-card:hover {
        transform: translateX(8px);
        border-left-color: #f5c542;
        box-shadow: 0 10px 22px rgba(0,0,0,0.1);
    }
    
    .rotation-card .medal {
        font-size: 28px;
    }
    
    .rotation-card strong {
        color: #1a4d2e !important;
        font-size: 28px;
    }
    
    /* ========== BENEFIT BADGES ========== */
    .benefit-high { 
        background: linear-gradient(135deg, #2d6a4f 0%, #40916c 100%);
        color: white !important; 
        font-weight: 600;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 13px;
        display: inline-block;
    }
    
    .benefit-medium { 
        background: linear-gradient(135deg, #f5c542 0%, #e9a23b 100%);
        color: #1a4d2e !important; 
        font-weight: 600;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 13px;
        display: inline-block;
    }
    
    .benefit-low { 
        background: linear-gradient(135deg, #a0aec0 0%, #718096 100%);
        color: white !important; 
        font-weight: 600;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 13px;
        display: inline-block;
    }
    
    /* ========== SOIL INSIGHT CARD ========== */
    .soil-insight {
        background: linear-gradient(135deg, #f5ede0 0%, #ebe0cf 100%);
        border-left: 8px solid #8b5a2b;
        padding: 24px;
        border-radius: 20px;
        margin: 24px 0;
        box-shadow: 0 8px 20px rgba(139,90,43,0.08);
    }
    
    /* Make soil-insight text black */
    .soil-insight, .soil-insight * {
        color: #000000 !important;
    }
    
    .soil-insight strong {
        color: #6b3f1c !important;
    }
    
    /* ========== CROP CARDS ========== */
    .crop-card {
        margin: 15px 0;
        padding: 18px;
        background: linear-gradient(135deg, #ffffff 0%, #f5faf0 100%);
        border-radius: 16px;
        border-left: 6px solid #52b788;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        transition: all 0.25s ease;
    }

    .crop-card:hover {
        transform: translateX(6px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        border-left-color: #f5c542;
    }
    
    .crop-card * {
        color: #1a4d2e !important;
    }
    
    /* ========== FAMILY BADGE ========== */
    .family-badge {
        background: linear-gradient(135deg, #2d6a4f 0%, #52b788 100%);
        padding: 5px 14px;
        border-radius: 25px;
        font-size: 14px;
        font-weight: 600;
        color: white !important;
        display: inline-block;
    }
    
    /* ========== ROTATION CYCLE CARDS ========== */
    .cycle-card-past {
        background: linear-gradient(135deg, #cbd5e1 0%, #a0aec0 100%);
        padding: 20px;
        border-radius: 18px;
        text-align: center;
        border-bottom: 5px solid #718096;
        transition: transform 0.2s;
    }
    
    .cycle-card-past:hover {
        transform: translateY(-5px);
    }
    
    .cycle-card-current {
        background: linear-gradient(135deg, #2d6a4f 0%, #40916c 100%);
        padding: 20px;
        border-radius: 18px;
        text-align: center;
        border-bottom: 5px solid #f5c542;
        transition: transform 0.2s;
    }
    
    .cycle-card-current:hover {
        transform: translateY(-5px);
    }
    
    .cycle-card-future {
        background: linear-gradient(135deg, #52b788 0%, #74c69d 100%);
        padding: 20px;
        border-radius: 18px;
        text-align: center;
        border-bottom: 5px solid #2d6a4f;
        transition: transform 0.2s;
    }
    
    .cycle-card-future:hover {
        transform: translateY(-5px);
    }
    
    .cycle-crop-name {
        font-size: 26px;
        font-weight: 800;
        margin: 14px 0;
        color: white !important;
    }
    
    .cycle-season-name {
        font-size: 14px;
        font-weight: 500;
        opacity: 0.9;
        color: white !important;
    }
    
    .cycle-arrow-past, .cycle-arrow-current, .cycle-arrow-future {
        font-size: 14px;
        font-weight: 700;
        color: white !important;
    }
    
    /* ========== TIMELINE CARDS ========== */
    .timeline-past {
        background: linear-gradient(135deg, #e2e8f0 0%, #cbd5e1 100%);
        padding: 18px;
        border-radius: 14px;
        text-align: center;
        border-left: 6px solid #64748b;
    }
    
    .timeline-future {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        padding: 18px;
        border-radius: 14px;
        text-align: center;
        border-left: 6px solid #059669;
    }
    
    /* ========== INPUT FIELDS ========== */
    [data-testid="stNumberInput"] input,
    [data-testid="stTextInput"] input,
    [data-testid="stSelectbox"] select {
        background: #f5faf0 !important;
        border: 2px solid #a8d08d !important;
        border-radius: 12px !important;
        padding: 10px !important;
        color: #1a4d2e !important;
    }
    
    [data-testid="stNumberInput"] input:focus,
    [data-testid="stTextInput"] input:focus {
        border-color: #52b788 !important;
        box-shadow: 0 0 0 3px rgba(82,183,136,0.2) !important;
    }
    
    /* ========== BUTTONS ========== */
    .stButton button {
        background: linear-gradient(135deg, #2d6a4f 0%, #52b788 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 40px !important;
        padding: 12px 28px !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(45,106,79,0.3);
        background: linear-gradient(135deg, #40916c 0%, #74c69d 100%) !important;
    }
    
    /* ========== CHECKBOX ========== */
    [data-testid="stCheckbox"] label {
        color: #1a4d2e !important;
        font-weight: 500;
    }
    
    /* ========== METRICS ========== */
    [data-testid="stMetric"] {
        background: rgba(255,255,245,0.7);
        padding: 15px;
        border-radius: 16px;
        border-left: 4px solid #52b788;
    }
    
    [data-testid="stMetric"] label {
        color: #1a4d2e !important;
    }
    
    [data-testid="stMetric"] .stMetric-value {
        color: #2d6a4f !important;
    }
    
    /* ========== EXPANDER ========== */
    [data-testid="stExpander"] {
        background: rgba(245,250,240,0.8);
        border-radius: 14px;
        border: 1px solid #c8e6c9;
    }
    
    [data-testid="stExpander"] summary {
        color: #1a4d2e !important;
        font-weight: 600;
    }
    
    /* ========== ALERTS / MESSAGES ========== */
    .stAlert {
        background: linear-gradient(135deg, #d5e8d4 0%, #c0dec0 100%) !important;
        border-left: 6px solid #2d6a4f !important;
        color: #1a4d2e !important;
    }
    
    .stAlert-warning {
        background: linear-gradient(135deg, #f5e6c8 0%, #ecd9a8 100%) !important;
        border-left-color: #f5c542 !important;
    }
    
    /* ========== INPUT SUMMARY ========== */
    .input-summary {
        background: linear-gradient(135deg, #f0f7e8 0%, #e6f0da 100%);
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #a8d08d;
        margin-bottom: 20px;
    }
    
    /* ========== MEDAL STYLING ========== */
    .medal {
        font-size: 28px;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
    }
    
    /* ========== CROP DETAIL ITEMS ========== */
    .crop-detail-item {
        background: rgba(82,183,136,0.1);
        padding: 6px 12px;
        border-radius: 20px;
        text-align: center;
        font-size: 13px;
        backdrop-filter: blur(2px);
    }
    
    /* ========== TAB STYLING ========== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(245,250,240,0.7);
        border-radius: 12px;
        padding: 8px 20px;
        color: #1a4d2e;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2d6a4f 0%, #52b788 100%);
        color: white !important;
    }
    
    /* ========== DATA FRAME ========== */
    .stDataFrame {
        background: rgba(255,255,245,0.8);
        border-radius: 14px;
        border: 1px solid #a8d08d;
    }
            
    /* Make st.success text dark green */
    .stAlert[data-baseweb="alert"] {
        color: #1a4d2e !important;
        font-weight: 600 !important;
    }

    .stAlert[data-baseweb="alert"] * {
        color: #1a4d2e !important;
    }

    /* Specifically for success messages */
    div[data-testid="stAlert"] {
        background: linear-gradient(135deg, #d5e8d4 0%, #c0dec0 100%) !important;
        border-left: 6px solid #2d6a4f !important;
    }

    div[data-testid="stAlert"] * {
        color: #1a4d2e !important;
    }
    </style>
""", unsafe_allow_html=True)

# LOAD MODEL AND FILES
@st.cache_resource
def load_model():
    return joblib.load('crop_model_xgb.joblib')

@st.cache_resource
def load_features():
    return joblib.load('feature_names.joblib')

@st.cache_resource
def load_crops():
    return joblib.load('crop_list.joblib')

@st.cache_resource
def load_encoder():
    return joblib.load('label_encoder.joblib')

try:
    model = load_model()
    feature_names = load_features()
    all_crops = load_crops()
    st.sidebar.success("✅ Model loaded successfully")
except Exception as e:
    st.sidebar.error(f"❌ Error loading model: {e}")
    st.stop()

# CROP KNOWLEDGE BASE
crop_families = {
    'Cereals': ['Rice', 'Maize', 'Wheat', 'Barley'],
    'Legumes': ['ChickPea', 'Lentil', 'PigeonPeas', 'MothBeans', 'MungBean', 'Blackgram', 'KidneyBeans'],
    'Fruits': ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange', 'Papaya', 'Pomegranate'],
    'Melons': ['Watermelon', 'Muskmelon'],
    'Fiber': ['Cotton', 'Jute'],
    'Others': ['Coconut', 'Coffee']
}

crop_seasons = {
    # Kharif crops (Monsoon - June to October)
    'Rice': 'Kharif',
    'Maize': 'Kharif',
    'Cotton': 'Kharif',
    'PigeonPeas': 'Kharif',
    'MothBeans': 'Kharif',
    'Blackgram': 'Kharif',
    'MungBean': 'Kharif',
    'KidneyBeans': 'Kharif',
    'Jute': 'Kharif',
    'Coconut': 'Kharif',

    # Rabi crops (Winter - October to March)
    'ChickPea': 'Rabi',
    'Lentil': 'Rabi',
    'Wheat': 'Rabi',
    'Apple': 'Rabi',
    'Grapes': 'Rabi',
    'Orange': 'Rabi',
    'Pomegranate': 'Rabi',
    'Coffee': 'Rabi',
    
    # Rabi crops (Winter - October to March)
    'ChickPea': 'Rabi',
    'Lentil': 'Rabi',
    'Wheat': 'Rabi',
    'Apple': 'Rabi',
    'Grapes': 'Rabi',
    'Orange': 'Rabi',
    'Pomegranate': 'Rabi',
    'Coffee': 'Rabi',
    
    # Zaid crops (Summer - April to June)
    'Watermelon': 'Zaid',
    'Muskmelon': 'Zaid',
    'Banana': 'Zaid',
    'Mango': 'Zaid',
    'Papaya': 'Zaid'
}

season_months = {
    'Kharif': 'June to October (Monsoon)',
    'Rabi': 'October to March (Winter)',
    'Zaid': 'April to June (Summer)'
}

season_order = ['Kharif', 'Rabi', 'Zaid']

# Rotation benefits matrix
rotation_benefits = {
    'Legume after Cereal': 30,
    'Different family': 20,
    'Same family': -20,
    'Same crop': -50,
    'Cereal after Legume': 25
}

# Nutrient impact (simplified for demo)
nutrient_impact = {
    'Rice': {'N': -40, 'P': -15, 'K': -20},
    'Maize': {'N': -35, 'P': -20, 'K': -15},
    'Wheat': {'N': -30, 'P': -15, 'K': -10},
    'ChickPea': {'N': 30, 'P': -10, 'K': -15},
    'Lentil': {'N': 25, 'P': -8, 'K': -12},
    'Cotton': {'N': -45, 'P': -20, 'K': -25},
    'Watermelon': {'N': -20, 'P': -15, 'K': -25}
}

# Crop detailed information for New Field display
crop_details = {
    # Legumes
    'ChickPea': {'benefit': '🌱 Fixes nitrogen', 'water': '💧 Low water', 'soil': '🧪 Improves fertility', 'tip': 'Good after cereals'},
    'Lentil': {'benefit': '🌱 Nitrogen fixing', 'water': '💧 Low water', 'soil': '🧪 Soil enhancer', 'tip': 'Quick maturing'},
    'PigeonPeas': {'benefit': '🌱 Deep roots', 'water': '💧 Drought tolerant', 'soil': '🧪 Breaks hardpan', 'tip': 'Perennial crop'},
    'MothBeans': {'benefit': '🌱 Drought hardy', 'water': '💧 Very low water', 'soil': '🧪 Grows in poor soil', 'tip': 'Dryland crop'},
    'MungBean': {'benefit': '🌱 Quick green manure', 'water': '💧 Low water', 'soil': '🧪 Improves nitrogen', 'tip': 'Short duration'},
    'Blackgram': {'benefit': '🌱 Soil cover', 'water': '💧 Moderate water', 'soil': '🧪 Prevents erosion', 'tip': 'Rich in protein'},
    'KidneyBeans': {'benefit': '🌱 High value', 'water': '💧 Regular water', 'soil': '🧪 Needs fertile soil', 'tip': 'Market crop'},

    # Cereals
    'Rice': {'benefit': '🌾 Staple food', 'water': '💧 High water', 'soil': '🧪 Needs puddled soil', 'tip': 'Main kharif crop'},
    'Maize': {'benefit': '🌾 Multi-purpose', 'water': '💧 Moderate water', 'soil': '🧪 Well-drained soil', 'tip': 'Can be intercropped'},
    'Wheat': {'benefit': '🌾 Staple food', 'water': '💧 Moderate water', 'soil': '🧪 Fertile loam', 'tip': 'Main rabi crop'},
    
    # Fruits
    'Apple': {'benefit': '🍎 High value', 'water': '💧 Regular irrigation', 'soil': '🧪 Well-drained', 'tip': 'Needs cold winters'},
    'Banana': {'benefit': '🍌 Year-round fruit', 'water': '💧 High water', 'soil': '🧪 Rich organic soil', 'tip': 'Perennial crop'},
    'Mango': {'benefit': '🥭 King of fruits', 'water': '💧 Low water', 'soil': '🧪 Deep soil', 'tip': 'Long-term investment'},
    'Grapes': {'benefit': '🍇 High profit', 'water': '💧 Regulated water', 'soil': '🧪 Well-drained', 'tip': 'Needs trellising'},
    'Orange': {'benefit': '🍊 Citrus fruit', 'water': '💧 Regular water', 'soil': '🧪 Slightly acidic', 'tip': 'Vitamin C rich'},
    'Papaya': {'benefit': '🍈 Fast growing', 'water': '💧 Moderate water', 'soil': '🧪 Well-drained', 'tip': 'Quick returns'},
    'Pomegranate': {'benefit': '🍎 Drought hardy', 'water': '💧 Low water', 'soil': '🧪 Adaptable', 'tip': 'Health fruit'},
    
    # Melons
    'Watermelon': {'benefit': '🍉 Summer fruit', 'water': '💧 Moderate water', 'soil': '💨 Sandy loam', 'tip': 'Needs space'},
    'Muskmelon': {'benefit': '🍈 Aromatic fruit', 'water': '💧 Regular water', 'soil': '🧪 Well-drained', 'tip': 'Short duration'},
    
    # Fiber
    'Cotton': {'benefit': '🧶 Cash crop', 'water': '💧 Moderate water', 'soil': '🧪 Black soil', 'tip': 'Needs warm weather'},
    'Jute': {'benefit': '🧶 Golden fiber', 'water': '💧 High water', 'soil': '🧪 Alluvial soil', 'tip': 'Needs flooding'},
    
    # Others
    'Coconut': {'benefit': '🥥 Multi-purpose', 'water': '💧 Low water', 'soil': '🧪 Coastal soil', 'tip': 'Long-term crop'},
    'Coffee': {'benefit': '☕ Beverage crop', 'water': '💧 Regular water', 'soil': '🧪 Acidic soil', 'tip': 'Needs shade'}
}

# Default details for any missing crop
default_details = {
    'benefit': '🌱 Good rotation crop',
    'water': '💧 Adaptable water needs',
    'soil': '🧪 Standard soil',
    'tip': 'Follow season guidelines'
}

# HELPER FUNCTIONS

def get_season_from_temperature(temp):
    """Detect season based on temperature"""
    if temp > 30:
        return 'Zaid'
    elif 20 <= temp <= 30:
        return 'Rabi'
    else:
        return 'Kharif'

def get_season_from_month(month):
    """Get season from month number"""
    if month in [6, 7, 8, 9, 10]:
        return 'Kharif'
    elif month in [11, 12, 1, 2, 3]:
        return 'Rabi'
    else:  # April, May
        return 'Zaid'

def get_crop_family(crop):
    """Get family of a crop"""
    for family, crops in crop_families.items():
        if crop in crops:
            return family
    return 'Unknown'

def get_rotation_benefit(previous_crop, candidate_crop):
    """Calculate rotation benefit score"""
    if previous_crop == candidate_crop:
        return rotation_benefits['Same crop']
    
    prev_family = get_crop_family(previous_crop)
    cand_family = get_crop_family(candidate_crop)
    
    if prev_family == cand_family:
        return rotation_benefits['Same family']
    
    # Legume after Cereal is excellent
    if cand_family == 'Legumes' and prev_family == 'Cereals':
        return rotation_benefits['Legume after Cereal']
    
    # Cereal after Legume is very good
    if cand_family == 'Cereals' and prev_family == 'Legumes':
        return rotation_benefits['Cereal after Legume']
    
    return rotation_benefits['Different family']

def get_shap_values(model, input_data):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(input_data)
    return shap_values
    
    # Cereals
    'Rice': {'benefit': '🌾 Staple food', 'water': '💧 High water', 'soil': '🧪 Needs puddled soil', 'tip': 'Main kharif crop'},
    'Maize': {'benefit': '🌾 Multi-purpose', 'water': '💧 Moderate water', 'soil': '🧪 Well-drained soil', 'tip': 'Can be intercropped'},
    'Wheat': {'benefit': '🌾 Staple food', 'water': '💧 Moderate water', 'soil': '🧪 Fertile loam', 'tip': 'Main rabi crop'},
    
    # Fruits
    'Apple': {'benefit': '🍎 High value', 'water': '💧 Regular irrigation', 'soil': '🧪 Well-drained', 'tip': 'Needs cold winters'},
    'Banana': {'benefit': '🍌 Year-round fruit', 'water': '💧 High water', 'soil': '🧪 Rich organic soil', 'tip': 'Perennial crop'},
    'Mango': {'benefit': '🥭 King of fruits', 'water': '💧 Low water', 'soil': '🧪 Deep soil', 'tip': 'Long-term investment'},
    'Grapes': {'benefit': '🍇 High profit', 'water': '💧 Regulated water', 'soil': '🧪 Well-drained', 'tip': 'Needs trellising'},
    'Orange': {'benefit': '🍊 Citrus fruit', 'water': '💧 Regular water', 'soil': '🧪 Slightly acidic', 'tip': 'Vitamin C rich'},
    'Papaya': {'benefit': '🍈 Fast growing', 'water': '💧 Moderate water', 'soil': '🧪 Well-drained', 'tip': 'Quick returns'},
    'Pomegranate': {'benefit': '🍎 Drought hardy', 'water': '💧 Low water', 'soil': '🧪 Adaptable', 'tip': 'Health fruit'},
    
    # Melons
    'Watermelon': {'benefit': '🍉 Summer fruit', 'water': '💧 Moderate water', 'soil': '💨 Sandy loam', 'tip': 'Needs space'},
    'Muskmelon': {'benefit': '🍈 Aromatic fruit', 'water': '💧 Regular water', 'soil': '🧪 Well-drained', 'tip': 'Short duration'},
    
    # Fiber
    'Cotton': {'benefit': '🧶 Cash crop', 'water': '💧 Moderate water', 'soil': '🧪 Black soil', 'tip': 'Needs warm weather'},
    'Jute': {'benefit': '🧶 Golden fiber', 'water': '💧 High water', 'soil': '🧪 Alluvial soil', 'tip': 'Needs flooding'},
    
    # Others
    'Coconut': {'benefit': '🥥 Multi-purpose', 'water': '💧 Low water', 'soil': '🧪 Coastal soil', 'tip': 'Long-term crop'},
    'Coffee': {'benefit': '☕ Beverage crop', 'water': '💧 Regular water', 'soil': '🧪 Acidic soil', 'tip': 'Needs shade'}
}

# Default details for any missing crop
default_details = {
    'benefit': '🌱 Good rotation crop',
    'water': '💧 Adaptable water needs',
    'soil': '🧪 Standard soil',
    'tip': 'Follow season guidelines'
}

# HELPER FUNCTIONS

def get_season_from_temperature(temp):
    """Detect season based on temperature"""
    if temp > 30:
        return 'Zaid'
    elif 20 <= temp <= 30:
        return 'Rabi'
    else:
        return 'Kharif'

def get_season_from_month(month):
    """Get season from month number"""
    if month in [6, 7, 8, 9, 10]:
        return 'Kharif'
    elif month in [11, 12, 1, 2, 3]:
        return 'Rabi'
    else:  # April, May
        return 'Zaid'

def get_crop_family(crop):
    """Get family of a crop"""
    for family, crops in crop_families.items():
        if crop in crops:
            return family
    return 'Unknown'

def get_rotation_benefit(previous_crop, candidate_crop):
    """Calculate rotation benefit score"""
    if previous_crop == candidate_crop:
        return rotation_benefits['Same crop']
    
    prev_family = get_crop_family(previous_crop)
    cand_family = get_crop_family(candidate_crop)
    
    if prev_family == cand_family:
        return rotation_benefits['Same family']
    
    # Legume after Cereal is excellent
    if cand_family == 'Legumes' and prev_family == 'Cereals':
        return rotation_benefits['Legume after Cereal']
    
    # Cereal after Legume is very good
    if cand_family == 'Cereals' and prev_family == 'Legumes':
        return rotation_benefits['Cereal after Legume']
    
    return rotation_benefits['Different family']

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






























    
        # ========================================
        # RECOMMENDATIONS SUMMARY
        # ========================================
        st.markdown('<div class="section-header">💡 SUMMARY RECOMMENDATIONS</div>', unsafe_allow_html=True)
        
        if r['has_previous']:
            st.markdown("""
            • 🌱 **Rotate crop families** - Don't plant same family twice
            • 💧 **Consider water needs** - Match crops to season
            • 🧪 **Soil testing** - Regular testing improves accuracy
            • 📈 **Track yields** - Keep records for better recommendations
            """)
        else:
            st.markdown("""
            • 🌱 **Start with soil testing** - Know your baseline
            • 💧 **Match crops to season** - Choose appropriate crops
            • 📊 **Consider market demand** - Plant profitable crops
            • 🔄 **Plan rotation ahead** - Think 2-3 seasons forward
            """)

# FOOTER
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "🌾 Smart Crop Rotation System </div>",
    unsafe_allow_html=True
)