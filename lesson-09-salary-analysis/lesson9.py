import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

print("=== 1. First Look ===")
print(df.head())

print("\n=== 2. Average Salary by Department ===")
print(df.groupby("Department")["Salary"].mean())

print("\n=== 3. Highest Paid Employee ===")
print(df.loc[df["Salary"].idxmax()])

print("\n=== 4. Salary Statistics ===")
print(df["Salary"].describe())

# Chart
df.groupby("Department")["Salary"].mean().plot(kind="bar", color=["blue","green","orange"])
plt.title("Average Salary by Department")
plt.ylabel("Salary ($)")
plt.tight_layout()
plt.savefig("salary_chart.png")
plt.show()