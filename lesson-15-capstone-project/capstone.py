import pandas as pd
import matplotlib.pyplot as plt

# Load and prepare
df = pd.read_csv("sales_2024.csv")
df["Revenue"] = df["Units"] * df["Price"]

print("=== CAPSTONE SALES REPORT 2024 ===")
print(f"Total Records: {len(df)}")
print(f"Total Revenue: ${df['Revenue'].sum():,.0f}")
print(f"Date Range: {df['Date'].min()} to {df['Date'].max()}")

print("\n=== Top Salesperson ===")
top = df.groupby("Salesperson")["Revenue"].sum()
print(top)
print(f"Winner: {top.idxmax()} with ${top.max():,.0f}")

print("\n=== Revenue by Product ===")
products = df.groupby("Product")["Revenue"].sum()
print(products)

print("\n=== Revenue by Region ===")
regions = df.groupby("Region")["Revenue"].sum()
print(regions)

print("\n=== Monthly Revenue ===")
monthly = df.groupby("Date")["Revenue"].sum()
print(monthly)

# Final Dashboard
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Chart 1 - Salesperson
top.plot(kind="bar", ax=axes[0,0], color=["blue","green","orange"])
axes[0,0].set_title("Revenue by Salesperson")
axes[0,0].set_ylabel("Revenue ($)")

# Chart 2 - Product
products.plot(kind="bar", ax=axes[0,1], color=["red","purple","brown"])
axes[0,1].set_title("Revenue by Product")

# Chart 3 - Region
regions.plot(kind="pie", ax=axes[1,0], autopct="%1.1f%%")
axes[1,0].set_title("Revenue by Region")

# Chart 4 - Monthly trend
monthly.plot(kind="line", ax=axes[1,1], color="blue", marker="o")
axes[1,1].set_title("Monthly Revenue Trend")
axes[1,1].set_ylabel("Revenue ($)")

plt.suptitle("2024 Sales Capstone Report - Ronald", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig("capstone_report.png")
plt.show()

print("\n=== Report Complete! ===")