import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
conn = sqlite3.connect("world.db")
df = pd.read_sql('select * from worldcities',conn)

plt.figure()
plt.hist(df['population'], bins = 40)
plt.show()

populations = df.groupby('country')['population']

country_pop = populations.sum()

most_populated = country_pop.sort_values(ascending = False)

most_populated.head(1).index.values[0]
