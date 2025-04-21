#!/usr/bin/env python3

import random
import sys
import os

def generate_random_pairs(miRNA_list, n, filter):
	"""
	Generate random pairs of miRNAs from the given list. Do not include pairs that are already in the filter list.
	"""
	rnd_pairs = []
	while n > 0:
		# generate a random pair of miRNAs
		pair = random.sample(miRNA_list, 2)
		# check if the pair is already in the filter list regardless of the order
		if (pair[0], pair[1]) not in filter and (pair[1], pair[0]) not in filter:
			rnd_pairs.append(pair)
			n -= 1
	return rnd_pairs


if __name__ == "__main__":

	# read the mirna list as standard input
	try:
		miRNA_list = [line.strip() for line in sys.stdin]
	except:
		print("Error: Please enter a valid list of miRNAs.")
		exit()
              
	# take n as the first argument
	n = int(sys.argv[1])

	# read the second argument, that is a tsv file, as a list of tuples
	try:
		filter = [tuple(line.strip().split("\t")) for line in open(sys.argv[2])]
	except:
		print("Error: Please enter a valid list of miRNA pairs.")
		exit()

	# generate random pairs
	random_pairs = generate_random_pairs(miRNA_list, n, filter)

	# print the random pairs to standard output as tsv
	for pair in random_pairs:
		print("\t".join(pair))



	