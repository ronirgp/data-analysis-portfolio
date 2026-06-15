import pandas as pd

df = pd.read_csv("dirty_data.csv")

print("=== Dirty Data ===")
print(df)

# Fix 1: Drop rows with no Name
df = df.dropna(subset=["Name"])

# Fix 2: Standardize names to Title Case
df["Name"] = df["Name"].str.title()

# Fix 3: Remove invalid Sales values
df = df[df["Sales"] != "UNKNOWN"]

# Fix 4: Fill missing Sales with 0
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(0)

print("\n=== Clean Data ===")
print(df)

print("\n=== Sales by Person ===")
print(df.groupby("Name")["Sales"].sum())