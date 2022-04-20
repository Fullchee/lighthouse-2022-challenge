import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')

neighbourhoods = df.groupby(['neighborhood'])

most_expensive_neighbourhood = neighbourhoods[['price']].mean().idxmax()

most_sqft_neighbourhood = neighbourhoods[['size_in_sqft']].mean().idxmax()

print(most_expensive_neighbourhood)
print(most_sqft_neighbourhood)

