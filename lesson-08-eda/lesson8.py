import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [25, 30, 35, 28, 22],
    "Sales": [200, 350, 150, 400, 300],
    "Region": ["North", "South", "North", "South", "North"]
}

df = pd.DataFrame(data)

# EDA Steps
print("=== 1. First Look ===")
print(df.head())

print("\n=== 2. Shape ===")
print(df.shape)

print("\n=== 3. Data Types ===")
print(df.dtypes)

print("\n=== 4. Statistics ===")
print(df.describe())

print("\n=== 5. Any Missing Values? ===")
print(df.isnull().sum())

print("\n=== 6. Sales by Region ===")
print(df.groupby("Region")["Sales"].sum())

# Chart
df.groupby("Region")["Sales"].sum().plot(kind="bar", color=["blue", "green"])
plt.title("Sales by Region")
plt.tight_layout()
plt.savefig("eda_chart.png")
plt.show()