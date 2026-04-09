import shutil

shutil.copy("data/raw/crop_recommendation.csv", "data/backup.csv")
import shutil
import os

print("===== DATA BACKUP PROCESS STARTED =====")

# -----------------------
# Source & Destination
# -----------------------
source = "data/raw/crop_recommendation.csv"
destination = "data/backup/crop_backup.csv"

# -----------------------
# Create backup folder
# -----------------------
os.makedirs("data/backup", exist_ok=True)
print("Backup folder checked/created")

# -----------------------
# Copy file
# -----------------------
shutil.copy(source, destination)

print(f"Backup created successfully at {destination}")

# -----------------------
# File size check (extra 🔥)
# -----------------------
size = os.path.getsize(destination)
print(f"Backup file size: {size} bytes")

# -----------------------
# Continuity Line 🔥
# -----------------------
print("\nDataset backup completed. Data is now safe and ready for further processing 🚀")