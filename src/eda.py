import pandas as pd
import matplotlib.pyplot as plt
import os

# =====================================
# CREATE OUTPUT FOLDERS
# =====================================

os.makedirs("outputs/charts", exist_ok=True)
os.makedirs("outputs/datasets", exist_ok=True)

# =====================================
# LOAD DATA
# =====================================

matches = pd.read_csv("data/clean_matches.csv")

print("=" * 60)
print("IPL EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# =====================================
# TOTAL MATCHES
# =====================================

total_matches = matches.shape[0]

print(f"\nTotal Matches: {total_matches}")

# =====================================
# TOTAL TEAMS
# =====================================

teams = pd.unique(
    matches[["team1", "team2"]]
    .values
    .ravel()
)

print(f"Total Teams: {len(teams)}")

# =====================================
# TEAM WINS ANALYSIS
# =====================================

team_wins = matches["winner"].value_counts()

print("\nTop Winning Teams:")
print(team_wins.head(10))

team_wins.to_csv(
    "outputs/datasets/team_wins.csv"
)

plt.figure(figsize=(10, 6))

team_wins.head(10).plot(kind="bar")

plt.title("Top 10 IPL Teams by Wins")
plt.xlabel("Teams")
plt.ylabel("Wins")

plt.tight_layout()

plt.savefig(
    "outputs/charts/top_teams_wins.png"
)

plt.close()

# =====================================
# TOSS ANALYSIS
# =====================================

toss_wins = matches["toss_winner"].value_counts()

print("\nTop Toss Winning Teams:")
print(toss_wins.head(10))

toss_wins.to_csv(
    "outputs/datasets/toss_wins.csv"
)

plt.figure(figsize=(10, 6))

toss_wins.head(10).plot(kind="bar")

plt.title("Top Teams Winning Toss")
plt.xlabel("Teams")
plt.ylabel("Toss Wins")

plt.tight_layout()

plt.savefig(
    "outputs/charts/toss_analysis.png"
)

plt.close()

# =====================================
# TOSS IMPACT ANALYSIS
# =====================================

toss_match_wins = (
    matches["toss_winner"]
    == matches["winner"]
).sum()

toss_advantage = (
    toss_match_wins / len(matches)
) * 100

print(
    f"\nToss Winner Also Won Match: {toss_advantage:.2f}%"
)

# =====================================
# VENUE ANALYSIS
# =====================================

if "venue" in matches.columns:

    venue_matches = (
        matches["venue"]
        .value_counts()
        .head(10)
    )

    print("\nTop Venues:")
    print(venue_matches)

    venue_matches.to_csv(
        "outputs/datasets/top_venues.csv"
    )

    plt.figure(figsize=(12, 6))

    venue_matches.plot(kind="bar")

    plt.title("Top 10 IPL Venues")
    plt.xlabel("Venue")
    plt.ylabel("Matches Hosted")

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/venue_analysis.png"
    )

    plt.close()

# =====================================
# CITY ANALYSIS
# =====================================

if "city" in matches.columns:

    city_matches = (
        matches["city"]
        .value_counts()
        .head(10)
    )

    print("\nTop Cities:")
    print(city_matches)

    city_matches.to_csv(
        "outputs/datasets/top_cities.csv"
    )

# =====================================
# SEASON ANALYSIS
# =====================================

if "season" in matches.columns:

    season_matches = (
        matches["season"]
        .value_counts()
        .sort_index()
    )

    print("\nMatches Per Season:")
    print(season_matches)

    season_matches.to_csv(
        "outputs/datasets/season_analysis.csv"
    )

# =====================================
# TEXT REPORT
# =====================================

with open(
    "outputs/datasets/eda_report.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("IPL EDA REPORT\n")
    f.write("=" * 50 + "\n\n")

    f.write(f"Total Matches: {total_matches}\n")
    f.write(f"Total Teams: {len(teams)}\n\n")

    f.write("Top Winning Teams\n")
    f.write(str(team_wins.head(10)))
    f.write("\n\n")

    f.write("Top Toss Winning Teams\n")
    f.write(str(toss_wins.head(10)))
    f.write("\n\n")

    if "venue" in matches.columns:
        f.write("Top Venues\n")
        f.write(str(venue_matches))
        f.write("\n\n")

print("\nEDA COMPLETED SUCCESSFULLY")

print("\nGenerated Files:")

print("outputs/charts/")
print("  - top_teams_wins.png")
print("  - toss_analysis.png")
print("  - venue_analysis.png")

print("\noutputs/datasets/")
print("  - team_wins.csv")
print("  - toss_wins.csv")
print("  - top_venues.csv")
print("  - eda_report.txt")