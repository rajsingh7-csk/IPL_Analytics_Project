import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

os.makedirs("models", exist_ok=True)

# Load dataset
matches = pd.read_csv("data/clean_matches.csv")

# Required columns
df = matches[
    [
        "team1",
        "team2",
        "venue",
        "toss_winner",
        "toss_decision",
        "winner"
    ]
].copy()

df.dropna(inplace=True)

print("=" * 60)
print("IPL MATCH WINNER PREDICTION")
print("=" * 60)

print(f"\nTotal Records Used: {len(df)}")

# Features and target
X = df.drop("winner", axis=1)
y = df["winner"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            [
                "team1",
                "team2",
                "venue",
                "toss_winner",
                "toss_decision"
            ]
        )
    ]
)

# Model
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=300,
                random_state=42
            )
        )
    ]
)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"\nModel Accuracy: {accuracy:.2%}")

# Save model
joblib.dump(
    model,
    "models/winner_predictor.pkl"
)

print("\nModel saved successfully!")
print("models/winner_predictor.pkl")