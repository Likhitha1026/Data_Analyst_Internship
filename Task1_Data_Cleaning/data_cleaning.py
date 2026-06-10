import pandas as pd

df = pd.read_csv("samplesuperstore.csv")

print("Missing Values:")
print(df.isnull().sum())

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

df["Processing Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

df.to_excel("samplesuperstore_cleaned.xlsx", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved as samplesuperstore_cleaned.xlsx")