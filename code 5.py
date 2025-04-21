import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\LENOVO\Desktop\python project\cosmetic_cleaned.csv")
df['BrandName'] = df['BrandName'].fillna('Unknown').str.strip()
top_categories = df['PrimaryCategory'].value_counts().nlargest(3).index
filtered = df[df['PrimaryCategory'].isin(top_categories)]
grouped = filtered.groupby(['PrimaryCategory', 'BrandName']).size().reset_index(name='ProductCount')
top_brands_per_category = (
    grouped.groupby('PrimaryCategory')
    .apply(lambda g: g.nlargest(5, 'ProductCount'))
    .reset_index(drop=True)
)

#Plot grouped bar chart
plt.figure(figsize=(14, 8))
sns.barplot(
    data=top_brands_per_category,
    x='BrandName',
    y='ProductCount',
    hue='PrimaryCategory'
)
plt.title("Top 5 Brands in Top 3 Product Categories", fontsize=16)
plt.xlabel("Brand Name")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)
plt.legend(title='Primary Category')
plt.tight_layout()
plt.show()
