import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    "Employee": ["Alice", "Bob", "Charlie", "Diana", "Eve",
                 "Frank", "Grace", "Henry", "Isabel", "James"],
    "Salary": [45000, 48000, 47000, 46000, 52000,
               44000, 49000, 46500, 47500, 150000]
}

df = pd.DataFrame(data)
salaries = df["Salary"]

# Statistics
print("=== Basic Statistics ===")
print(f"Mean:   ${salaries.mean():,.0f}")
print(f"Median: ${salaries.median():,.0f}")
print(f"Mode:   ${salaries.mode()[0]:,.0f}")
print(f"Std Dev:${salaries.std():,.0f}")
print(f"Min:    ${salaries.min():,.0f}")
print(f"Max:    ${salaries.max():,.0f}")

print("\n=== Mean vs Median ===")
print(f"Mean is higher by: ${salaries.mean() - salaries.median():,.0f}")
print("This is because of the outlier pulling the mean up!")

# Chart
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Histogram
axes[0].hist(salaries, bins=6, color="blue", edgecolor="black")
axes[0].axvline(salaries.mean(), color="red", linestyle="--", label=f"Mean: ${salaries.mean():,.0f}")
axes[0].axvline(salaries.median(), color="green", linestyle="--", label=f"Median: ${salaries.median():,.0f}")
axes[0].set_title("Salary Distribution")
axes[0].set_xlabel("Salary ($)")
axes[0].legend()

# Box plot
axes[1].boxplot(salaries)
axes[1].set_title("Salary Box Plot")
axes[1].set_ylabel("Salary ($)")

plt.tight_layout()
plt.savefig("statistics.png")
plt.show()

print("\nDone!")