
def getStateSet(timeSeries, nodeList):
	stateSet = set([]) 
	for i in timeSeries:
		if i in nodeList:
			stateSet.add(timeSeries[i])
		else:
			break
		stateSet = list(stateSet)
	return stateSet
	

