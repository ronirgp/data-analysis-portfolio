import pandas as pd
import matplotlib.pyplot as plt

# Create data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Sales": [600, 650, 400]
}

df = pd.DataFrame(data)

# Chart 1 - Bar chart
df.plot(kind="bar", x="Name", y="Sales", color="blue", legend=False)
plt.title("Total Sales by Person")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

print("Chart saved as sales_chart.png!")