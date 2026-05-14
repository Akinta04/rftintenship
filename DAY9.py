#create database
import pandas as pd
data={"Name":["A","B","C","D","E"],"Age":[37,27,21,30,18],"Salary":[45000,120000,80000,1000,60000]}
df=pd.DataFrame(data)
print(df)

#filter name and age 
filtered_data=df[(df["Salary"]>50000)&(df["Age"]<30)]

#display filtered results
print("FILTERED RESULTS:\n",filtered_data)

#save filtered data to csv file
filtered_data.to_csv("filtered.csv",index=False)
print("FILTERED DATA SAVED SUCCESSFULLY")