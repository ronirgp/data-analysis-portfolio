import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Employee": ["Alice", "Bob", "Charlie", "Diana", "Eve", 
                 "Frank", "Grace", "Henry", "Isabel", "James"],
    "Salary": [45000, 48000, 47000, 46000, 150000, 
               44000, 49000, 46500, 47500, 45500]
}

df = pd.DataFrame(data)

print("=== Salary Statistics ===")
print(df["Salary"].describe())

# Detect outliers using IQR method
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print(f"\n=== Normal Range ===")
print(f"Lower: ${lower:,.0f}")
print(f"Upper: ${upper:,.0f}")

outliers = df[(df["Salary"] < lower) | (df["Salary"] > upper)]
print(f"\n=== Outliers Found ===")
print(outliers)

# Chart
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.boxplot(df["Salary"])
plt.title("Salary Box Plot")
plt.ylabel("Salary ($)")

plt.subplot(1, 2, 2)
colors = ["red" if s > upper or s < lower else "blue" for s in df["Salary"]]
plt.bar(df["Employee"], df["Salary"], color=colors)
plt.title("Salaries - Red = Outlier")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("outliers.png")
plt.show()

print("\nDone!")