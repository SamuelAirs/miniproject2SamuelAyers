### INF601 - Advanced Programming in Python
### Samuel Ayers
### Mini Project 2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tvShows = pd.read_csv("IMDB.csv", index_col=0)

print (tvShows.head())