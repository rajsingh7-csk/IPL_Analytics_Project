import streamlit as st
import pandas as pd
from PIL import Image
import os

# ======================================
# PAGE CONFIG
# ======================================

st.set_page_config(
    page_title="IPL Analytics Dashboard",
    page_icon="🏏",
    layout="wide"
)

# ======================================
# LOAD DATA
# ======================================

matches = pd.read_csv("data/clean_matches.csv")

# ======================================
# SIDEBAR
# ======================================

st.sidebar.title("🏏 IPL Analytics")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Team Analysis",
        "Player Analysis"
    ]
)

# ======================================
# HOME PAGE
# ======================================

if page == "Home":

    st.title("🏏 IPL Analytics Dashboard")

    st.markdown("---")

    total_matches = matches.shape[0]

    teams = pd.unique(
        matches[["team1", "team2"]]
        .values
        .ravel()
    )

    total_teams = len(teams)

    total_venues = (
        matches["venue"].nunique()
        if "venue" in matches.columns
        else 0
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Matches",
        total_matches
    )

    col2.metric(
        "Total Teams",
        total_teams
    )

    col3.metric(
        "Total Venues",
        total_venues
    )

    st.markdown("---")

    st.subheader("Project Overview")

    st.write("""
    This IPL Analytics Dashboard provides:

    - Team Performance Analysis
    - Toss Analysis
    - Venue Analysis
    - Player Performance Analysis
    - Strike Rate Analysis
    - Bowling Economy Analysis
    """)

# ======================================
# TEAM ANALYSIS
# ======================================

elif page == "Team Analysis":

    st.title("📊 Team Analysis")

    chart_path = "outputs/charts"

    team_charts = [
        ("Top Teams by Wins", "top_teams_wins.png"),
        ("Toss Analysis", "toss_analysis.png"),
        ("Venue Analysis", "venue_analysis.png")
    ]

    for title, filename in team_charts:

        filepath = os.path.join(
            chart_path,
            filename
        )

        if os.path.exists(filepath):

            st.subheader(title)

            image = Image.open(filepath)

            st.image(
                image,
                use_container_width=True
            )

        else:

            st.warning(
                f"{filename} not found."
            )

# ======================================
# PLAYER ANALYSIS
# ======================================

elif page == "Player Analysis":

    st.title("🏏 Player Analysis")

    chart_path = "outputs/charts"

    player_charts = [
        (
            "Top Run Scorers",
            "top_run_scorers.png"
        ),
        (
            "Top Players with Most Fours",
            "top_fours.png"
        ),
        (
            "Top Players with Most Sixes",
            "top_sixes.png"
        ),
        (
            "Top Wicket Takers",
            "top_wicket_takers.png"
        ),
        (
            "Top Strike Rates",
            "top_strike_rates.png"
        ),
        (
            "Best Economy Bowlers",
            "best_economy_bowlers.png"
        )
    ]

    for title, filename in player_charts:

        filepath = os.path.join(
            chart_path,
            filename
        )

        if os.path.exists(filepath):

            st.subheader(title)

            image = Image.open(filepath)

            st.image(
                image,
                use_container_width=True
            )

        else:

            st.warning(
                f"{filename} not found."
            )