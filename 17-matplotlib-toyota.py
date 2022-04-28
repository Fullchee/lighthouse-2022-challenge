import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('toyota_cars.csv')
df.head()
twenty_twenty = df[df['Year'] == 2020]

grouped_by_category = twenty_twenty.groupby("Category")

count_of_each_category = grouped_by_category.size().sort_values(ascending=False)

plt.figure()
plt.bar(x = count_of_each_category.index, height = count_of_each_category.values)
plt.show()
