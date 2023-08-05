#Author: Rahul Kumania 
#Final Project 
#

from matplotlib import pyplot as plt
import math
import numpy as np
import pandas as pd
import seaborn as sns

##Opening the Top 10,000 movie dataset##
movies_data = pd.read_csv('/Users/rahulkumania/Desktop/Top_10000_Movies.csv')
#print(movie_data)

##Doing Explorartory commands on the datasets to look for some valuable insights## 
movies_data.head()

print(movies_data.shape)

movies_data.info()

'''Checking for the missing values'''
print(movies_data.isnull().sum())

'''Checking for the duplicates'''
print("Duplicates in the dataset", movies_data.duplicated().sum())

##Moving on to Data Visualization


'''Languages used in Top 10,000 movies'''

plt.figure(figsize=(10,8))
movies_data["original_language"].value_counts().plot(kind='barh')
plt.title("Languages used in movies", size=20)
plt.xlabel('Number of Movies')
plt.ylabel('Different Languages')
plt.show()

'''Narrowing it down'''

plt.figure(figsize=(10,8))
movies_data["original_language"].value_counts().head(10).plot(kind='barh')
plt.title("Top 10 Languages used in movies", size=20)
plt.xlabel('Number of Movies')
plt.ylabel('Different Languages')
plt.show()



'''Runtime in Top 10,000 movies'''

##deleting rows which have zero runtime and zero revenue
print(movies_data.columns[10:12])

print(movies_data[movies_data.columns[10:12]] == 0)

##Datasets rows which does not have zero runtime and revenue

new_movies_data = movies_data[~(movies_data[movies_data.columns[10:12]] == 0).any(axis = 1)]

plt.figure(figsize=(10,8))
sns.histplot(new_movies_data["runtime"])
plt.title("Runtime of top 10,000 movies", size=20)
plt.xlabel('Runtime in Minutes')
plt.show()

'''Looking for a relation in runtime and vote'''



yaxis = new_movies_data["runtime"]
xaxis = new_movies_data["vote_average"]
sns.scatterplot(xaxis,yaxis)
plt.title('Runtime Vs Voting')
plt.xlabel('Votes given to movie out of 10')
plt.ylabel('Runtime of Movies')
plt.show()

'''Looking for a relation in runtime and revenue'''

xaxis = new_movies_data["runtime"]
yaxis = new_movies_data["revenue"]
sns.scatterplot(xaxis,yaxis)
plt.title('Runtime Vs Revenue', size = 20)
plt.ylabel('Revenue of movies')
plt.xlabel('Runtime of Movies')
plt.show()

'''Top 10 genre of movies with high voting average'''

top_movies = new_movies_data[new_movies_data["genre"] != "[]"].sort_values(by="vote_average", ascending=False).head(10)
plt.figure(figsize=(5,5))
sns.countplot(top_movies["genre"])
plt.title("Top 10 Genre of Movies with High Ratings", size=20)
plt.xticks(rotation=90)
plt.show()

'''Looking for relation in Runtime and its popularity'''


g = sns.relplot(data= new_movies_data, x="runtime", y="popularity")
g.ax.axline(xy1=(10, 2), slope=.2, color="b", dashes=(5, 2))
plt.show()





