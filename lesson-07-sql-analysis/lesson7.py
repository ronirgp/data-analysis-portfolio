import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Create database and connect
conn = sqlite3.connect("sales.db")

# Create table and insert data
conn.execute("""
CREATE TABLE IF NOT EXISTS sales (
    name TEXT,
    product TEXT,
    amount REAL,
    month TEXT
)
""")

conn.execute("DELETE FROM sales")

data = [
    ("Alice", "Food", 200, "Jan"),
    ("Bob", "Electronics", 350, "Jan"),
    ("Charlie", "Food", 150, "Feb"),
    ("Alice", "Electronics", 400, "Feb"),
    ("Bob", "Food", 300, "Mar"),
    ("Charlie", "Electronics", 250, "Mar"),
]

conn.executemany("INSERT INTO sales VALUES (?,?,?,?)", data)
conn.commit()

# Query with SQL
df = pd.read_sql_query("SELECT product, SUM(amount) as Total FROM sales GROUP BY product", conn)

print("=== Sales by Product ===")
print(df)

# Chart
df.plot(kind="bar", x="product", y="Total", color="purple", legend=False)
plt.title("Sales by Product")
plt.tight_layout()
plt.savefig("sql_chart.png")
plt.show()

conn.close()
print("\nDone!")