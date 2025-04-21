import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\LENOVO\Desktop\python project\cosmetic_cleaned.csv")

df['InitialDateReported'] = pd.to_datetime(df['InitialDateReported'], errors='coerce')

df['ReportedYear'] = df['InitialDateReported'].dt.year

df = df[(df['ReportedYear'].notnull()) & (df['ReportedYear'] <= pd.Timestamp.now().year)]

# Line Chart: Chemical Usage Over Time ---
yearly_trend = df.groupby('ReportedYear').size()

plt.figure(figsize=(12, 6))
sns.lineplot(x=yearly_trend.index, y=yearly_trend.values, marker='o', color='blue')
plt.title("Trend of Chemical Usage Over Time", fontsize=16)
plt.xlabel("Year")
plt.ylabel("Number of Chemicals Reported")
plt.grid(True)
plt.tight_layout()
plt.show()

# Stacked Area Chart: Category-wise 
category_trend = df.groupby(['ReportedYear', 'PrimaryCategory']).size().unstack(fill_value=0)

category_trend = category_trend.sort_index()

# Plot stacked area chart
plt.figure(figsize=(14, 7))
category_trend.plot.area(colormap='Set2', alpha=0.9)
plt.title("Category-wise Trend of Chemical Reporting Over Time", fontsize=16)
plt.xlabel("Year")
plt.ylabel
