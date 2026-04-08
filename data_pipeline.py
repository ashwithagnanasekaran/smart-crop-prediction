import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

def load_data(path):
    print("Loading dataset...")
    return pd.read_csv(path)

def clean_data(df):
    print("Cleaning data...")

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    # Handle missing values
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    print("Cleaning completed")
    return df

def preprocess_data(df):
    print("Preprocessing data...")

    # Split features & target
    X = df.drop("label", axis=1)
    y = df["label"]

    # Encode target
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Convert to DataFrame
    processed_df = pd.DataFrame(X_scaled, columns=X.columns)
    processed_df["label"] = y_encoded

    print("Preprocessing completed")
    return processed_df

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