import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("store_data.csv")

# Calculate Revenue
df["Revenue"] = df["Units_Sold"] * df["Price"]

print("=== 1. First Look ===")
print(df.head())

print("\n=== 2. Missing Values ===")
print(df.isnull().sum())

print("\n=== 3. Revenue by Category ===")
cat_rev = df.groupby("Category")["Revenue"].sum()
print(cat_rev)

print("\n=== 4. Revenue by Region ===")
reg_rev = df.groupby("Region")["Revenue"].sum()
print(reg_rev)

print("\n=== 5. Best Product ===")
best = df.groupby("Product")["Revenue"].sum().idxmax()
print(best)

print("\n=== 6. Monthly Revenue ===")
monthly = df.groupby("Date")["Revenue"].sum()
print(monthly)

# Dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Chart 1
cat_rev.plot(kind="bar", ax=axes[0,0], color=["blue","green"], legend=False)
axes[0,0].set_title("Revenue by Category")

# Chart 2
reg_rev.plot(kind="bar", ax=axes[0,1], color=["orange","purple"], legend=False)
axes[0,1].set_title("Revenue by Region")

# Chart 3
df.groupby("Product")["Revenue"].sum().plot(kind="bar", ax=axes[1,0], color="red", legend=False)
axes[1,0].set_title("Revenue by Product")

# Chart 4
df.groupby("Date")["Revenue"].sum().plot(kind="line", ax=axes[1,1], color="blue", marker="o", legend=False)
axes[1,1].set_title("Revenue Over Time")

plt.suptitle("Store Sales Professional Report", fontsize=16)
plt.tight_layout()
plt.savefig("professional_report.png")
plt.show()

print("\nReport saved!")