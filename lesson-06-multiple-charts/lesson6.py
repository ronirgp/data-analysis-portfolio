import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [200, 350, 300, 500, 450],
    "Customers": [20, 35, 30, 50, 45],
    "Profit": [50, 90, 70, 150, 120]
}

df = pd.DataFrame(data)

# Create 3 charts in one window
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Chart 1 - Sales bar chart
df.plot(kind="bar", x="Month", y="Sales", ax=axes[0], color="blue", legend=False)
axes[0].set_title("Monthly Sales")

# Chart 2 - Customers line chart
df.plot(kind="line", x="Month", y="Customers", ax=axes[1], color="green", legend=False)
axes[1].set_title("Monthly Customers")

# Chart 3 - Profit bar chart
df.plot(kind="bar", x="Month", y="Profit", ax=axes[2], color="orange", legend=False)
axes[2].set_title("Monthly Profit")

plt.tight_layout()
plt.savefig("dashboard.png")
plt.show()

print("Dashboard saved!")