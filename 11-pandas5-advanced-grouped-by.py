# https://data-challenge.lighthouselabs.ca/challenge/11

import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')

# regular DataFrame
price_min_max = df.groupby(['neighborhood']).agg({'price' : ['min', 'max']})

# also a DataFrame
min_max = price_min_max['price']

# Series
diff = min_max['max'] - min_max['min']

diff.idxmax()


#### Lighthouse Labs Solution: iloc

grouped = price_min_max
(grouped.iloc[:,1] - grouped.iloc[:,0]).sort_values(ascending=False).head()

