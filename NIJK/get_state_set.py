
def get_state_set(time_series, node_list):
	state_set = set([]) 
	for node in node_list:
		for row in time_series:
			state_set.add(row[node])
		#state_set = list(state_set)
	return state_set
	

