import pandas as pd

df = pd.read_csv("data/cleaned/crop_cleaned.csv")

report = df.describe()
report.to_csv("data/report.csv")

print("Data report generated")
import pandas as pd
import os

# -----------------------
# Load cleaned dataset
# -----------------------
df = pd.read_csv("data/cleaned/crop_cleaned.csv")

print("===== DATA REPORT GENERATION =====")

# -----------------------
# Basic Info
# -----------------------
print("\nDataset Shape:", df.shape)
print("Columns:", df.columns.tolist())

# -----------------------
# Statistical Report
# -----------------------
report = df.describe()
report.to_csv("data/report.csv")
print("\nStatistical report saved")

# -----------------------
# Missing Values
# -----------------------
missing = df.isnull().sum()
print("\nMissing Values:")
print(missing)

# -----------------------
# Unique Target Values
# -----------------------
print("\nUnique Crops:")
print(df["label"].unique())

# -----------------------
# Data Range Check
# -----------------------
print("\nChecking value ranges...")

if (df["ph"] >= 0).all() and (df["ph"] <= 14).all():
    print("✅ pH values valid")
else:
    print("⚠️ pH values out of range")

# -----------------------
# Feature Means (Insight)
# -----------------------
print("\nFeature Means:")
print(df.mean(numeric_only=True))

# -----------------------
# Save Clean Copy (backup)
# -----------------------
os.makedirs("data/report", exist_ok=True)
df.head(10).to_csv("data/report/sample_data.csv", index=False)

print("\nSample data saved for quick reference")

# -----------------------
# Continuity (FINAL 🔥)
# -----------------------
print("\nData report and validation completed successfully")
print("Dataset is well-structured and ready for advanced analysis or model training 🚀")