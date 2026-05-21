import matplotlib.pyplot as plt
# DATASET
CATEGORIES = ["FOOD","TRAVEL","SHOPPING"]
EXPENSES = [500,300,200]

#HIGHLIGHT HIGHEST CATEGORY
explode = [0.1,0,0]


#PIE CHART
plt.pie(EXPENSES,labels=CATEGORIES,shadow = True, wedgeprops ={'edgecolor': 'black'},explode =explode ,autopct = '%1.1f%%',
startangle = 90)
plt.title("CATEGORY WISE BREAKDOWN OF EXPENSES")
plt.show()