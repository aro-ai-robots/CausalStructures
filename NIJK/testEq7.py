from calNIJK import *
from equation_7 import *
from binner import loadData
import numpy as np

timeSeries = loadData('example_time_series.csv', 0)
timeSeries = np.array(timeSeries).T.tolist()
adjMat = loadData('example_adj_matrix.csv', 0)
adjMat = np.array(adjMat).T.tolist()

print(calEq7(adjMat, timeSeries))



