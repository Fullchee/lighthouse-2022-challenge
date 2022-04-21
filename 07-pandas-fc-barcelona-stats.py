# https://data-challenge.lighthouselabs.ca/challenge/7

import pandas as pd

df = pd.read_csv('fc_barcelona.csv')
df.head()
points = df.Pts
games_played = df.MP
wins = df.W
losses = df.L
attendance = df.Attendance.dropna() # skipping missing values (NaN) because there were no fans during 2020-2021 season because of COVID

print(f"Max matches played: {games_played.max()}")
print(f"Average attendance: {round(attendance.mean(), 2)}")
print(f"Diff of wins and loss median: {wins.median() - losses.median()}")
print(f"Min number of wins in a season: {wins.min()}")
print(f"diff of max and min points: {points.max() - points.min()}")

