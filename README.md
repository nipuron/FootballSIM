# Premier League Monte Carlo Simulation

## Overview
This project simulates the Premier League 2025/2026 season using a Monte Carlo method based on historical data. It uses a Poisson distribution to model match outcomes based on the attack and defense strengths of teams over the last 5 years.

## How it Works
1. **Data Ingestion:** Loads historical home/away performance data (Goals Scored/Conceded) from the 2020/21 season to present.
2. **Team Modeling:** Calculates a weighted average of performance over the last 5 seasons, giving higher importance to recent seasons.
3. **Match Simulation:** For every fixture in the season, goals are simulated using the poisson distribution.
   Where $\lambda$ (expected goals) is derived from the home team's attack strength vs. the away team's defense strength.
4. **Monte Carlo Loop:** The season is simulated $N$ times (default: 1000) to smooth out variance and produce a predicted final league table.

## Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install pandas numpy scipy
