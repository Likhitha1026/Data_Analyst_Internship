import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("samplesuperstore_cleaned.xlsx")
plt.figure(figsize=(8,5))
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()