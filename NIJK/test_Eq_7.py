from call_nijk import *
from equation_7 import *
from binner import *
from get_all_graphs import *
from equation_7_params import *
import numpy as np

series = load_data('ecanruns_2/setting_7/pydump-percentage-af.data', 2)
time_series = binner(series, 5, 0, 0)
for index in range(0, len(time_series)):
    temp = time_series[index].tolist()
    time_series[index] = temp        
time_series = np.array(time_series).T.tolist()
all_probs = []
for start in range(0, len(time_series)-start):
    slider_series = time_series[start: start+n_length]
    graphs = get_graphs()
    prob_list = []
    for graph in graphs:
        adj_mat = graph
        prob_calc = call_eq_7(adj_mat, slider_series)
        prob_list.append(prob_calc)
    all_probs.append(prob_list)
print(all_probs)




