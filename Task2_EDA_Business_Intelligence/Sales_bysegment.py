import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("samplesuperstore_cleaned.xlsx")
sales_by_segment = df.groupby("Segment")["Sales"].sum()
print(sales_by_segment)
sales_by_segment.plot(kind="bar")
plt.title("Sales by Segment")
plt.xlabel("Segment")
plt.ylabel("Total Sales")

plt.show()