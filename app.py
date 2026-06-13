import streamlit as st
import pandas as pd
import joblib
from PIL import Image
import os

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="IPL Analytics Dashboard",
    page_icon="🏏",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================

matches = pd.read_csv("data/clean_matches.csv")

# =====================================
# SIDEBAR NAVIGATION
# =====================================

st.sidebar.title("🏏 IPL Analytics")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Team Analysis",
        "Player Analysis",
        "Match Prediction",
        "Team Comparison",
        "Player Comparison"
    ]
)

# =====================================
# HOME
# =====================================

if page == "Home":

    st.title("🏏 IPL Analytics Dashboard")

    teams = sorted(
        list(set(matches["team1"]).union(set(matches["team2"])))
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Matches", len(matches))
    col2.metric("Total Teams", len(teams))
    col3.metric("Total Venues", matches["venue"].nunique())

    st.markdown("---")

    st.subheader("Project Overview")

    st.write("""
    This IPL Analytics Dashboard provides:

    • Team Performance Analysis  
    • Player Performance Analysis  
    • Toss Analysis  
    • Venue Analysis  
    • Match Winner Prediction (ML Model)  
    • Team Comparison  
    • Player Comparison  
    """)

# =====================================
# TEAM ANALYSIS
# =====================================

elif page == "Team Analysis":

    st.title("📊 Team Analysis")

    charts = [
        ("Top Teams Wins", "top_teams_wins.png"),
        ("Toss Analysis", "toss_analysis.png"),
        ("Venue Analysis", "venue_analysis.png")
    ]

    for title, file in charts:

        path = os.path.join("outputs/charts", file)

        st.subheader(title)

        if os.path.exists(path):
            st.image(Image.open(path), use_container_width=True)
        else:
            st.error(f"{file} not found")

# =====================================
# PLAYER ANALYSIS
# =====================================

elif page == "Player Analysis":

    st.title("🏏 Player Analysis")

    charts = [
        ("Top Run Scorers", "top_run_scorers.png"),
        ("Top Fours", "top_fours.png"),
        ("Top Sixes", "top_sixes.png"),
        ("Top Wicket Takers", "top_wicket_takers.png"),
        ("Top Strike Rates", "top_strike_rates.png"),
        ("Best Economy Bowlers", "best_economy_bowlers.png")
    ]

    for title, file in charts:

        path = os.path.join("outputs/charts", file)

        st.subheader(title)

        if os.path.exists(path):
            st.image(Image.open(path), use_container_width=True)
        else:
            st.error(f"{file} not found")

# =====================================
# MATCH PREDICTION
# =====================================

elif page == "Match Prediction":

    st.title("🏆 IPL Match Winner Prediction")

    model = joblib.load("models/winner_predictor.pkl")

    teams = sorted(list(set(matches["team1"]).union(set(matches["team2"]))))

    venues = sorted(matches["venue"].unique())

    team1 = st.selectbox("Team 1", teams)
    team2 = st.selectbox("Team 2", teams, index=1)

    venue = st.selectbox("Venue", venues)

    toss_winner = st.selectbox("Toss Winner", [team1, team2])

    toss_decision = st.selectbox("Toss Decision", ["bat", "field"])

    if st.button("Predict Winner"):

        input_df = pd.DataFrame({
            "team1": [team1],
            "team2": [team2],
            "venue": [venue],
            "toss_winner": [toss_winner],
            "toss_decision": [toss_decision]
        })

        prediction = model.predict(input_df)[0]

        st.success(f"🏆 Predicted Winner: {prediction}")

# =====================================
# TEAM COMPARISON
# =====================================

elif page == "Team Comparison":

    st.title("⚔️ Team Comparison")

    teams = sorted(list(set(matches["team1"]).union(set(matches["team2"]))))

    col1, col2 = st.columns(2)

    with col1:
        team_a = st.selectbox("Team A", teams)

    with col2:
        team_b = st.selectbox("Team B", teams, index=1)

    def stats(team):

        played = ((matches["team1"] == team) | (matches["team2"] == team)).sum()
        wins = (matches["winner"] == team).sum()
        win_pct = (wins / played * 100) if played > 0 else 0

        return played, wins, win_pct

    a = stats(team_a)
    b = stats(team_b)

    df = pd.DataFrame({
        "Metric": ["Matches", "Wins", "Win %"],
        team_a: [a[0], a[1], round(a[2], 2)],
        team_b: [b[0], b[1], round(b[2], 2)]
    })

    st.dataframe(df, use_container_width=True)

# =====================================
# PLAYER COMPARISON
# =====================================

elif page == "Player Comparison":

    st.title("🏏 Player Comparison")

    deliveries = pd.read_csv("data/deliveries.csv")

    players = sorted(deliveries["batter"].dropna().unique())

    col1, col2 = st.columns(2)

    with col1:
        player_a = st.selectbox("Player A", players)

    with col2:
        player_b = st.selectbox("Player B", players, index=1)

    def player_stats(player):

        data = deliveries[deliveries["batter"] == player]

        runs = data["batsman_runs"].sum()
        balls = data.shape[0]
        fours = (data["batsman_runs"] == 4).sum()
        sixes = (data["batsman_runs"] == 6).sum()

        strike_rate = (runs / balls * 100) if balls > 0 else 0

        return runs, balls, fours, sixes, strike_rate

    a = player_stats(player_a)
    b = player_stats(player_b)

    comp = pd.DataFrame({
        "Metric": ["Runs", "Balls", "Fours", "Sixes", "Strike Rate"],
        player_a: [a[0], a[1], a[2], a[3], round(a[4], 2)],
        player_b: [b[0], b[1], b[2], b[3], round(b[4], 2)]
    })

    st.dataframe(comp, use_container_width=True)