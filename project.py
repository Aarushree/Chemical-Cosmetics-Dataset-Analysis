import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv(r"C:\Users\LENOVO\Desktop\python project\cosmetic file.csv")

print("📊 Initial Dataset Info:\n")
print(df.info())
print("\n🧮 Summary Statistics (Before Cleaning):\n")
print(df.describe(include='all'))

# Show missing values per column
print("\n❓ Missing Values Count (Before Cleaning):\n")
print(df.isnull().sum())

# -------------------------------
# 🧼 Data Preprocessing
# -------------------------------

# Create a working copy
df_clean = df.copy()

# 1. Remove duplicates
df_clean.drop_duplicates(inplace=True)

# 2. Drop columns with > 50% missing values
threshold = 0.5 * len(df_clean)
df_clean = df_clean.loc[:, df_clean.isnull().sum() < threshold]

# 3. Fill or impute missing values
if 'BrandName' in df_clean.columns:
    df_clean['BrandName'].fillna('Unknown', inplace=True)

if 'CSFId' in df_clean.columns:
    df_clean['CSFId'].fillna(-1, inplace=True)

if 'CSF' in df_clean.columns:
    df_clean['CSF'].fillna('Unknown', inplace=True)

if 'CasNumber' in df_clean.columns:
    df_clean['CasNumber'].fillna('Unknown', inplace=True)

# 4. Drop rows missing key values
key_columns = ['ProductName', 'CompanyName', 'ChemicalName', 'PrimaryCategory']
df_clean.dropna(subset=key_columns, inplace=True)

# 5. Convert date columns
date_columns = [
    'InitialDateReported', 'MostRecentDateReported', 'DiscontinuedDate',
    'ChemicalCreatedAt', 'ChemicalUpdatedAt', 'ChemicalDateRemoved'
]
for col in date_columns:
    if col in df_clean.columns:
        df_clean[col] = pd.to_datetime(df_clean[col], errors='coerce')

# -------------------------------
# ✅ Post-cleaning Inspection
# -------------------------------

print("\n✅ Cleaned Dataset Info:\n")
print(df_clean.info())

print("\n📈 Summary Statistics (After Cleaning):\n")
print(df_clean.describe(include='all'))

print("\n🔍 Missing Values Count (After Cleaning):\n")
print(df_clean.isnull().sum())

# Save the cleaned DataFrame to a new CSV file
cleaned_file_path = "cosmetic_cleaned.csv"
df_clean.to_csv(cleaned_file_path, index=False)

print(f"✅ Cleaned file saved as: {cleaned_file_path}")

# (Optional) Save the cleaned dataset
# df_clean.to_csv("cosmetic_cleaned.csv", index=False)
