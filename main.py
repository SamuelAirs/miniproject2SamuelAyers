### INF601 - Advanced Programming in Python
### Samuel Ayers
### Mini Project 2
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path



"""         FUNCTION: SAVES CHARTS TO FILE"""
#function for saving and showing plots
def saveChartToFile(chartName):
    savefile = "charts/" + chartName + ".png"
    plt.savefig(savefile)
    plt.show()
    plt.close()


"""         FUNCTION: CREATES CHARTS FOLDER"""
def attemptToCreateChartFolder():
    #create charts folder
    try:
        Path("charts").mkdir()
    except FileExistsError:
        pass


"""         FUNCTION: PLOT ONE, NEEDS POLISH"""
#shows average rating, highest rating, lowest rating
def createPlotOne():
    plt.figure()
    title = "Book Rating Statistics"

    averageBookRating = (booksPandasFrame["average_rating"].mean())
    highestBookRating = (booksPandasFrame["average_rating"].max())
    lowestBookRating = (booksPandasFrame["average_rating"].min())

    labels = ['Average', 'Highest', 'Lowest']
    values = [averageBookRating, highestBookRating, lowestBookRating]


    plt.title(title)
    plt.ylabel('Rating')

    plt.bar(labels, values)

    saveChartToFile(title)


"""         FUNCTION: PLOT TWO, NEEDS POLISH"""
#creates a function showing year and rating
def createPlotTwo():
    plt.figure()
    title = "Books Published in 1998"

    booksFrom1998 = []

    for date in booksPandasFrame["publication_date"]:
        if str(1998) in date:
            booksFrom1998.append(date)

    Months = {"January": 0,
              "February": 0,
              "March": 0,
              "April": 0,
              "May": 0,
              "June": 0,
              "July": 0,
              "August": 0,
              "September": 0,
              "October": 0,
              "November": 0,
              "December": 0}

    for i in range(len(booksFrom1998)):
        monthDayYearList = booksFrom1998[i].split('/')
        if monthDayYearList[0] == '1':
            Months["January"] += 1
        elif monthDayYearList[0] == '2':
            Months["February"] += 1
        elif monthDayYearList[0] == '3':
            Months["March"] += 1
        elif monthDayYearList[0] == '4':
            Months["April"] += 1
        elif monthDayYearList[0] == '5':
            Months["May"] += 1
        elif monthDayYearList[0] == '6':
            Months["June"] += 1
        elif monthDayYearList[0] == '7':
            Months["July"] += 1
        elif monthDayYearList[0] == '8':
            Months["August"] += 1
        elif monthDayYearList[0] == '9':
            Months["September"] += 1
        elif monthDayYearList[0] == '10':
            Months["October"] += 1
        elif monthDayYearList[0] == '11':
            Months["November"] += 1
        elif monthDayYearList[0] == '12':
            Months["December"] += 1
    listOfMonths = (Months.keys())
    listOfValues = (Months.values())
    plt.bar(listOfMonths, listOfValues)
    saveChartToFile(title)




"""         FUNCTION: PLOT THREE, NEEDS POLISH"""
#creates a plot of top five authors with most books on list
def createPlotThree():
    plt.figure(figsize=(16, 10))
    title = "Top 5 Most Prolific Authors"
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

    #plt.xticks(rotation=25)
    plt.title(title)
    plt.xlabel("Authors")
    plt.ylabel("Number of Books")

    plt.bar(authors, counts)


    saveChartToFile(title)


"""         FUNCTION: PLOT FOUR, NEEDS POLISH"""
#plots the rating of a random book
def createPlotFour():
    sampleBooks = booksPandasFrame.sample(1)
    plt.figure()

    title = sampleBooks['title'].iloc[0]
    avgRate = sampleBooks['average_rating'].iloc[0]
    pubDate = sampleBooks['publication_date'].iloc[0]

    plt.yticks([])
    plt.xticks([])

    plt.title(title)
    plt.ylabel("Published in " + str(pubDate))
    plt.xlabel("Achieving an average rating of " + str(avgRate))

    plt.scatter(avgRate, pubDate)

    saveChartToFile('Random Book Rating and Year')


"""         FUNCTION: PLOT FIVE, NEEDS POLISH"""
# this chart shows the page count vs rating distribution for all books in the list
def createPlotFive():

    plt.figure()
    title = "Page Count vs Rating"
    plt.title(title)
    plt.xlabel("Page Count")
    plt.ylabel("Rating")
    plt.xlim(50, 1600)
    plt.ylim(2.5, 5)

    plt.scatter(booksPandasFrame['  num_pages'], booksPandasFrame['average_rating'])

    saveChartToFile(title)




"""||||||||||||MAIN ||||||||||||"""
#create pandas dataframe called tvShows from csv data
booksPandasFrame = pd.read_csv("books.csv", on_bad_lines='skip', parse_dates=['publication_date'])

#attempt to create chart folder
attemptToCreateChartFolder()

#create plots
createPlotOne()
createPlotTwo()
createPlotThree()
createPlotFour()
createPlotFive()
