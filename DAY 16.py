#DATASET
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {'Date': ['25-04-2026', '26-05-2026','27-04-2026', '25-06-2026','28-07-2026'],
'Product': ['Laptop', 'Mouse', 'Keyboard','Laptop', 'Mouse'],
'Region': ['North', 'South', 'East','Central', 'West'],
'Sales': [ 3000, 50000,2000,55000, None]
}
df = pd.DataFrame(data)

#handle missing values
print(df["Sales"].isnull().sum())
df["Sales"]= df["Sales"].fillna(df["Sales"].mean())
print(df)

#total sales per product
total = df.groupby("Product")["Sales"].sum()
print(total)

#region wise performance
region = df.groupby("Region")["Sales"].sum()
print(region.sort_values(ascending = False))

fig = plt.figure(figsize=(15,5))

#Sales trend
ax1 = fig.add_subplot(2,2,1)
df["Date"] =pd.to_datetime(df["Date"],dayfirst = True)
daily_sales = df.groupby("Date")["Sales"].sum()
sns.lineplot(x = daily_sales.index,y =daily_sales.values,ax = ax1,marker='o')
ax1.set_title("SALES TREND")
ax1.set_xlabel("Date")
ax1.set_ylabel("Sales")

#top products
ax2 = fig.add_subplot(2,2,2)
total = df.groupby("Product")["Sales"].sum()
ax2.bar(total.index,total.values)
ax2.set_title("TOP PRODUCTS")
ax2.set_xlabel("PRODUCTS")
ax2.set_ylabel("SALES")

#monthly growth analysis
ax3 = fig.add_subplot(2,2,3)
monthly_sales = df.resample("ME",on = "Date")["Sales"].sum()
sns.lineplot(x = monthly_sales.index,y = monthly_sales.values,marker = 'o',ax = ax3)
ax3.set_title("MONTHLY SALES GROWTH")
ax3.set_xlabel("Month")
ax3.set_ylabel("Sales")

#best performing region
print(region.sort_values(ascending = False).head(1))

print("INSIGHTS")
print("1. Laptop has highest sales.")
print("2. Central region performs best.")
print("3. Missing values handled using mean.")
print("4. Monthly sales varied across regions and products.")

plt.tight_layout()
plt.show()


