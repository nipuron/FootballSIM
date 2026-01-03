class Team:
    def __init__(self,name):
        self.name=name

        self.home_goals_scored=[]
        self.home_goals_conceded=[]
        self.away_goals_scored=[]
        self.away_goals_conceded=[]

        self.stats={'P':0,
                    'W':0,
                    'D':0,
                    'L':0,
                    'F':0,
                    'A':0,
                    '+/-':0,
                    'Pts':0}
        
        self.matches=[]

    def add_season(self,home,away):
        self.home_goals_scored.append(home.loc[home['Teams']==self.name,'F'].values[0])
        self.home_goals_conceded.append(home.loc[home['Teams']==self.name,'A'].values[0])

        self.away_goals_scored.append(away.loc[away['Teams']==self.name,'F'].values[0])
        self.away_goals_conceded.append(away.loc[away['Teams']==self.name,'A'].values[0])

    def add_season_min(self,home,away):
        self.home_goals_scored.append(home['F'].min())
        self.home_goals_conceded.append(home['A'].max())
        
        self.away_goals_scored.append(away['F'].min())
        self.away_goals_conceded.append(away['A'].max())
    
    def add_match(self,match):
        
        if match.home_name==self.name:
            our_goals=match.home_goals
            their_goals=match.away_goals
        else:
            our_goals=match.away_goals
            their_goals=match.home_goals

        self.stats['P']=self.stats['P']+1
        self.stats['F']=self.stats['F']+our_goals
        self.stats['A']=self.stats['A']+their_goals
        self.stats['+/-']=self.stats['+/-']+our_goals-their_goals
        
        if our_goals>their_goals:
            self.stats['W']=self.stats['W']+1
            self.stats['Pts']=self.stats['Pts']+3

        elif our_goals<their_goals:
            self.stats['L']=self.stats['L']+1
        else:
            self.stats['D']=self.stats['D']+1
            self.stats['Pts']=self.stats['Pts']+1

        self.matches.append(match)

    def reset(self):
        self.stats={'P':0,
                    'W':0,
                    'D':0,
                    'L':0,
                    'F':0,
                    'A':0,
                    '+/-':0,
                    'Pts':0}
        self.matches=[]

        
    def print_matches(self):
        print(f'{self.name} matches:')

        for match in self.matches:
            print(50*'-')
            match.print_info()

    def print_info(self):
        print(f"{self.name} since 2020/2021 season")
        print("_"*50)
        print(f'Goals scored home:{self.home_goals_scored}')
        print(f'Goals conceded home:{self.home_goals_conceded}')
        print(f'Goals scored away:{self.away_goals_scored}')
        print(f'Goals conceded away:{self.away_goals_conceded}')
        