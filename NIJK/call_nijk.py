def call_nijk(time_series, adj_mat, parents, i , j , k):

	"""************************************************************************************
					Check the input types
	************************************************************************************"""
	data_type_error_str = "Bad data type given to calNijk for "
	if not type(time_series) == list:
		print(data_type_error_str + "time_series\n" + "Data type given:" +
		str(type(time_series)) + " (list required)")
		return None
	if not type(time_series[0]) == list:
		print("Insuffecent data passed in time_series to calNijk")
		return None
	if not type(adj_mat) == list:
		print(data_type_error_str + "adj_mat\n" + "Data type given:" +
		str(type(adj_mat) + " (list required)"))
		return None
	if not type(adj_mat[0]) == list:
		print("Insuffecent data passed in adj_mat to calNijk")
		return None	
	if not type(i) == int:
		print(data_type_error_str + "i\n"+ "Data type given:" +
		str(type(i)) + " (int required)")
		return None
	if not (type(j) == float or type(j) == int):
		print(data_type_error_str + "j\n"+ "Data type given:" +
		str(type(j)) + " (number required)")
		return None
	if not type(k) == set:
		print(data_type_error_str + "k\n"+ "Data type given:" +
		str(type(k)) + " (set required)")
		return None
		
	
	"""************************************************************************************
					Calculate the Nijk
	************************************************************************************"""
	#parents = get_parents(i , adj_mat)
	my_val = 0
	if len(parents) == 0:
		print("No Parents!")
		return 0
	for row in time_series:
		#print(row[i])
		if row[i] == j:
			my_set = set([])
			for parent in parents:
				my_set.add(row[parent])
			#print(my_set)
			if(my_set == k):
				my_val = my_val + 1
	return my_val;
	
"""def get_child_nodes(adj_mat):
	child_nodes = {}
	
	i = 0
	for row in adj_mat:
		j = 0
		for elm in row:
			if elm == 1:
				if j in child_nodes:
					child_nodes[j].append(i)
				else:
					child_nodes[j] = [i]
	
	return child_nodes"""
	
def get_parents(i, adj_mat):
	parents = []
	index = 0
	for row in adj_mat:
		#print(adj_mat[i])
		if (row[i] == 1):
			parents.append(index)
		if not adj_mat[index][index] == 0:
			print("Diagnols not zero!")
			return None
		index = index + 1
	return parents
	


