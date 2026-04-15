import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib  # Using joblib instead of pickle (better for large numpy arrays)
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("\n LOADING DATASET...")
df = pd.read_csv("Crop_Recommendation.csv")

print(f"\n Dataset loaded successfully!")
print(f"   • Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"   • Crops: {df['Crop'].nunique()} different crops")
print(f"   • Samples per crop: {df['Crop'].value_counts().min()} to {df['Crop'].value_counts().max()}")

print("\n Data Types:")
print(df.dtypes)

print("\n Missing Values:")
print(df.isnull().sum())

print("\n Statistical Summary:")
print(df.describe())

# Create a figure with multiple subplots
fig = plt.figure(figsize=(20, 16))

# Distribution of Numerical Features
ax1 = plt.subplot(3, 3, 1)
df[['Nitrogen', 'Phosphorus', 'Potassium']].hist(ax=ax1, bins=20, alpha=0.7)
ax1.set_title('Distribution of Soil Nutrients (N, P, K)')
ax1.set_xlabel('Value')
ax1.set_ylabel('Frequency')