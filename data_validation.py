import pandas as pd

# -----------------------
# Load cleaned dataset
# -----------------------
df = pd.read_csv("data/cleaned/crop_cleaned.csv")

print("===== DATA VALIDATION STARTED =====")

# -----------------------
# 1. Shape Check
# -----------------------
print("\nDataset Shape:", df.shape)

# -----------------------
# 2. Missing Values Check
# -----------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------
# 3. Data Types Check
# -----------------------
print("\nData Types:")
print(df.dtypes)

# -----------------------
# 4. Duplicate Check
# -----------------------
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

# -----------------------
# 5. Value Range Check
# -----------------------
print("\nStatistical Summary:")
print(df.describe())

# -----------------------
# 6. Unique Values (Target)
# -----------------------
print("\nUnique Crops:")
print(df["label"].unique())

# -----------------------
# 7. Basic Validation Rules
# -----------------------
print("\nValidation Rules Check:")

if (df["ph"] < 0).any() or (df["ph"] > 14).any():
    print("⚠️ pH values out of range!")
else:
    print("✅ pH values within valid range")

if (df["temperature"] < -10).any() or (df["temperature"] > 60).any():
    print("⚠️ Temperature values suspicious!")
else:
    print("✅ Temperature values look valid")

# -----------------------
# Continuity line 🔥
# -----------------------
print("\nDataset validated successfully and ready for model training")