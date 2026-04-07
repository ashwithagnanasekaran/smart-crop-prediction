import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/crop_recommendation.csv")

# -----------------------
# Basic Info
# -----------------------
print("Before Cleaning")
print("Shape:", df.shape)

# -----------------------
# Missing Values
# -----------------------
print("\nMissing values before:")
print(df.isnull().sum())

# Fill missing values (if any)
df.fillna(df.mean(numeric_only=True), inplace=True)

# -----------------------
# Remove Duplicates
# -----------------------
duplicates = df.duplicated().sum()
print("\nDuplicate rows:", duplicates)

df.drop_duplicates(inplace=True)

# -----------------------
# After Cleaning
# -----------------------
print("\nAfter Cleaning")
print("Shape:", df.shape)

print("\nMissing values after:")
print(df.isnull().sum())

# -----------------------
# Save Cleaned Dataset
# -----------------------
df.to_csv("data/cleaned/crop_cleaned.csv", index=False)

print("\nData cleaning completed and saved!")
print("Dataset is now clean and ready for preprocessing")