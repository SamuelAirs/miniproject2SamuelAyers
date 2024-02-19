### INF601 - Advanced Programming in Python
### Samuel Ayers
### Mini Project 2

#import pandas, and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


#create charts folder
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

#create pandas dataframe called tvShows from csv data
booksPandasFrame = pd.read_csv("books.csv")

"""PLOT ONE, SHITTY"""

#tvShows.head(25)["Rating"].plot()
#savefile = "charts/Top 25 Rating.png"
#plt.savefig(savefile)

#plt.show()

"""PLOT TWO, UNSTARTED"""
#plt.scatter(tvShows["Episodes"], tvShows["Rating"])
#plt.show()

"""PLOT THREE, UNSTARTED"""
#tvShows.head(25)["Rating"].plot.density()
#plt.show()

"""PLOT FOUR, FINISHED"""
#pulls top five tv shows from pandaframe
#topFiveTvShows = tvShows.head(5)
#finds min and max rating and creates buffer
#minRating = topFiveTvShows['Rating'].min() - .1
#maxRating = topFiveTvShows['Rating'].max() + .1
#creates bar plot
#topFiveTvShows.plot.bar(x='Name', y='Rating', legend=False, figsize=(8, 16))
#adds labels
#plt.title('Top 5 Tv Shows by Rating', fontsize='32')
#customize plot
#plt.xticks(rotation=45, fontsize='12')
#plt.ylim(minRating, maxRating)
#save file
#savefile = "charts/Top 5 Tv Shows By Rating.png"
#plt.savefig(savefile)

"""PLOT FIVE, UNSTARTED"""
#tvShows.plot(tvShows["Episodes"], tvShows["Rating"])
#plt.show()