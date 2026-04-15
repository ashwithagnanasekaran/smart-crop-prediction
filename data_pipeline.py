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


def save_data(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Data saved at {path}")

def run_pipeline():
    print("===== DATA PIPELINE STARTED =====")

    # Step 1: Load
    df = load_data("data/raw/crop_recommendation.csv")

    # Step 2: Clean
    df_cleaned = clean_data(df)

    # Step 3: Preprocess
    df_processed = preprocess_data(df_cleaned)

    # Step 4: Save
    save_data(df_processed, "data/processed/crop_processed_pipeline.csv")

    print("\nPipeline executed successfully 🚀")
    print("Dataset ready for model training")

# Run pipeline
if __name__ == "__main__":
    run_pipeline()
    print("✔ Data loaded successfully")
    print("✔ Cleaning step completed")
    print("✔ Preprocessing step completed")