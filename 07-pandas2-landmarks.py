import pandas as pd

df = pd.read_csv('paris_landmarks.csv')
df.head()
highest_price_index = df['price'].idxmax()

print(df.iloc[highest_price_index].landmark)

df['queue_time'].mean()

