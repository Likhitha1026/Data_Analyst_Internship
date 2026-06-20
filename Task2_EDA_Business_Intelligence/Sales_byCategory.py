import pandas as py
import matplotlib.pyplot as plt
df=py.read_excel("samplesuperstore_cleaned.xlsx")
sales_by_category=df.groupby("Category")["Sales"].sum()
sales_by_category.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()