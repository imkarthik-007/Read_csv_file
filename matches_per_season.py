import pandas as pd

data=pd.read_csv("C://data/matches.csv")
matches_per_season = data.groupby('Season').size().reset_index(name='Match_Count')
print(matches_per_season)