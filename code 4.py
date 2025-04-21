import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\LENOVO\Desktop\python project\cosmetic_cleaned.csv")
top_brands = df['BrandName'].value_counts().head(10)

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(x=top_brands.values, y=top_brands.index, palette='cubehelix')
plt.title("Top 10 Brands by Product Count", fontsize=16)
plt.xlabel("Number of Products")
plt.ylabel("Brand Name")
plt.tight_layout()
plt.show()
