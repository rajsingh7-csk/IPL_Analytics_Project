import pandas as pd
import os

# =====================================
# CREATE DATA DIRECTORY IF NOT EXISTS
# =====================================

os.makedirs("data", exist_ok=True)

# =====================================
# LOAD DATASET
# =====================================

matches = pd.read_csv("data/matches.csv")

print("=" * 60)
print("IPL DATA PREPROCESSING")
print("=" * 60)

print("\nOriginal Dataset Shape:")
print(matches.shape)

# =====================================
# REMOVE DUPLICATES
# =====================================

duplicate_count = matches.duplicated().sum()

print(f"\nDuplicate Records Found: {duplicate_count}")

matches.drop_duplicates(inplace=True)

# =====================================
# HANDLE MISSING VALUES
# =====================================

print("\nMissing Values Before Cleaning:")
print(matches.isnull().sum())

# Fill important columns instead of removing rows

if "city" in matches.columns:
    matches["city"] = matches["city"].fillna("Unknown")

if "method" in matches.columns:
    matches["method"] = matches["method"].fillna("Normal")

if "umpire1" in matches.columns:
    matches["umpire1"] = matches["umpire1"].fillna("Unknown")

if "umpire2" in matches.columns:
    matches["umpire2"] = matches["umpire2"].fillna("Unknown")

if "winner" in matches.columns:
    matches = matches[matches["winner"].notna()]

# =====================================
# STANDARDIZE TEAM NAMES
# =====================================

team_name_mapping = {
    "Delhi Daredevils": "Delhi Capitals",
    "Kings XI Punjab": "Punjab Kings"
}

matches.replace(team_name_mapping, inplace=True)

# =====================================
# DATE CONVERSION
# =====================================

if "date" in matches.columns:
    matches["date"] = pd.to_datetime(
        matches["date"],
        errors="coerce"
    )

# =====================================
# FINAL DATASET INFO
# =====================================

print("\nMissing Values After Cleaning:")
print(matches.isnull().sum())

print("\nCleaned Dataset Shape:")
print(matches.shape)

# =====================================
# SAVE CLEAN DATASET
# =====================================

matches.to_csv(
    "data/clean_matches.csv",
    index=False
)

print("\nClean Dataset Saved Successfully!")
print("File: data/clean_matches.csv")

print("\nPREPROCESSING COMPLETED SUCCESSFULLY")