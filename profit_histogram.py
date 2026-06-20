import pandas as py
import matplotlib.pyplot as plt
df=py.read_excel("samplesuperstore_cleaned.xlsx")
plt.hist(df["Profit"],bins=30)
plt.title("Profit Distribution")
plt.xlabel("profit")
plt.ylabel("Frequency")
plt.show()