# Import
import re

def generate_K_mers(data, k):
	# List of k-mer
	K_mer = []
	dict = {}

	# Initialization of the dictionary
	for d in data:
		for i in range(0, len(d[1]) - k + 1, 1): dict[d[1][i:i + k]] = 0;
		
	# Remove patterns not used
	for key in dict.keys():
		if bool(re.match('^[ACGT]+$', str(key))) == True: K_mer.append(str(key))
	
	# Return K_mer
	return K_mer


