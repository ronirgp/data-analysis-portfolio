import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Data: Advertising spend vs Sales
data = {
    "Advertising": [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500],
    "Sales":       [5000, 6000, 7000, 8000, 9500, 9000, 11000, 12000]
}

df = pd.DataFrame(data)

# Prepare data for the model
X = df[["Advertising"]]   # Input (must be 2D)
y = df["Sales"]            # Output

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# The model learned a line: Sales = slope * Advertising + intercept
print("=== What the model learned ===")
print(f"Slope (m): {model.coef_[0]:.2f}")
print(f"Intercept (b): {model.intercept_:.2f}")
print(f"Equation: Sales = {model.coef_[0]:.2f} * Advertising + {model.intercept_:.2f}")

# Predict sales for a new advertising budget
new_budget = [[5000]]
prediction = model.predict(new_budget)
print(f"\n=== Prediction ===")
print(f"If we spend $5000 on advertising, predicted sales = ${prediction[0]:,.0f}")

# Visualize
plt.scatter(df["Advertising"], df["Sales"], color="blue", label="Real Data")
plt.plot(df["Advertising"], model.predict(X), color="red", label="Predicted Line")
plt.scatter(5000, prediction, color="green", s=100, label="New Prediction")
plt.title("Linear Regression - Advertising vs Sales")
plt.xlabel("Advertising ($)")
plt.ylabel("Sales ($)")
plt.legend()
plt.tight_layout()
plt.savefig("ml_prediction.png")
plt.show()