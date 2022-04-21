# https://data-challenge.lighthouselabs.ca/challenge/10

import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')

######## PART 1: groupby

# when we group by neighborhood, it creates a DataFrameGroupBy
# which is like having a DataFrame (df) for every neighborhood
# so if `df` is one table, then neighborhoods is 54 tables (for each neighborhood)

neighborhoods = df.groupby(['neighborhood'])  # type: DataFrameGroupBy

# this is how you print GroupBy objects
# neighborhoods.apply(display)                # UNCOMMENT LINE TO SEE NEIGHBORHOOD


######### PART 2: square brackets on the GROUP_BY

# SeriesGroupBy object: we slice a column (price) of the DataFrameGroupBy
# so it's like having 54 series for each neighborhoods
# not useful for us because when we slice, we lose all the data in the other columns
price_series_group_by = neighborhoods['price']
# price_series.apply(display)                 # UNCOMMENT LINE TO SEE NEIGHBORHOOD

# DataFrameGroupBy object when we make the key a list
group_by_price = df.groupby('neighborhood')[['price']]
# group_by_price.apply(display)               # UNCOMMENT LINE TO SEE DATA


# also a DataFrameGroupBy
# prints really nicely because it has multiple columns
# notice how it's multiple tables

# similar to above, there's still a table for each neighborhood
# except we have 2 columns
group_by_price_and_size = df.groupby('neighborhood')[['price', 'size_in_sqft']]
# group_by_price_and_size.apply(display)     # UNCOMMENT LINE TO SEE DATA


######## PART 3: Aggregation functions

# runs the mean() function on every table
# so each row is the price.mean() and size_in_sqft.mean() of every table (aka neighborhood)
# there should be 1 row for each neighbourhood
# notice how the key (it used to be an index, integer)
# is now the neighborhood name!
neighborhood_means = group_by_price_and_size.mean()
# display(neighborhood_means)                 # UNCOMMENT LINE TO SEE DATA

######### PART 4: Get the max

##### the lighthouse lab solution: sorting

## Highest Price

# the default sort is ascending=True
# when ascending=False, that means descending
descending_prices = neighborhood_means.sort_values('price', ascending=False)
# display(descending_prices)                 # UNCOMMENT LINE TO SEE DATA

# we just want the max so we do .head(1)
# the 1 means we just want 1 value
max_descending_price = descending_prices.head(1)
# display(max_descending_price)              # UNCOMMENT LINE TO SEE DATA
# Palm Jumeirah	4.379435e+06	2084.134831


## Largest Size
largest_size = neighborhood_means.sort_values('size_in_sqft', ascending=False).head(1)
# display(largest_size)                      # UNCOMMENT LINE TO SEE DATA
# Dubai Festival City	2445000.0	2778.4

##### using the strategy from 2 days ago
# because the key is the neighborhood name, we can use .idxmax()!
# because idxmax() returns the index (aka the key)

# idxmax returns the index of the max of each column
# neighborhood_means.idxmax()               # UNCOMMENT LINE TO SEE DATA

# price                 Palm Jumeirah
# size_in_sqft    Dubai Festival City

