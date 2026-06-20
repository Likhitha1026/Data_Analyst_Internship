import pandas as pd
df = pd.read_excel("samplesuperstore_cleaned.xlsx")
top_products = df.groupby("Product Name")["Sales"].sum()
top_products = top_products.sort_values(ascending=False)
print(top_products.head(5))