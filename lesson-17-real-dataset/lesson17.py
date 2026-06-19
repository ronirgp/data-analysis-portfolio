import pandas as pd
import matplotlib.pyplot as plt

# Load real Titanic dataset directly from the internet
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

try:
    df = pd.read_csv(url)
    print("=== Real Data Loaded! ===")
    print(df.head())
    print("\n=== Shape ===")
    print(df.shape)
    print("\n=== Columns ===")
    print(df.columns.tolist())
    
    print("\n=== Survival Rate ===")
    print(df["Survived"].value_counts())
    
    print("\n=== Survival by Gender ===")
    print(df.groupby("Sex")["Survived"].mean())
    
    # Chart
    df.groupby("Sex")["Survived"].mean().plot(kind="bar", color=["pink","blue"])
    plt.title("Survival Rate by Gender - Titanic")
    plt.ylabel("Survival Rate")
    plt.tight_layout()
    plt.savefig("titanic_survival.png")
    plt.show()
    
except Exception as e:
    print(f"Error loading data: {e}")