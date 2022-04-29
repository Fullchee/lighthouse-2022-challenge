import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("air_traffic_data.csv")

to_van = df[df["DEST"] == "YVR"]

from_city = to_van.groupby("ORIGIN_CITY_NAME")
passengers = from_city["PASSENGERS"]

passenger_count = passengers.sum()
city = passenger_count.idxmax()
people_count = passenger_count.max()

print(f"City: {city}, count: {people_count}")


# **Use a histogram to plot the probability distribution of distances for all routes in June 2021.**

# 1. figure out if January is 1 (it usually is) or 0
# months = df['MONTH'].drop_duplicates()
# display(months)

june_2021 = df[(df["MONTH"] == 6) & (df["YEAR"] == 2021)]

distances = june_2021["DISTANCE"]
plt.figure()
plt.hist(
    distances, bins=100
)  # Play around with the bin sizes when plotting your histogram
plt.show()
