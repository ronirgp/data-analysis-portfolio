import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Advertising": [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500],
    "Sales":       [5000, 6000, 7000, 8000, 9500, 9000, 11000, 12000],
    "Temperature": [30, 28, 35, 32, 20, 18, 25, 22]
}

df = pd.DataFrame(data)

# Correlation matrix
print("=== Correlation Matrix ===")
print(df.corr())

# Scatter plot - Advertising vs Sales
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.scatter(df["Advertising"], df["Sales"], color="blue")
plt.title("Advertising vs Sales")
plt.xlabel("Advertising ($)")
plt.ylabel("Sales ($)")

plt.subplot(1, 2, 2)
plt.scatter(df["Temperature"], df["Sales"], color="red")
plt.title("Temperature vs Sales")
plt.xlabel("Temperature")
plt.ylabel("Sales ($)")

plt.tight_layout()
plt.savefig("correlation.png")
plt.show()

print("\nDone!")