import numpy as np
def getAllPosGraphNums():
    allPosGraphs = []
    for i in range(0, 64):
        binString = str(bin(i))
        binString = binString[2:]
        while len(binString) < 6:
            binString = '0' + binString
        temp = []
        for char in binString:
            temp.append(int(char))
        allPosGraphs.append(temp)
    return allPosGraphs
    
    
def makeGraphs():
    allPosGraphs = getAllPosGraphNums()
    allGraphs = []
    for combo in allPosGraphs:
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
        allGraphs.append(g)
    return allGraphs

def cyclical(g):
    gSquare = np.matmul(g, g)
    gCube = np.matmul(g, gSquare)
    for _ in range(0,50):
        gCube = np.matmul(g, gCube)
    for row in gCube:
        for element in row:
            if element >= 1:
                return False
    return True

def getGraphs():
    graphs = []
    allGraphs = makeGraphs()
    for graph in allGraphs:
        if cyclical(graph):
            
            graphs.append(graph)
    print(graphs)
    return graphs

blah = getGraphs()
