from call_nijk import *
from binner import load_data
import numpy as np

time_series = load_data("example_time_series.csv", 0)
time_series = np.array(time_series).T.tolist()
adj_mat = load_data("example_adj_matrix.csv", 0)
adj_mat = np.array(adj_mat).T.tolist()
print(call_nijk(time_series, adj_mat, 2 , 1 , set([1])))
