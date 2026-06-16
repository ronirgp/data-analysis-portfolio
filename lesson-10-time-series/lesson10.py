import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Date": ["2024-01", "2024-02", "2024-03", "2024-04", 
              "2024-05", "2024-06", "2024-07", "2024-08"],
    "Revenue": [15000, 18000, 16000, 22000, 
                25000, 23000, 28000, 30000],
    "Expenses": [10000, 12000, 11000, 14000, 
                 15000, 14000, 16000, 17000]
}

df = pd.DataFrame(data)

# Calculate Profit
df["Profit"] = df["Revenue"] - df["Expenses"]

print("=== Monthly Data ===")
print(df)

print("\n=== Best Month ===")
print(df.loc[df["Revenue"].idxmax()])

print("\n=== Average Monthly Profit ===")
print(df["Profit"].mean())

# Chart
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Revenue"], marker="o", color="blue", label="Revenue")
plt.plot(df["Date"], df["Expenses"], marker="o", color="red", label="Expenses")
plt.plot(df["Date"], df["Profit"], marker="o", color="green", label="Profit")
plt.title("Revenue vs Expenses vs Profit Over Time")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("time_series.png")
plt.show()