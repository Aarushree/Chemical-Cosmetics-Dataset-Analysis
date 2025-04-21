import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv(r"C:\Users\LENOVO\Desktop\python project\cosmetic_cleaned.csv")
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

#Bar Chart: Top 10 Most Common Chemicals
top_chemicals = df['ChemicalName'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_chemicals.values, y=top_chemicals.index, palette="viridis")
plt.title("Top 10 Most Common Chemicals in Cosmetics", fontsize=16)
plt.xlabel("Frequency")
plt.ylabel("Chemical Name")
plt.tight_layout()
plt.show()
top_chemicals = df['ChemicalName'].value_counts().head(10)
# Pie chart
plt.figure(figsize=(10, 10))
colors = plt.cm.viridis_r(np.linspace(0, 1, len(top_chemicals)))

plt.pie(
    top_chemicals.values,
    labels=top_chemicals.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops={'edgecolor': 'white'}
)

plt.title("Top 10 Most Common Chemicals in Cosmetics", fontsize=16)
plt.tight_layout()
plt.show()
