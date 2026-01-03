#%%
import numpy as np
import pandas as pd

import os
from Team import Team
from Match import Match

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#%%
def clean_df(table):
    table=table.drop(table.columns[0],axis=1)
    table=table.rename(columns={"Unnamed: 1":"Teams"})
    return table

def get_teams():
    seasons=['2021','2122','2223','2324','2425']
    home_res={}
    away_res={}
    team_names=[]

    for season in seasons:
        table_home=clean_df(pd.read_csv(f'PLData/PL{season}Home.csv'))
        table_away=clean_df(pd.read_csv(f'PLData/PL{season}Away.csv'))
        
        home_res[season]=table_home
        away_res[season]=table_away
        team_names.append(table_home['Teams'])

    current_table=clean_df(pd.read_csv(f'PLData/PL2526.csv'))
    current_team_names=current_table['Teams']

    team_names.append(current_team_names)
    team_names=pd.concat(team_names,ignore_index=True)
    team_names=team_names.unique()
    
    teams_map={}
    for team_name in team_names:
        team_obj=Team(team_name)

        for season in seasons:
            home=home_res[season]
            away=away_res[season]

            if team_name in home['Teams'].values:
                team_obj.add_season(home,away)
            else: 
                team_obj.add_season_min(home,away)

        teams_map[team_name]=team_obj
    return teams_map,current_team_names

def run_simulation(teams_map: dict,team_names: list,n_simulations:int=100)->pd.DataFrame:
    all_tables=[]

    for i in range(n_simulations):
        for team in teams_map:
            teams_map[team].reset()

        for h_name in team_names:
            for a_name in team_names:
                if h_name!=a_name:
                    home_team=teams_map[h_name]
                    away_team=teams_map[a_name]
                    match=Match(home_team,away_team)

                    home_team.add_match(match)
                    away_team.add_match(match)
        rows=[]
        for name in team_names:
            team_obj=teams_map[name]

            team_stats=team_obj.stats.copy()
            team_stats['Teams']=name

            rows.append(team_stats)
            
        all_tables.append(pd.DataFrame(rows))
    
    combined=pd.concat(all_tables)
    summary_table=combined.groupby('Teams').mean().reset_index()
    summary_table=summary_table.sort_values(by='Pts',ascending=False).reset_index(drop=True)

    return summary_table                
  
    

#%%
if __name__ == "__main__":
    
    teams_map,current_team_names=get_teams()
    final_standings=run_simulation(teams_map,current_team_names,1000)
    print(final_standings)
    
    
# %%
