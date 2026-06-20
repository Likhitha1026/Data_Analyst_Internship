import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel("samplesuperstore_cleaned.xlsx")
corr = df[["Sales", "Profit", "Quantity", "Discount"]].corr()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()