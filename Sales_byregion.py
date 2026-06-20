import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("samplesuperstore_cleaned.xlsx")
sales_by_region = df.groupby("Region")["Sales"].sum()
print(sales_by_region)
sales_by_region.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()