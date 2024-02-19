### INF601 - Advanced Programming in Python
### Samuel Ayers
### Mini Project 2

#import pandas, and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

#create pandas dataframe called tvShows from csv data
tvShows = pd.read_csv("IMDB.csv", index_col=0)

tvShows.head(10)["Rating"].plot()
plt.show()

