
"""*************************************************************************************

This Module is desined to get the STI values from a csv

*************************************************************************************"""

from logger_agent import *
import sys

#Path to the file that hold the STI values
input_fname = "STIseries_reduced.csv"

#Array that will hold the STI values
time_series = []

#Helper function for get time series
def load_arrays():

	#Open the file, iterate through the lines
	my_file = open(input_fname, "r")
	for line in my_file:
	
		#Get the next list, and add it to the time series
		next_list = get_list_from_line(line)
		time_series.append(next_list)
		
	#Close the file
	my_file.close()

#This function take a line of STI values and puts them int a list		
def get_list_from_line(line):

	#Initiilize the new list and trigger var
	new_array = []
	has_next = True
	
	#While there are STI value left...
	while has_next:
	
		#find will always return the location of the first occurance of the char in passed
		#to the function, thus, the in is inbetween that
		current_location = line.find(",")
		
		#Set the next number to None
		next_num = None
		
		#If there are no more commas, then we are on the last iteration.
		#if we are getting an error here, comment out the whole 'if' statement
		if (current_location == -1): 
		
			#end the loop
			has_next = False
			
			#try to capture the last num and turn it into an int
			try:
				next_num = line[:len(line)-1]#Remove the return char
				next_num = int(next_num)	
				
			#Kill the system and log the problem if an error occured
			except:
				log_error("Error in loading last STI value in get_time_series.py \n STI values end with a comma?")
				close_files()
				sys.exit("STI loading error")
			
		#if we are not on the last one
		else:
			#try to capture the num and turn it into an int
			try:
				next_num = line[0:current_location]
				line = line[current_location + 1:]
				next_num = int(next_num)
				
			#Kill the system and log the problem if an error occured	
			except:
				log_error("Error in loading 'some' STI value in get_time_series.py \n STI values may contain non integer?")
				close_files()
				sys.exit("Comma splicing error")
				
		#Kill the system and log the problem if an error occured
		if(next_num == None):
			log_error("Error in loading 'some' STI value in get_time_series.py \n next_num remained None")
			close_files()
			sys.exit("Comma splicing error")
			
		#Add the value to the array
		new_array.append(next_num)
	
	#Return the list	
	return new_array

#This is for getting the time series
def get_time_series():
	load_arrays()
	return time_series
