# preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load dataset
df = pd.read_csv("data/raw/crop_recommendation.csv")

# -----------------------
# Basic Info
# -----------------------
print("Shape:", df.shape)
print(df.info())

# -----------------------
# Missing Values
# -----------------------
print("Missing values:\n", df.isnull().sum())

# If any missing → fill (safe step)
df.fillna(df.mean(numeric_only=True), inplace=True)

# -----------------------
# Remove Duplicates
# -----------------------
df.drop_duplicates(inplace=True)

# -----------------------
# Feature & Target Split
# -----------------------
X = df.drop("label", axis=1)
y = df["label"]

# -----------------------
# Encoding (Target)
# -----------------------
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# -----------------------
# Scaling Features
# -----------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------
# Save Processed Data
# -----------------------
processed_df = pd.DataFrame(X_scaled, columns=X.columns)
processed_df["label"] = y_encoded

processed_df.to_csv("data/processed/crop_processed.csv", index=False)

print("Preprocessing completed and saved!")
# -----------------------
# Feature Correlation (for analysis)
# -----------------------
print("Correlation:\n", df.corr(numeric_only=True))

# -----------------------
# Save Label Classes
# -----------------------
import joblib
joblib.dump(le, "data/processed/label_encoder.pkl")

# -----------------------
# Save Scaler
# -----------------------
joblib.dump(scaler, "data/processed/scaler.pkl")

# -----------------------
# Check Final Data
# -----------------------
print(processed_df.head())

# -----------------------
# Class Distribution
# -----------------------
print("Class distribution:\n", df["label"].value_counts())# -----------------------
# Save Feature Columns
# -----------------------
joblib.dump(X.columns.tolist(), "data/processed/feature_columns.pkl")

# -----------------------
# Data Types Check
# -----------------------
print("Data types:\n", df.dtypes)

# -----------------------
# Summary Statistics
# -----------------------
print("Summary:\n", df.describe())

# -----------------------
# Check Unique Labels
# -----------------------
print("Unique crops:\n", df["label"].unique())

# -----------------------
# Final Shape
# -----------------------
print("Final processed shape:", processed_df.shape)
# -----------------------
# Check for Outliers (basic)
# -----------------------
print("Outliers check:\n", ((df - df.mean(numeric_only=True)).abs() > 3*df.std(numeric_only=True)).sum())

# -----------------------
# Feature Count
# -----------------------
print("Number of features:", X.shape[1])

# -----------------------
# Save Dataset Info
# -----------------------
with open("data/processed/dataset_info.txt", "w") as f:
    f.write(str(df.describe()))# -----------------------
# Check if any null values left
# -----------------------
print("Remaining null values:\n", df.isnull().sum().sum())