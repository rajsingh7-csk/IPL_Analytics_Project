import pandas as pd

# ==========================
# Load Dataset
# ==========================

matches = pd.read_csv("data/matches.csv")

print("=" * 50)
print("IPL DATA PREPROCESSING")
print("=" * 50)

print(f"\nOriginal Dataset Shape: {matches.shape}")

# ==========================
# Missing Values
# ==========================

print("\nMissing Values Before Cleaning:")
print(matches.isnull().sum())

# Remove rows with missing values
matches.dropna(inplace=True)

# ==========================
# Duplicate Records
# ==========================

duplicate_count = matches.duplicated().sum()
print(f"\nDuplicate Rows Found: {duplicate_count}")

matches.drop_duplicates(inplace=True)

# ==========================
# Standardize Team Names
# ==========================

team_name_mapping = {
    "Delhi Daredevils": "Delhi Capitals",
    "Kings XI Punjab": "Punjab Kings"
}

matches.replace(team_name_mapping, inplace=True)

# ==========================
# Date Formatting
# ==========================

if "date" in matches.columns:
    matches["date"] = pd.to_datetime(matches["date"])

# ==========================
# Dataset Information
# ==========================

print(f"\nCleaned Dataset Shape: {matches.shape}")

print("\nDataset Information:")
print(matches.info())

print("\nUnique Teams:")

teams = pd.unique(
    matches[["team1", "team2"]]
    .values
    .ravel()
)

for team in sorted(teams):
    print(team)

# ==========================
# Save Clean Dataset
# ==========================

matches.to_csv(
    "data/clean_matches.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")
print("File Name: clean_matches.csv")
print("\nPreprocessing Completed Successfully.")