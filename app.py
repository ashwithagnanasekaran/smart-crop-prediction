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

    def get_shap_values(model, input_data):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(input_data)
    return shap_values

def get_weather_data(city):
    api_key = "29c899545aa2ed371bcf7d9b16949128"
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
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Model Accuracy", "99.32%", "↑ 0.5%")
    with col2:
        st.metric("Crops Supported", f"{len(all_crops)}", "22 total")
    with col3:
        st.metric("Seasons", "3", "Kharif, Rabi, Zaid")
    with col4:
        st.metric("Rotation Rules", "5 types", "Smart scoring")

# CROP ASSESSMENT PAGE
elif selected == "Crop Assessment":
    st.title("🔍 Crop Rotation Assessment")
    
    col1, col2, col3 = st.columns([4, 1, 1])

    with col2:
        if st.button("🎲 Random"):
            fill_random()
            st.success("Random values generated!")
            st.rerun()

    with col3:
        if st.button("🌐 Fetch Weather"):
            if st.session_state.location.strip() == "":
                st.warning("⚠️ Please enter a location first")
            else:
                temp, hum, rain = get_weather_data(st.session_state.location)

                if temp is not None:
                    st.session_state.temperature = round(temp, 1)
                    st.session_state.humidity = round(hum, 1)
                    st.session_state.rainfall = round(rain, 1)
                    st.success(f"Weather updated for {st.session_state.location} ✅")
                else:
                    st.error("❌ Failed to fetch weather data. Check location name.")
    
    # Input Form
    with st.container():
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🌱 Soil Conditions")
            st.session_state.nitrogen = st.number_input("Nitrogen (N)", 0.0, 200.0, st.session_state.nitrogen, help="20-120 is ideal range")
            st.session_state.phosphorus = st.number_input("Phosphorus (P)", 0.0, 200.0, st.session_state.phosphorus, help="15-100 is ideal range")
            st.session_state.potassium = st.number_input("Potassium (K)", 0.0, 250.0, st.session_state.potassium, help="15-150 is ideal range")
            st.session_state.ph = st.number_input("pH Value", 3.0, 10.0, st.session_state.ph, help="5.5-8.0 is ideal range")
        
        with col2:
            st.subheader("🌤️ Climate Conditions")
            st.session_state.temperature = st.number_input("Temperature (°C)", 0.0, 50.0, st.session_state.temperature, help="15-35°C typical")
            st.session_state.humidity = st.number_input("Humidity (%)", 0.0, 100.0, float(st.session_state.humidity), help="40-90% typical")
            st.session_state.rainfall = st.number_input("Rainfall (mm)", 0.0, 400.0, float(st.session_state.rainfall), help="50-250mm typical")
            st.session_state.location = st.text_input(
                "Location/Region", 
                st.session_state.location,
                placeholder="Enter city name (e.g., Chennai, Coimbatore, Delhi)"
            )                    
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Previous Crop Section
        
        col1, col2 = st.columns([1, 3])
        with col1:
            st.session_state.has_previous = st.checkbox("Had Previous Crop?", st.session_state.has_previous)
        
        with col2:
            if st.session_state.has_previous:
                # Detect current season
                current_month = datetime.now().month
                current_season = get_season_from_month(current_month)
                
                # Determine previous season (the one before current)
                if current_season == 'Rabi':
                    prev_season = 'Kharif'
                elif current_season == 'Zaid':
                    prev_season = 'Rabi'
                else:  # Kharif
                    prev_season = 'Zaid'
                
                # Get crops from previous season only
                prev_season_crops = get_crops_by_season(prev_season)
                
                st.markdown(f"**Previous Season:** {prev_season} ({season_months[prev_season]})")
                st.session_state.previous_crop = st.selectbox(
                    "Select Previous Crop",
                    options=prev_season_crops,
                    index=prev_season_crops.index(st.session_state.previous_crop) if st.session_state.previous_crop in prev_season_crops else 0
                )
            else:
                st.info("No previous crop selected. Will show recommendations for all seasons.")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Predict button
        if st.button("Get Rotation Recommendations", type="primary", use_container_width=True):
            # Prepare input data
            input_data = [
                st.session_state.nitrogen,
                st.session_state.phosphorus,
                st.session_state.potassium,
                st.session_state.temperature,
                st.session_state.humidity,
                st.session_state.ph,
                st.session_state.rainfall
            ]
            
            # Get predictions
            all_predictions = predict_crops(input_data)
            
            # Detect current season
            current_season = get_season_from_temperature(st.session_state.temperature)
            
            # Store results
            st.session_state.results = {
                'predictions': all_predictions,
                'nitrogen': st.session_state.nitrogen,
                'phosphorus': st.session_state.phosphorus,
                'potassium': st.session_state.potassium,
                'ph': st.session_state.ph,
                'temperature': st.session_state.temperature,
                'humidity': st.session_state.humidity,
                'rainfall': st.session_state.rainfall,
                'location': st.session_state.location,
                'has_previous': st.session_state.has_previous,
                'previous_crop': st.session_state.previous_crop if st.session_state.has_previous else None,
                'current_season': current_season
            }
            
            st.session_state.pred_made = True
            st.success("✅ Analysis complete! View results below.")

# RESULTS PAGE
elif selected == "Results":
    st.title("📊 Crop Rotation Recommendations")
    
    if not st.session_state.pred_made:
        st.warning("No recommendations available. Please complete the Crop Assessment first.")
        if st.button("Go to Crop Assessment"):
            st.session_state.selected = "Crop Assessment"
            st.rerun()
    else:
        r = st.session_state.results
        
        # ========================================
        # INPUT SUMMARY
        # ========================================
        st.markdown('<div class="section-header">📥 INPUT CONDITIONS</div>', unsafe_allow_html=True)
        
        col1, col2, col3= st.columns(3)
        with col1:
            st.markdown(f"**📍 Location:** {r['location']}")
            st.markdown(f"**🧪 pH:** {r['ph']}")
        with col2:
            st.markdown(f"**🌡️ Temperature:** {r['temperature']}°C")
            st.markdown(f"**💧 Humidity:** {r['humidity']}%")
        with col3:
            st.markdown(f"**🟤 N:** {r['nitrogen']} | **🔴 P:** {r['phosphorus']} | **🟡 K:** {r['potassium']}")
            st.markdown(f"**🌧️ Rainfall:** {r['rainfall']} mm")

        
        # ========================================
        # SCENARIO 1: NEW FIELD (No Previous Crop)
        # ========================================
        if not r['has_previous']:
            st.markdown('<div class="section-header">🌱 NEW FIELD - RECOMMENDATIONS FOR ALL SEASONS</div>', unsafe_allow_html=True)
            
            # Get predictions
            all_preds = r['predictions']
            
            # Group by season
            season_crops = {'Kharif': [], 'Rabi': [], 'Zaid': []}
            for crop, conf in all_preds:
                season = crop_seasons.get(crop, 'Kharif')
                season_crops[season].append((crop, conf))
            
            # Display each season
            for season in season_order:
                crops = season_crops[season][:3]  # Top 3
                
                # Determine card class
                if season == 'Kharif':
                    card_class = 'kharif-card'
                    icon = '🌧️'
                elif season == 'Rabi':
                    card_class = 'rabi-card'
                    icon = '❄️'
                else:
                    card_class = 'zaid-card'
                    icon = '☀️'
                
                st.markdown(f"""
                <div class="season-card {card_class}">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <span class="season-title">{icon} {season} ({season_months[season]})</span>
                    </div>
                """, unsafe_allow_html=True)
                
                if crops:
                    for i, (crop, conf) in enumerate(crops):
                        # Get crop details from dictionary or use defaults
                        details = crop_details.get(crop, default_details)
                        family = get_crop_family(crop)
                        
                        st.markdown(f"""
                        <div class="crop-card">
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <span style="font-size:22px; font-weight:600;">{i+1}. {crop}</span>
                                <span class="family-badge">{family}</span>
                            </div>
                            <div style="margin-top:8px; display:grid; grid-template-columns:repeat(3,1fr); gap:5px; font-size:18px;">
                                <span>{details['benefit']}</span>
                                <span>{details['water']}</span>
                                <span>{details['soil']}</span>
                            </div>
                            <div style="margin-top:6px; font-size:18px; color:#555 !important; font-style:italic;">
                                📌 {details['tip']} • Best in {season_months[season]}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.markdown("<p>No crops data available for this season</p>", unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
        
        # ========================================
        # SCENARIO 2: EXISTING FIELD (With Previous Crop)
        # ========================================
        else:
            st.markdown('<div class="section-header">🔄 ROTATION RECOMMENDATIONS FOR REMAINING SEASONS</div>', unsafe_allow_html=True)
            
            previous_crop = r['previous_crop']
            prev_season = crop_seasons.get(previous_crop, 'Unknown')
            current_season = r['current_season']
            
            # Summary card
            st.markdown(f"""
            <div class="info-card">
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; text-align: center;">
                    <!-- Column 1: Previous Crop -->
                    <div style="padding: 10px;">
                        <div style="font-size: 14px; color: #64748b; margin-bottom: 5px;">🌾 PREVIOUS CROP</div>
                        <div style="font-size: 20px; font-weight: 700; color: #1e293b;">{previous_crop}</div>
                        <div style="font-size: 13px; color: #475569;">{prev_season} season</div>
                    </div>
                    <!-- Column 2: Current Season -->
                    <div style="padding: 10px; border-left: 1px solid #e2e8f0; border-right: 1px solid #e2e8f0;">
                        <div style="font-size: 14px; color: #64748b; margin-bottom: 5px;">🌤️ CURRENT SEASON</div>
                        <div style="font-size: 20px; font-weight: 700; color: #1e293b;">{current_season}</div>
                        <div style="font-size: 13px; color: #475569;">auto-detected from {r['temperature']}°C</div>
                    </div>
                    <!-- Column 3: Rotation Goal -->
                    <div style="padding: 10px;">
                        <div style="font-size: 14px; color: #64748b; margin-bottom: 5px;">🎯 ROTATION GOAL</div>
                        <div style="font-size: 16px; font-weight: 600; color: #1e293b; margin-top: 5px;">Optimal Soil Health</div>
                        <div style="font-size: 13px; color: #475569;">crop sequence planning</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Determine remaining seasons
            all_seasons = season_order.copy()
            if prev_season in all_seasons:
                all_seasons.remove(prev_season)
            
            # Reorder to show current season first if it's in remaining
            if current_season in all_seasons:
                all_seasons.remove(current_season)
                remaining_seasons = [current_season] + all_seasons
            else:
                remaining_seasons = all_seasons
            
            # Get all predictions
            all_preds = dict(r['predictions'])
            
            # For each remaining season
            for season in remaining_seasons:
                # Get crops for this season
                season_crops = get_crops_by_season(season)
                
                # Calculate rotation scores
                crop_scores = []
                for crop in season_crops:
                    if crop in all_preds:
                        base_conf = all_preds[crop]
                        rot_benefit = get_rotation_benefit(previous_crop, crop)
                        final_score = base_conf + rot_benefit
                        crop_scores.append((crop, base_conf, rot_benefit, final_score))
                
                # Sort by final score
                crop_scores.sort(key=lambda x: x[3], reverse=True)
                top_crops = crop_scores[:3]
                
                # Season card
                if season == 'Kharif':
                    card_class = 'kharif-card'
                    icon = '🌧️'
                elif season == 'Rabi':
                    card_class = 'rabi-card'
                    icon = '❄️'
                else:
                    card_class = 'zaid-card'
                    icon = '☀️'
                
                timing = "Next" if season == current_season else "Later"
                st.markdown(f"""
                <div class="season-card {card_class}">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <span class="season-title">{icon} {season} Season ({timing})</span>
                        <span class="season-months">{season_months[season]}</span>
                    </div>
                """, unsafe_allow_html=True)
                
                # Top recommendations
                for i, (crop, base_conf, rot_benefit, final_score) in enumerate(top_crops):
                    # Determine benefit class
                    if rot_benefit > 0:
                        benefit_class = "benefit-high"
                        benefit_text = f"+{rot_benefit}"
                    elif rot_benefit < 0:
                        benefit_class = "benefit-low"
                        benefit_text = f"{rot_benefit}"
                    else:
                        benefit_class = "benefit-medium"
                        benefit_text = f"{rot_benefit}"
                    
                    # Medal emoji - using numbers instead of emojis as in your code
                    medals = ["🥇", "🥈", "🥉"]
                    
                    # Why text
                    if rot_benefit == 50:
                        why = "Same crop - not recommended!"
                    elif rot_benefit == -20:
                        why = f"Same family as {previous_crop}"
                    elif rot_benefit == 30:
                        why = f"Legume after {get_crop_family(previous_crop)} - excellent!"
                    elif rot_benefit == 25:
                        why = f"Cereal after Legume - very good"
                    elif rot_benefit == 20:
                        why = f"Different family than {previous_crop}"
                    else:
                        why = "Rotation benefit"
                    
                    # THIS NEEDS TO BE INSIDE THE LOOP
                    st.markdown(f"""
                    <div class="rotation-card">
                        <!-- Crop name centered -->
                        <div style="text-align: center; margin-bottom: 15px;">
                            <span class="medal">{medals[i]}</span>
                            <strong style="font-size: 30px; margin-left: 5px;">{crop}</strong>
                        </div>
                        <!-- Why on left, Final score on right -->
                        <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 5px;">
                            <div style="font-size: 15px; color: #4a5568; max-width: 60%;">
                                📌 {why}
                            </div>
                            <div style="text-align: right;">
                            <span class="{get_confidence_level(final_score)}">Final score: {final_score:.1f}%</span>             
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                # Close the season card AFTER the loop
                st.markdown('</div>', unsafe_allow_html=True)
                            
            # ========================================
            # ROTATION CYCLE VISUALIZATION
            # ========================================
            st.markdown('<div class="section-header">🔄 CROP ROTATION CYCLE</div>', unsafe_allow_html=True)

            # Get top recommendations for each remaining season
            rotation_cycle = []
            rotation_cycle.append(("Past", previous_crop, prev_season))

            # Track if we're at current or future
            is_first_future = True
            for season in remaining_seasons:
                season_crops = get_crops_by_season(season)
                crop_scores = []
                for crop in season_crops:
                    if crop in all_preds:
                        base_conf = all_preds[crop]
                        rot_benefit = get_rotation_benefit(previous_crop, crop)
                        final_score = base_conf + rot_benefit
                        crop_scores.append((crop, final_score))
                crop_scores.sort(key=lambda x: x[1], reverse=True)
                if crop_scores:
                    rotation_cycle.append((season, crop_scores[0][0], season))

            # Display as timeline with 3 unique colors
            cols = st.columns(len(rotation_cycle))

            for i, (col, (time_period, crop, season)) in enumerate(zip(cols, rotation_cycle)):
                with col:
                    if time_period == "Past":
                        # PAST CARD - Grey
                        arrow_text = "⬅️ PAST"
                        arrow_class = "cycle-arrow-past"
                        card_class = "cycle-card-past"
                    elif i == 1:  # First future = Current season
                        # CURRENT CARD - Blue
                        arrow_text = f"➡️ CURRENT ({time_period})"
                        arrow_class = "cycle-arrow-current"
                        card_class = "cycle-card-current"
                    else:  # Later future
                        # FUTURE CARD - Green
                        arrow_text = f"⬇️ FUTURE ({time_period})"
                        arrow_class = "cycle-arrow-future"
                        card_class = "cycle-card-future"
                    
                    st.markdown(f"""
                    <div class="{card_class}">
                        <div class="{arrow_class}">{arrow_text}</div>
                        <div class="cycle-crop-name">{crop}</div>
                        <div class="cycle-season-name">{season}</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # ========================================
            # SOIL HEALTH INSIGHT
            # ========================================
            st.markdown('<div class="section-header">🌱 SOIL HEALTH INSIGHT</div>', unsafe_allow_html=True)
            
            # Get nutrient impact
            prev_impact = nutrient_impact.get(previous_crop, {'N': -20, 'P': -10, 'K': -10})
            
            # Get top recommendation for current season
            if remaining_seasons:
                first_season = remaining_seasons[0]
                season_crops = get_crops_by_season(first_season)
                crop_scores = []
                for crop in season_crops:
                    if crop in all_preds:
                        base_conf = all_preds[crop]
                        rot_benefit = get_rotation_benefit(previous_crop, crop)
                        final_score = base_conf + rot_benefit
                        crop_scores.append((crop, final_score))
                crop_scores.sort(key=lambda x: x[1], reverse=True)
                
                if crop_scores:
                    next_crop = crop_scores[0][0]
                    next_impact = nutrient_impact.get(next_crop, {'N': 0, 'P': 0, 'K': 0})
                    
                    # Calculate soil changes
                    n_change = prev_impact.get('N', 0) + next_impact.get('N', 0)
                    p_change = prev_impact.get('P', 0) + next_impact.get('P', 0)
                    k_change = prev_impact.get('K', 0) + next_impact.get('K', 0)
                    
                    st.markdown(f"""
                    <div class="soil-insight">
                        <strong>📊 Soil Nutrient Journey:</strong><br><br>
                        • After <strong>{previous_crop}</strong>: N {prev_impact['N']:+d}, P {prev_impact['P']:+d}, K {prev_impact['K']:+d}<br>
                        • After <strong>{next_crop}</strong>: N {next_impact['N']:+d}, P {next_impact['P']:+d}, K {next_impact['K']:+d}<br>
                        • <strong>Net change over rotation</strong>: N {n_change:+d}, P {p_change:+d}, K {k_change:+d}<br><br>
                        <strong>💡 Recommendation:</strong> {"Planting " + next_crop + " after " + previous_crop + " will " + 
                        ("improve soil nitrogen naturally" if next_impact.get('N',0) > 0 else "require nitrogen supplementation") + "."}
                    </div>
                    """, unsafe_allow_html=True)
            
            # ========================================
            # CROPS TO AVOID
            # ========================================
            st.markdown('<div class="section-header">⛔ CROPS TO AVOID THIS SEASON</div>', unsafe_allow_html=True)
            
            # Get same family crops
            prev_family = get_crop_family(previous_crop)
            same_family_crops = crop_families.get(prev_family, [])
            
            # Filter to current season only
            current_season_crops = get_crops_by_season(current_season)
            avoid_crops = [c for c in same_family_crops if c in current_season_crops and c != previous_crop]
            
            if avoid_crops:
                st.markdown(f"**Same family as {previous_crop} ({prev_family}):**")
                cols = st.columns(3)
                for i, crop in enumerate(avoid_crops[:6]):
                    cols[i % 3].markdown(f"• ❌ {crop}")
            else:
                st.markdown(f"✅ No same-family crops found for {current_season} season - good for rotation!")
            
            if previous_crop in current_season_crops:
                st.error(f"❌ **Never plant {previous_crop} again in {current_season}!** Wait at least one year.")

        st.markdown('<div class="section-header">🧠 MODEL EXPLANATION (SHAP)</div>', unsafe_allow_html=True)

        # =========================
        # PREPARE INPUT
        # =========================
        input_data = pd.DataFrame([[ 
            r['nitrogen'],
            r['phosphorus'],
            r['potassium'],
            r['temperature'],
            r['humidity'],
            r['ph'],
            r['rainfall']
        ]], columns=feature_names)

        try:
            # =========================
            # EXPLAINER
            # =========================
            explainer = shap.TreeExplainer(model)
            shap_values = explainer(input_data)   # ✅ NEW API (IMPORTANT)

            # Get predicted class index
            pred_class = np.argmax(model.predict_proba(input_data)[0])

            # =========================
            # EXTRACT SINGLE EXPLANATION
            # =========================
            # shape: (features,)
            shap_values_single = shap_values.values[0, :, pred_class]
            expected_value = shap_values.base_values[0, pred_class]

            # =========================
            # 1 & 2 SIDE BY SIDE
            # =========================
            st.markdown("### 📊 Model Insights")

            col1, col2 = st.columns(2)

            # =========================
            # LEFT: FEATURE IMPORTANCE
            # =========================
            with col1:
                st.markdown("#### 📊 Feature Importance")

                importance = np.abs(shap_values_single)
                sorted_idx = np.argsort(importance)[::-1]

                fig, ax = plt.subplots()
                ax.barh(np.array(feature_names)[sorted_idx], importance[sorted_idx])
                ax.invert_yaxis()
                ax.set_title("Feature Importance")

                st.pyplot(fig)
                plt.close(fig)

            # =========================
            # RIGHT: WATERFALL
            # =========================
            with col2:
                st.markdown("#### 📉 Prediction Breakdown")

                explanation = shap.Explanation(
                    values=shap_values_single,
                    base_values=expected_value,
                    data=input_data.iloc[0].values,
                    feature_names=feature_names
                )

                fig2, ax2 = plt.subplots(figsize=(6, 4))  # smaller for column fit
                shap.plots.waterfall(explanation, show=False)

                st.pyplot(fig2)
                plt.close(fig2)

            # =========================
            # 3. FORCE PLOT (FINAL FIX - HTML)
            # =========================
            import streamlit.components.v1 as components

            st.markdown("### 🔍 Prediction Force Plot")

            force_plot = shap.force_plot(
                expected_value,
                shap_values_single,
                input_data.iloc[0]
            )

            html = f"""
            <head>{shap.getjs()}</head>
            <body>{force_plot.html()}</body>
            """

            components.html(html, height=220)

            # =========================
            # 4. HUMAN EXPLANATION
            # =========================
            st.markdown("### 🧠 Explanation in Words")

            for i, feature in enumerate(feature_names):
                val = input_data.iloc[0][feature]
                impact = shap_values_single[i]

                if impact > 0:
                    st.write(f"🔺 {feature} = {val} increased prediction by {impact:.4f}")
                else:
                    st.write(f"🔻 {feature} = {val} decreased prediction by {abs(impact):.4f}")

            # =========================
            # 5. KEY INSIGHT
            # =========================
            st.markdown("### 📌 Key Insight")

            top_idx = np.argmax(np.abs(shap_values_single))
            top_feature = feature_names[top_idx]

            st.markdown(f'<div style="color: #1a4d2e; font-weight: 600; background: #d5e8d4; padding: 10px; border-radius: 8px; border-left: 4px solid #2d6a4f;">✅ Most influential feature: <strong>{top_feature}</strong></div>', unsafe_allow_html=True)
            top_crop = r['predictions'][0][0]

            st.info(f"""
            The model recommends **{top_crop}** mainly because:

            • {top_feature} had the strongest influence  
            • SHAP values show how each feature contributed  
            • Positive values push prediction higher  
            • Negative values reduce confidence  

            👉 Fully explainable AI decision.
            """)

        except Exception as e:
            st.error(f"SHAP error: {e}")

    
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
