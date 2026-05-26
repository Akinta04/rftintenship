import pandas as pd
import matplotlib.pyplot as plt
#DATASET
data={'customer_id':[1,2,3,4,5,6,7,8],
       'age':[36,50,40,45,29,28,35,22],
       'spending':[5000,3000,4000,4500,3500,1500,3000,2000],
       'visits':[15,4,25,10,20,7,12,5]
       }
df = pd.DataFrame(data)
#GROUP CUSTOMERS BY SPENDING LEVELS
def segment_customer(spending):
    if spending>=4000:
        return 'High'
    elif spending>=2000:
        return 'Medium'
    else:
        return'Low'
df['category']=df['spending'].apply(segment_customer)
print("CUSTOMER DETAILS:\n",df)

#high value customer 
high_value=df[df['category']=='High']
print('HIGH VALUE CUSTOMER:\n',high_value)

#low engagement customer
low_engagement=df[df['category']=='Low']
print('LOW ENGAGEMENT CUSTOMER:\n',low_engagement)

#spending distribution
plt.figure(figsize=(8,5))
plt.hist(df['spending'],bins=5,edgecolor='black')
plt.title('CUSTOMER SPENDING DISTRIBUTION')
plt.xlabel('spending')
plt.ylabel('number of customers')
plt.show()

#customer categories
category_count=df['category'].value_counts()
plt.figure(figsize=(8,5))
plt.bar(category_count.index,category_count.values,edgecolor='black')
plt.title('customer categories')
plt.xlabel('category')
plt.ylabel('count')
plt.show()
#business strategies
print("BUSINESS STRATEGIES:")
print("1.send promotional offers to low_engagement user ")
print("2.offer premium membership to high-value customers")
print("3.provide discounts to medium customers to increase spending")