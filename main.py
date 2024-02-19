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
booksPandasFrame = pd.read_csv("books.csv", on_bad_lines='skip')


"""PLOT ONE, Average, Low, Min book rating, FINISHED"""

averageBookRating = (booksPandasFrame["average_rating"].mean())
highestBookRating = (booksPandasFrame["average_rating"].max())
lowestBookRating = (booksPandasFrame["average_rating"].min())

labels = ['Average', 'Highest', 'Lowest']
values = [averageBookRating, highestBookRating, lowestBookRating]

plt.bar(labels, values)

plt.title("Book Rating Statistics")
plt.ylabel('Rating')
#savefile = "charts/book statistics.png"
#plt.savefig(savefile)

"""PLOT TWO, UNSTARTED"""
plt.scatter(booksPandasFrame["publication_date"], booksPandasFrame["average_rating"])
plt.show()

"""PLOT THREE, UNSTARTED"""
#tvShows.head(25)["Rating"].plot.density()
#plt.show()

"""PLOT FOUR, UNSTARTED"""
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