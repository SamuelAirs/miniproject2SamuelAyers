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
booksPandasFrame = pd.read_csv("books.csv", on_bad_lines='skip', parse_dates=['publication_date'])


"""PLOT ONE, Average, Low, Min book rating, NEEDS POLISH"""

plt.figure()

averageBookRating = (booksPandasFrame["average_rating"].mean())
highestBookRating = (booksPandasFrame["average_rating"].max())
lowestBookRating = (booksPandasFrame["average_rating"].min())

labels = ['Average', 'Highest', 'Lowest']
values = [averageBookRating, highestBookRating, lowestBookRating]



plt.title("Book Rating Statistics")
plt.ylabel('Rating')

plt.bar(labels, values)

savefile = "charts/Book Rating Statistics.png"
plt.savefig(savefile)
plt.show()
plt.close()
"""PLOT TWO, FINISHED"""
plt.figure()

firstPubDate = booksPandasFrame["publication_date"].min()
lastPubDate = booksPandasFrame["publication_date"].max()


plt.xticks([], [])
plt.xlabel("Dates from " + firstPubDate + " to " + lastPubDate)
plt.scatter(booksPandasFrame["publication_date"], booksPandasFrame["average_rating"])

savefile = "charts/Dates and Ratings.png"
plt.savefig(savefile)
plt.show()
plt.close()
"""PLOT THREE, pulls publication date and rating to show a scatter plot, NEEDS POLISH"""

plt.figure(figsize=(16, 10))
#pulls all authors from panda frames, some entries contain multiple authors though
authorListWithMultipleAuthors = booksPandasFrame["authors"].tolist()

#create list to hold single authors (split entries with multiple authors up)
authorListWithSingleAuthors = []

#loop that goes through list with multiple authors and splits them up so that each author is an individual index
for i in range(len(authorListWithMultipleAuthors)):
    authors = authorListWithMultipleAuthors[i]
    if "/" in authors:
        newList = authors.split('/')
        authorListWithSingleAuthors.extend(newList)
    else:
        authorListWithSingleAuthors.append(authors)

authorCount = {}
#loop that counts how many times each author occurs and adds to dictionary holding counts
for author in authorListWithSingleAuthors:
    if author not in authorCount:
        authorCount[author] = 1
    else:
        authorCount[author] += 1

sortedAuthors = sorted(authorCount.items(), key=lambda item: item[1], reverse=True)

topFiveAuthors = sortedAuthors[:5]
authors, counts = zip(*topFiveAuthors)

plt.xticks(rotation=45)
plt.title("Top 5 Most Prolific Authors")
plt.xlabel("Authors")
plt.ylabel("Number of Books")

plt.bar(authors, counts)


savefile = "charts/Most Prolific.png"
plt.savefig(savefile)
plt.show()
plt.close()

"""PLOT FOUR, IN PROGRESS"""
plt.figure()
#pulls 20 random books. Calculates book length versus score
plt.title("Page Count vs. Rating - 10 Random Titles")
plt.xlabel("Page Count")
plt.ylabel("Rating")

plt.show()
plt.close()
"""PLOT FIVE, UNSTARTED"""
