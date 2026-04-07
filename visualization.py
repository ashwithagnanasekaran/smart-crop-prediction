import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/raw/crop_recommendation.csv")

print("===== DATA VISUALIZATION =====")

# -----------------------
# Crop Distribution
# -----------------------
plt.figure(figsize=(10,5))
sns.countplot(x="label", data=df)
plt.xticks(rotation=90)
plt.title("Crop Distribution")
plt.show()

print("Displayed crop distribution")

# -----------------------
# Correlation Heatmap
# -----------------------
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

print("Displayed correlation heatmap")

# -----------------------
# Feature Distribution
# -----------------------
df.hist(figsize=(10,8))
plt.show()

print("Displayed feature distributions")

# -----------------------
# Continuity line 🔥
# -----------------------
print("\nVisualization completed. Insights can be used for model building")