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

# Crop Distribution
fig = plt.figure(figsize=(20, 16))
ax2 = plt.subplot(3, 3, 2)
crop_counts = df['Crop'].value_counts()
crop_counts.plot(kind='bar', ax=ax2, color='skyblue')
ax2.set_title('Distribution of Crops')
ax2.set_xlabel('Crop')
ax2.set_ylabel('Count')
ax2.tick_params(axis='x', rotation=45)

# pH Distribution
fig = plt.figure(figsize=(20, 16))
ax3 = plt.subplot(3, 3, 3)
df['pH_Value'].hist(bins=20, color='green', alpha=0.7, ax=ax3)
ax3.axvline(df['pH_Value'].mean(), color='red', linestyle='--', label=f'Mean: {df["pH_Value"].mean():.2f}')
ax3.set_title('pH Value Distribution')
ax3.set_xlabel('pH')
ax3.set_ylabel('Frequency')
ax3.legend()

# Correlation Heatmap
fig = plt.figure(figsize=(20, 16))
ax4 = plt.subplot(3, 3, 4)
fig = plt.figure(figsize=(20, 16))
numeric_df = df.select_dtypes(include=[np.number])
correlation = numeric_df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, ax=ax4)
ax4.set_title('Feature Correlation Heatmap')

# Boxplot: N, P, K by Crop Type (Top 10 crops)
fig = plt.figure(figsize=(20, 16))
ax5 = plt.subplot(3, 3, 5)
top_crops = df['Crop'].value_counts().head(10).index
df_top = df[df['Crop'].isin(top_crops)]
sns.boxplot(data=df_top, x='Crop', y='Nitrogen', ax=ax5)
ax5.set_title('Nitrogen Distribution by Crop (Top 10)')
ax5.tick_params(axis='x', rotation=45)

# Temperature vs Humidity Scatter
fig = plt.figure(figsize=(20, 16))
ax6 = plt.subplot(3, 3, 6)
scatter = ax6.scatter(df['Temperature'], df['Humidity'], 
                      c=pd.factorize(df['Crop'])[0], alpha=0.6, cmap='tab20')
ax6.set_title('Temperature vs Humidity')
ax6.set_xlabel('Temperature (°C)')
ax6.set_ylabel('Humidity (%)')

# Rainfall Distribution
fig = plt.figure(figsize=(20, 16))
ax7 = plt.subplot(3, 3, 7)
df['Rainfall'].hist(bins=30, color='blue', alpha=0.7, ax=ax7)
ax7.set_title('Rainfall Distribution')
ax7.set_xlabel('Rainfall (mm)')
ax7.set_ylabel('Frequency')