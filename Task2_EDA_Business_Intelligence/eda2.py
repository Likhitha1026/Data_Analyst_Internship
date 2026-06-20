import pandas as py
import matplotlib.pyplot as plt
df=py.read_excel("samplesuperstore_cleaned.xlsx")
sales_by_category=df.groupby("Category")["Sales"].sum()
print(sales_by_category)
profit_by_category=df.groupby("Category")["Profit"].sum()
print(profit_by_category)