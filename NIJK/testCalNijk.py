from calNIJK import *
from binner import loadData
import numpy as np

time_series = loadData("example_time_series.csv", 0)
time_series = np.array(time_series).T.tolist()
adj_mat = loadData("example_adj_matrix.csv", 0)
adj_mat = np.array(adj_mat).T.tolist()
print(calNijk(time_series, adj_mat, 2 , 1 , set([1])))
