#Sales data analyzer
import pandas as pd
df= pd.read_csv("SALES.CSV")
#total sales per product
df['TOTAL']=df['QUANTITY']*df['PRICE']
print(df)
sales_per_product=df.groupby('PRODUCT')['TOTAL'].sum()
print("Total sales per product:",sales_per_product)
#total revenue
total_revenue=df['TOTAL'].sum()
print("Total revenue is:",total_revenue)
# top selling product
top_product=sales_per_product.idxmax()
print(top_product)
# sort by revenue 
sorted_revenue=df.sort_values("TOTAL")
print(sorted_revenue)