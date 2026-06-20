import pandas as py
import matplotlib.pyplot as plt
df=py.read_excel("samplesuperstore_cleaned.xlsx")
profit_by_category=df.groupby("Category")["Profit"].sum()
profit_by_category.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.show()