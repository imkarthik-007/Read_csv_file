import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("C://data/Sales Data Analysis.csv")
product_sales=data.groupby("Product").size().reset_index(name="sales_count")
print(product_sales)

plt.scatter(product_sales["Product"],product_sales["sales_count"])
plt.show()