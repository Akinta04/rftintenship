import matplotlib.pyplot as plt
#DATASET
dates = ["MON","TUE","WED","THU","FRI"]
sales=[200,250,300,280,350]

#FIND HIGHEST AND LOWEST SALES
max_sales = max(sales)
min_sales = min(sales)

max_day =dates[sales.index(max_sales)]
min_day =dates[sales.index(min_sales)]

#create line plot
plt.plot(dates,sales,linestyle = '-',color = 'green',label="Sales Trend")
#HIGHLIGHT HIGHEST SALES DAY
plt.scatter(max_day,max_sales,color = 'blue',label="HIGHEST SALES")
#HIGHLIGHT LOWEST SALES DAY
plt.scatter(min_day,min_sales,color = 'red',label="LOWEST SALES")
#ADD LABELS AND TITLE
plt.xlabel("DATES")
plt.ylabel("SALES")
plt.title("SALES TREND VISUALIZATION")
plt.legend()
plt.show()
