import pandas as pd
df = pd.read_csv('aus_weather.csv')
df = df[df["Location"] == "Melbourne"]
df["Temp9am"].plot(kind='hist')

# df["Rainfall"].plot(kind='box')
