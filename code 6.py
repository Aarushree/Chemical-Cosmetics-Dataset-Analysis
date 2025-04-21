import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\LENOVO\Desktop\python project\cosmetic_cleaned.csv")
df['ProductName'] = df['ProductName'].fillna('Unknown Product')
df['PrimaryCategory'] = df['PrimaryCategory'].fillna('Uncategorized')

chemical_count = df.groupby('ProductName')['ChemicalName'].nunique().reset_index()
chemical_count.columns = ['ProductName', 'ChemicalCount']
product_frequency = df['ProductName'].value_counts().reset_index()
product_frequency.columns = ['ProductName', 'Frequency']
product_stats = pd.merge(chemical_count, product_frequency, on='ProductName')

# Scatter Plot - ChemicalCount vs Frequency
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=product_stats,
    x='ChemicalCount',
    y='Frequency',
    alpha=0.6,
    color='teal'
)
plt.title("Scatter Plot: Chemical Count vs Product Frequency", fontsize=16)
plt.xlabel("Number of Chemicals in Product")
plt.ylabel("Product Frequency in Dataset")
plt.grid(True)
plt.tight_layout()
plt.show()

# Boxplot - ChemicalCount by Primary Category

product_category = df[['ProductName', 'PrimaryCategory']].drop_duplicates()
product_stats_cat = pd.merge(product_stats, product_category, on='ProductName')
top_categories = product_stats_cat['PrimaryCategory'].value_counts().nlargest(6).index
filtered = product_stats_cat[product_stats_cat['PrimaryCategory'].isin(top_categories)]

plt.figure(figsize=(12, 7))
sns.boxplot(
    data=filtered,
    x='PrimaryCategory',
    y='ChemicalCount',
    palette='Set2'
)
plt.title("Boxplot: Chemical Count Distribution by Category", fontsize=16)
plt.xlabel("Primary Category")
plt.ylabel("Chemical Count per Product")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
