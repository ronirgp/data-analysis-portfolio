import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("supermarket_sales.csv")

print("=== First 5 Rows ===")
print(df.head())

print("\n=== Dataset Shape ===")
print(df.shape)

print("\n=== Sales by Product Line ===")
product_sales = df.groupby("Product line")["Total"].sum()
print(product_sales)

# Chart
product_sales.plot(kind="bar", color="green")
plt.title("Sales by Product Line")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("product_sales.png")
plt.show()

print("\n=== Best Product Line ===")
print(product_sales.idxmax())