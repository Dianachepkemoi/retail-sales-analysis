import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
df = pd.read_csv("../data/retail_sales.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Basic Overview
print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

print("\n--- Category Distribution ---")
print(df['Category'].value_counts())

# Monthly Sales Trend
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales['Month'].astype(str), monthly_sales['Sales'], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../visualizations/monthly_sales.png")
plt.show()

# Top 10 Products/Sub-Categories
top_subcats = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_subcats.values, y=top_subcats.index, palette='viridis')
plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Total Sales")
plt.tight_layout()
plt.savefig("../visualizations/top_products_bar.png")
plt.show()

# Sales vs Profit Scatter
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='Sales', y='Profit', hue='Category')
plt.title("Sales vs Profit by Category")
plt.tight_layout()
plt.savefig("../visualizations/sales_vs_profit.png")
plt.show()

# Save processed data
df.to_csv("../data/retail_sales_processed.csv", index=False)
print("\nAnalysis complete. Visualizations saved to the visualizations folder.")
