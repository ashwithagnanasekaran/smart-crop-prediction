import pandas as pd

df = pd.read_csv("data/cleaned/crop_cleaned.csv")

report = df.describe()
report.to_csv("data/report.csv")

print("Data report generated")