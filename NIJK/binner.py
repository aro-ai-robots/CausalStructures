import sys
import csv
import numpy as np
import math
import pandas as pd

# Returns an array of the same size with values replaced by appropriate bin numbers.
# Bin ranges are found as ((SERIES_MAX - SERIES_MIN)/ NUMBER_BINS) * BIN_NUMBER + SERIES_MIN
def binner(series, numBins, length, start):
    series = loadData('pydump-percentage-af.data', 2)
    #print((binned))
    my_return = []
    for sect in series:
        newseries = binner_all(sect, 10,0,0)
        my_return.append(newseries)
    return my_return
def binner_all(series, numBins, length, start):
    # Find the bin range.
    minimum = min(series)
    diffRange = (max(series) - minimum)/float(numBins)

    # Create array of bin ranges.
    bins = [np.NINF]
    for idx in range(1, numBins):
        bins.append(minimum + (idx * diffRange))

    # length of 0, or any negative value, means length of the passed series.
    if length <= 0:
        length = len(series)

    # Return the newly binned series
    binned = np.digitize(series[start:start+length], bins, right=True)
   # print(binned)
    return binned


# Function to load data from vertical csv. Assumes no header.
def loadData(dataFile, skipColums):
    allSeries = []

    # With open handles file opening and closing automatically. Then handle file as csv.
    with open(dataFile) as z:
        f = csv.reader(open(dataFile, 'rU'), delimiter=',')
        firstFlag = 0

        # Go through csv line by line.
        for row in f:
            # Build allSeries according to how many columns are in the csv. 1 column = 1 series.
            if firstFlag == 0:
                firstFlag = 1
                for idx in range(skipColums, len(row)):
                    allSeries.append([])
                    
            # Append values to corresponding series.
            seriesTrack = 0
            for i in range(skipColums, len(row)):
                allSeries[seriesTrack].append(float(row[i]))
                seriesTrack = seriesTrack + 1
         
        return allSeries
"""
# Test plot to validate code.
import matplotlib.pyplot as plt
my_list = list(range(0, 428))
series = loadData('pydump-percentage-af.data')
#print(binner(series, 10,0,0))

#print((binned))
for sect in series:
    newseries = binner(sect, 10,0,0,1)
    #plt.plot(my_list,newseries)
#plt.show()
"""
