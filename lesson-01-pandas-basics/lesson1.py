# Lesson 1: Loading data with Pandas
import pandas as pd

# Create a simple dataset
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Sales": [200, 350, 150],
    "Month": ["Jan", "Jan", "Jan"]
}

df = pd.DataFrame(data)

print(df)
print("\nTotal Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())