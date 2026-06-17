import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Region": ["North", "South", "North", "South", "North", "South", "North", "South"],
    "Category": ["Electronics", "Electronics", "Food", "Food", "Electronics", "Food", "Food", "Electronics"],
    "Month": ["Jan", "Jan", "Jan", "Jan", "Feb", "Feb", "Feb", "Feb"],
    "Sales": [5000, 4500, 300, 250, 6000, 280, 320, 5500]
}

df = pd.DataFrame(data)

# Pivot Table 1 - Sales by Region and Category
pivot1 = df.pivot_table(values="Sales", index="Region", columns="Category", aggfunc="sum")
print("=== Sales by Region and Category ===")
print(pivot1)

# Pivot Table 2 - Sales by Month and Region
pivot2 = df.pivot_table(values="Sales", index="Month", columns="Region", aggfunc="sum")
print("\n=== Sales by Month and Region ===")
print(pivot2)

# Chart
pivot1.plot(kind="bar", figsize=(8,5))
plt.title("Sales by Region and Category")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("pivot_chart.png")
plt.show()

print("\nDone!")