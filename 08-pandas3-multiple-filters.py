import pandas as pd
df = pd.read_csv('wine.csv')
df.head()

sub_13_wine_count = len(df[df['Alcohol'] < 13])
print(f"sub_13_wine_count: {sub_13_wine_count}")

class3_wine_count = len(df[df['Class'] == 3])
print(f"class3_wine_count: {class3_wine_count}")

magnesium_90_to_100_count = len(df[(df['Magnesium'] > 90) & (df['Magnesium'] < 100)])
print(f"magnesium_90_to_100_count: {magnesium_90_to_100_count}")

high_magnesium_low_alcohol_count = len(df[(df['Magnesium'] > 90) & (df['Alcohol'] < 13.5)])
print(f"high_magnesium_low_alcohol_count: {high_magnesium_low_alcohol_count}")

