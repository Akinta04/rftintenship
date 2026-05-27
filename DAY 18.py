import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data={"MOVIE_NAME":["KGF","3 IDIOTS","SHERSHAAH","LEKH","CHHICHHORE"],"RATING":[8.8,7.5,9.1,7.5,8.4],"GENRE":["ACTION",
"COMEDY","WAR","ROMANCE","DRAMA"],"REVENUE":[1500,1200,800,500,950]}
#DATASET
df=pd.DataFrame(data)
print(df)

#HIGHEST RATED MOVIES
highest_rated=df.sort_values(by = "RATING",ascending=False)
print("HIGHEST RATED MOVIES:\n",highest_rated)

#MOST PROFITABLE GENRES
genre_revenue=df.groupby("GENRE")["REVENUE"].sum()
print("MOST PROFITABLE GENRES:\n",genre_revenue.sort_values(ascending = False))

#TOP 5 MOVIES
TOP5=df.sort_values(by="REVENUE",ascending=False).head(5)
print("TOP5:\n",TOP5)

#correlation between rating and revenue
correlation=df['RATING'].corr(df['REVENUE'])
print("correlation between rating and revenue:",correlation)

#visualization GENRE VS REVENUE
plt.figure(figsize=(8,5))
sns.barplot(x=genre_revenue.index,y=genre_revenue.values)
plt.title("GENRE VS REVENUE")
plt.xlabel("GENRE")
plt.ylabel("REVENUE")

#RATING DISTRIBUTION
plt.figure(figsize=(8,5))
sns.histplot(df["RATING"],bins=5)
plt.title("RATING DISTRIBUTION")
plt.xlabel("RATING")
plt.ylabel("COUNT")
plt.show()