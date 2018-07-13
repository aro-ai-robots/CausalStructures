import numpy as np
from equation_7_params import *
def get_all_pos_graph_nums():
    all_pos_graphs = []
    if (no_connections_enabled):
        start = 0
    else:
        start = 1
    for i in range(start, 64):
        bin_string = str(bin(i))
        bin_string = bin_string[2:]
        while len(bin_string) < 6:
            bin_string = '0' + bin_string
        temp = []
        for char in bin_string:
            temp.append(int(char))
        all_pos_graphs.append(temp)
    return all_pos_graphs
    
    
def make_graphs():
    all_pos_graphs = get_all_pos_graph_nums()
    all_graphs = []
    for combo in all_pos_graphs:
        g = np.zeros((3,3))
        count = 0
        i = 0
        for row in g:
            j = 0
            for col in row:
                if not j == i:
                    g[i][j] = combo[count]
                    count += 1
                j += 1
            i += 1
        all_graphs.append(g)
    return all_graphs

def cyclical(g):
    g_square = np.matmul(g, g)
    g_cube = np.matmul(g, g_square)
    #for _ in range(0,50):
      #  g_cube = np.matmul(g, g_cube)
    for row in g_cube:
        for element in row:
            if element >= 1:
                return False
    return True

def get_graphs():
    graphs = []
    all_graphs = make_graphs()
    for graph in all_graphs:
        if cyclical(graph):
            graph = graph.tolist()
            graphs.append(graph)
            
    #print(graphs)
    
    return graphs
