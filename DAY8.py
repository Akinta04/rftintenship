#CREATE DATABASE:
import pandas as pd
data = { "NAME":["A","B","C","D"],"DEPT":["IT","HR","IT","HR"],"SALARY":[50000,40000,60000,45000]}
df =pd.DataFrame(data) 
print("DATABASE:\n",df)

#AVERAGE SALARY PER DEPARTMENT
AVERAGE_SALARY=df.groupby("DEPT")["SALARY"].mean()
print("AVERAGE SALARY PER DEPARTMENT\n",AVERAGE_SALARY)

#highest paid employee per department
HIGHEST_PAID = df.loc[df.groupby("DEPT")["SALARY"].idxmax()]
print("Highest Paid Employee Per Department:\n",HIGHEST_PAID)

#COUNT EMPLOYEES PER DEPARTMENT
COUNT_EMP=df.groupby("DEPT")["NAME"].count()
print("Employee Count per Department:\n",COUNT_EMP)

#SORT DEPARTMENTS BY AVERAGE SALARY
sorted_avg=AVERAGE_SALARY.sort_values(ascending=False)
print("SORT DEPARTMENTS BY AVERAGE SALARY:\n",sorted_avg)


