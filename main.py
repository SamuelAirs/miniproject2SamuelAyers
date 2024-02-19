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
tvShows = pd.read_csv("IMDB.csv", index_col=0)

#PLOT ONE, SHITTY
tvShows.head(25)["Rating"].plot()
#savefile = "charts/Top 25 Rating.png"
#plt.savefig(savefile)
plt.show()

#PLOT TWO, UNSTARTED

#PLOT THREE, UNSTARTED

#PLOT FOUR, UNSTARTED

#PLOT FIVE, UNSTARTED
