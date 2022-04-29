import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("thai_tourism.csv")

df["Receipts (bn $)"].corr(df["% of GNP"])  # 0.9324892611735859

correlation_matrix = df.corr()

correlation_matrix
