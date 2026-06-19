import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Mouse"],
    "Units_Sold": [45, 120, 30, 200, 150],
    "Price": [1200, 800, 500, 50, 25]
}

df = pd.DataFrame(data)
df["Revenue"] = df["Units_Sold"] * df["Price"]

# Generate automated text report
today = datetime.now().strftime("%Y-%m-%d")

report = f"""
========================================
       WEEKLY SALES REPORT
       Generated: {today}
========================================

TOTAL REVENUE: ${df['Revenue'].sum():,.0f}
TOTAL UNITS SOLD: {df['Units_Sold'].sum()}
TOP PRODUCT: {df.loc[df['Revenue'].idxmax(), 'Product']}
AVERAGE PRICE: ${df['Price'].mean():,.2f}

--- PRODUCT BREAKDOWN ---
"""

for _, row in df.iterrows():
    report += f"{row['Product']:<15} Units: {row['Units_Sold']:<5} Revenue: ${row['Revenue']:,.0f}\n"

report += "\n========================================"

print(report)

# Save report to a text file automatically
with open("weekly_report.txt", "w") as f:
    f.write(report)

# Save chart automatically too
df.plot(kind="bar", x="Product", y="Revenue", color="teal", legend=False)
plt.title(f"Revenue by Product - {today}")
plt.tight_layout()
plt.savefig("weekly_chart.png")
plt.show()

print("\n✅ Report saved as weekly_report.txt")
print("✅ Chart saved as weekly_chart.png")