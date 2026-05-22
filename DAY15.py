import pandas as pd
import matplotlib.pyplot as plt
#DATASET
data = {"DAY":["MON","TUE","WED","THU","FRI","SAT","SUN"],"SALES":[120,150,128,140,128,150,400]}
df=pd.DataFrame(data)
print(df)

# create subplots
plt.figure(figsize=(14,4))

#create line chart
plt.subplot(1,4,1)
plt.plot(df["DAY"],df["SALES"],marker='o')
plt.title("SALES TREND")
plt.xlabel("DAY")
plt.ylabel("SALES")

#BAR CHART
plt.subplot(1,4,2)
plt.bar(df["DAY"],df["SALES"])
plt.title("SALES COMPARISON")
plt.xlabel("DAY")
plt.ylabel("SALES")

#HISTOGRAM
plt.subplot(1,4,3)
plt.hist(df["SALES"],bins=5)
plt.title("SALES DISTRIBUTION")
plt.xlabel("DAY")
plt.ylabel("SALES")

#outliers detection
plt.subplot(1,4,4)
plt.boxplot(df["SALES"])
plt.title("OUTLIER DETECTION")
plt.ylabel("SALES")

plt.suptitle("STUDENT MARKS MINI DASHBOARD")
plt.show()

print("INSIGHTS:")
print("1.SALE WAS HIGHEST ON SUNDAY")
print("2.SALE WAS LOWEST ON WEDNESDAY")
print("3.SUNDAY'S SALES APPEARED AS AN OUTLIER")
print("4. OVERALL SALES WAS GOOD")