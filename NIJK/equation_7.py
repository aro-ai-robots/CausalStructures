import scipy.special as sc
from call_nijk import *
from equation_7_params import *
from get_state_set import *
global alpha, lil_gamma

def call_eq_7(adj_mat, time_series):

	#initilize the result and get the number of nodes
	P_of_G_given_X = 1
	n = len(adj_mat)
	
	#Start the outer most product
	for i in range(0, n):
		parents = get_parents(i, adj_mat)
		P_of_G_given_X = P_of_G_given_X * (lil_gamma ** len(parents))
		per_state_set = get_state_set(time_series, parents)
		node_state_set = get_state_set(time_series, [i])
		#print("Here")
		if not type(per_state_set) == set:
			print("getStateSet returned invalid data type! Type: " +
				str(type(per_state_set)))
			return None
			
		#Do the second Product
		term_2 = 1
		#print(per_state_set)
		for k in per_state_set:
			alpha_i_k = float(alpha) / float(len(per_state_set)) #calc alpha
			#print(alpha_i_k)
			
			#Calculate Ni.k
			ni_k = 0
			for j in node_state_set:
				ni_k += call_nijk(time_series, adj_mat, parents, i, j , set([k]))
				
			#Calculate the term for k
			numerator  = sc.gamma(alpha_i_k)
			denominator = sc.gamma(alpha_i_k + ni_k)
			term_2 = (numerator)/(float(denominator))
			
			#Multiply term_2 and start the thrid product
			P_of_G_given_X = P_of_G_given_X * term_2
			for j in node_state_set:
			
				#Calculaste alpha and nijk
				alpha_i_j_k = float(alpha) / (float(len(node_state_set)) * 
					float(len(per_state_set)))
				nijk = call_nijk(time_series, adj_mat, parents, i, j , set([k]))
				
				#Calculate the term for k 
				numerator = sc.gamma(nijk + alpha_i_j_k)
				denominator = sc.gamma(alpha_i_j_k)
				term_3 = (numerator)/(float(denominator))
				
				#Multiply term_3
				P_of_G_given_X = P_of_G_given_X * term_3
	return P_of_G_given_X
