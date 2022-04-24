
import pandas as pd
df = pd.read_csv('nz_car_traffic.csv')

# regionName with the lowest total amount of light/heavy traffic
def get_region_with_least_traffic(type: str):
    light_traffic = df[df['classWeight'] == type]
    traffic_count = light_traffic.groupby('regionName')['trafficCount']
    least_traffic = traffic_count.sum().idxmin()
    print(f"Region with the least {type} Traffic: {least_traffic}")

get_region_with_least_traffic('Light')
get_region_with_least_traffic('Heavy')


months = df.groupby('month')['trafficCount'].sum()
months.plot(kind='bar')


# percent of trafficCount classified as heavy (classWeight) in 2020

# no need to filter by year
    # the data is already only for 2020
# twenty_twenty = df[(df['startDate'] >= '2020-01-01') & (df['startDate'] <= '2020-12-31')]

def count_traffic(type: str):
    traffic = df[df['classWeight'] == type]
    return traffic['trafficCount'].sum()


heavy_count = count_traffic('Heavy')
light_count = count_traffic('Light')

print(heavy_count)
print(light_count)

print((heavy_count / (heavy_count + light_count)) * 100)
