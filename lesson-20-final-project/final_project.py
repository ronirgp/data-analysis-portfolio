import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# === 1. LOAD & CLEAN ===
df = pd.read_csv("business_data.csv")
df["Revenue"] = df["Units"] * df["Price"]

print("=== FINAL PROJECT: Business Performance Report ===\n")
print(f"Total Records: {len(df)}")
print(f"Date Range: {df['Date'].min()} to {df['Date'].max()}")
print(f"Total Revenue: ${df['Revenue'].sum():,.0f}")
print(f"Total Marketing Spend: ${df['Marketing_Spend'].sum():,.0f}")

# === 2. EDA ===
print("\n=== Revenue by Region ===")
region_rev = df.groupby("Region")["Revenue"].sum()
print(region_rev)

print("\n=== Revenue by Product ===")
product_rev = df.groupby("Product")["Revenue"].sum()
print(product_rev)

# === 3. STATISTICS ===
print("\n=== Revenue Statistics ===")
print(df["Revenue"].describe())

# === 4. CORRELATION ===
print("\n=== Correlation: Marketing Spend vs Revenue ===")
corr = df["Marketing_Spend"].corr(df["Revenue"])
print(f"Correlation: {corr:.3f}")

# === 5. MACHINE LEARNING PREDICTION ===
X = df[["Marketing_Spend"]]
y = df["Revenue"]
model = LinearRegression()
model.fit(X, y)

new_spend = [[1000]]
prediction = model.predict(new_spend)
print(f"\n=== Prediction ===")
print(f"If we spend $1000 on marketing, predicted revenue = ${prediction[0]:,.0f}")

# === 6. DASHBOARD ===
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

region_rev.plot(kind="bar", ax=axes[0,0], color=["blue","orange"])
axes[0,0].set_title("Revenue by Region")

product_rev.plot(kind="bar", ax=axes[0,1], color=["green","red","purple"])
axes[0,1].set_title("Revenue by Product")

axes[1,0].scatter(df["Marketing_Spend"], df["Revenue"], color="blue")
axes[1,0].plot(df["Marketing_Spend"], model.predict(X), color="red")
axes[1,0].set_title(f"Marketing vs Revenue (corr={corr:.2f})")
axes[1,0].set_xlabel("Marketing Spend ($)")

df.groupby("Date")["Revenue"].sum().plot(kind="line", ax=axes[1,1], marker="o", color="teal")
axes[1,1].set_title("Revenue Over Time")
axes[1,1].tick_params(axis='x', rotation=45)

plt.suptitle("FINAL PROJECT: Business Performance Dashboard - Ronald", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig("final_dashboard.png")
plt.show()

print("\n🎓 FINAL PROJECT COMPLETE!")