import pandas as pd

# Load data from a CSV file
df = pd.read_csv("sales_data.csv")

print("=== Full Data ===")
print(df)

print("\n=== Sales by Person ===")
print(df.groupby("Name")["Sales"].sum())

print("\n=== Best Seller ===")
best = df.groupby("Name")["Sales"].sum().idxmax()
print(best)