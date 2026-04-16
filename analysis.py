import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/zara_products.csv")

# Clean data
df["price"] = pd.to_numeric(df["price"])
df["Sales Volume"] = pd.to_numeric(df["Sales Volume"])

# Feature engineering
df["Revenue"] = df["price"] * df["Sales Volume"]

# Summary statistics
print(df.describe())

# Promotion effect
promo_sales = df.groupby("Promotion")["Sales Volume"].mean()
print("\nAverage Sales by Promotion:")
print(promo_sales)

# Position performance
position_sales = df.groupby("Product Position")["Sales Volume"].mean()
print("\nAverage Sales by Position:")
print(position_sales)

# Plot
sns.barplot(x="Product Position", y="Sales Volume", data=df)
plt.title("Average Sales by Product Position")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("images/charts/position_sales.png")
plt.show()