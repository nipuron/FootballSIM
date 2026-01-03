import numpy as np
from scipy.stats import poisson

# Constants
SEASON_WEIGHTS = np.array([1/16, 1/16, 1/8, 1/4, 1/2])
GAMES_PER_SEASON = 19
SCALING_FACTOR = 0.5

class Match:
    def __init__(self,home_team,away_team):
        self.home_name=home_team.name
        self.away_name=away_team.name
        


        home_score=np.array(home_team.home_goals_scored)
        home_concede=np.array(home_team.home_goals_conceded)
        away_score=np.array(away_team.away_goals_scored)
        away_concede=np.array(away_team.away_goals_conceded)

        exp_goals_home=np.sum((home_score+away_concede)*SEASON_WEIGHTS)*SCALING_FACTOR/GAMES_PER_SEASON
        exp_goals_away=np.sum((away_score+home_concede)*SEASON_WEIGHTS)*SCALING_FACTOR/GAMES_PER_SEASON

        self.home_goals=poisson.rvs(exp_goals_home)
        self.away_goals=poisson.rvs(exp_goals_away)

    def print_info(self):
        print(f'Match:{self.home_name} vs {self.away_name}')
        print(f'Score:{self.home_goals} vs {self.away_goals}')


        

        