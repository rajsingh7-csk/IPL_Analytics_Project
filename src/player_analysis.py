import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# CREATE OUTPUT FOLDERS
# ==========================================

os.makedirs("outputs/charts", exist_ok=True)
os.makedirs("outputs/datasets", exist_ok=True)

# ==========================================
# LOAD DATASET
# ==========================================

deliveries = pd.read_csv("data/deliveries.csv")

print("=" * 60)
print("IPL PLAYER ANALYSIS")
print("=" * 60)

# ==========================================
# TOP RUN SCORERS
# ==========================================

runs = (
    deliveries.groupby("batter")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTOP 10 RUN SCORERS")
print(runs.head(10))

runs.head(10).to_csv(
    "outputs/datasets/top_run_scorers.csv"
)

plt.figure(figsize=(10, 6))
runs.head(10).plot(kind="bar")

plt.title("Top 10 IPL Run Scorers")
plt.xlabel("Player")
plt.ylabel("Runs")

plt.tight_layout()

plt.savefig(
    "outputs/charts/top_run_scorers.png"
)

plt.close()

# ==========================================
# MOST FOURS
# ==========================================

fours = deliveries[
    deliveries["batsman_runs"] == 4
]

top_fours = (
    fours.groupby("batter")
    .size()
    .sort_values(ascending=False)
)

print("\nTOP 10 PLAYERS WITH MOST FOURS")
print(top_fours.head(10))

top_fours.head(10).to_csv(
    "outputs/datasets/top_fours.csv"
)

plt.figure(figsize=(10, 6))
top_fours.head(10).plot(kind="bar")

plt.title("Top 10 Players with Most Fours")
plt.xlabel("Player")
plt.ylabel("Number of Fours")

plt.tight_layout()

plt.savefig(
    "outputs/charts/top_fours.png"
)

plt.close()

# ==========================================
# MOST SIXES
# ==========================================

sixes = deliveries[
    deliveries["batsman_runs"] == 6
]

top_sixes = (
    sixes.groupby("batter")
    .size()
    .sort_values(ascending=False)
)

print("\nTOP 10 PLAYERS WITH MOST SIXES")
print(top_sixes.head(10))

top_sixes.head(10).to_csv(
    "outputs/datasets/top_sixes.csv"
)

plt.figure(figsize=(10, 6))
top_sixes.head(10).plot(kind="bar")

plt.title("Top 10 Players with Most Sixes")
plt.xlabel("Player")
plt.ylabel("Number of Sixes")

plt.tight_layout()

plt.savefig(
    "outputs/charts/top_sixes.png"
)

plt.close()

# ==========================================
# TOP WICKET TAKERS
# ==========================================

wickets = deliveries[
    deliveries["player_dismissed"].notna()
]

top_bowlers = (
    wickets.groupby("bowler")
    .size()
    .sort_values(ascending=False)
)

print("\nTOP 10 WICKET TAKERS")
print(top_bowlers.head(10))

top_bowlers.head(10).to_csv(
    "outputs/datasets/top_wicket_takers.csv"
)

plt.figure(figsize=(10, 6))
top_bowlers.head(10).plot(kind="bar")

plt.title("Top 10 IPL Wicket Takers")
plt.xlabel("Bowler")
plt.ylabel("Wickets")

plt.tight_layout()

plt.savefig(
    "outputs/charts/top_wicket_takers.png"
)

plt.close()

# ==========================================
# STRIKE RATE ANALYSIS
# ==========================================

balls_faced = (
    deliveries.groupby("batter")
    .size()
)

runs_scored = (
    deliveries.groupby("batter")
    ["batsman_runs"]
    .sum()
)

strike_rate = (
    (runs_scored / balls_faced) * 100
)

strike_rate = strike_rate[
    balls_faced >= 500
]

strike_rate = strike_rate.sort_values(
    ascending=False
)

print("\nTOP 10 STRIKE RATES (MIN 500 BALLS)")
print(strike_rate.head(10))

strike_rate.head(10).to_csv(
    "outputs/datasets/top_strike_rates.csv"
)

plt.figure(figsize=(10, 6))
strike_rate.head(10).plot(kind="bar")

plt.title("Top Strike Rates (Min 500 Balls)")
plt.xlabel("Player")
plt.ylabel("Strike Rate")

plt.tight_layout()

plt.savefig(
    "outputs/charts/top_strike_rates.png"
)

plt.close()

# ==========================================
# ECONOMY RATE ANALYSIS
# ==========================================

runs_conceded = (
    deliveries.groupby("bowler")
    ["total_runs"]
    .sum()
)

balls_bowled = (
    deliveries.groupby("bowler")
    .size()
)

economy = (
    runs_conceded /
    (balls_bowled / 6)
)

economy = economy[
    balls_bowled >= 300
]

economy = economy.sort_values()

print("\nTOP 10 BEST ECONOMY BOWLERS")
print(economy.head(10))

economy.head(10).to_csv(
    "outputs/datasets/best_economy_bowlers.csv"
)

plt.figure(figsize=(10, 6))
economy.head(10).plot(kind="bar")

plt.title("Best Economy Bowlers")
plt.xlabel("Bowler")
plt.ylabel("Economy Rate")

plt.tight_layout()

plt.savefig(
    "outputs/charts/best_economy_bowlers.png"
)

plt.close()

# ==========================================
# SUMMARY REPORT
# ==========================================

with open(
    "outputs/datasets/player_analysis_report.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("IPL PLAYER ANALYSIS REPORT\n")
    f.write("=" * 50 + "\n\n")

    f.write("TOP RUN SCORERS\n")
    f.write(str(runs.head(10)))
    f.write("\n\n")

    f.write("TOP SIX HITTERS\n")
    f.write(str(top_sixes.head(10)))
    f.write("\n\n")

    f.write("TOP WICKET TAKERS\n")
    f.write(str(top_bowlers.head(10)))

print("\n" + "=" * 60)
print("PLAYER ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nFiles Generated Successfully:")
print("outputs/charts/")
print("outputs/datasets/")