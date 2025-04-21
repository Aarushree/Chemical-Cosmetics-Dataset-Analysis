import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\LENOVO\Desktop\python project\cosmetic_cleaned.csv")
category_counts = df['PrimaryCategory'].value_counts()

# Pie chart
plt.figure(figsize=(10, 10))
colors = plt.cm.Set3(np.linspace(0, 1, len(category_counts)))

plt.pie(
    category_counts.values,
    labels=category_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops={'edgecolor': 'white'}
)

plt.title("Share of Primary Cosmetic Categories", fontsize=16)
plt.tight_layout()
plt.show()
