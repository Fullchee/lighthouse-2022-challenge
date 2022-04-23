import pandas as pd
df = pd.read_csv('aus_weather.csv')

summer_and_winter = df[(df['season'] == 'winter') | (df['season'] == 'summer')]

# a DF for each (location, season)
city_season = summer_and_winter.groupby(['Location', 'season'])


# Location     season
# Adelaide     summer    22.184554
#              winter    11.471689
# Albany       summer    19.727211
#              winter    12.332011
avg_temp = city_season['Temp9am'].mean()

# move summer and winter into columns
seasons_as_columns = avg_temp.unstack()

# Series
season_diff = seasons_as_columns.summer - seasons_as_columns.winter

season_diff['Adelaide':'Albury']
