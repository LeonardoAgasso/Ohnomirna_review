#!/usr/bin/env python3

#script that takes a list of miRNA gene pairs as standard input and the adjacency list of a network as an argument and returns the miRNA pair list with the sorensen dice coefficient for each pair, as the stqndard output

import sys
import networkx as nx

#read the adjacency list of the network
G=nx.read_adjlist(sys.argv[1])

def sorensen_dice_coefficient(G, u, v):
	"""
	Compute the sorensen dice coefficient for two nodes u and v in the graph G
	"""
	#compute the intersection of the neighbors of u and v
	intersection=set(G.neighbors(u)) & set(G.neighbors(v))
	#compute the sorensen dice coefficient
	sorensen=[(u,v,2*len(intersection)/(len(set(G.neighbors(u)))+len(set(G.neighbors(v)))))]

	return sorensen

#read the miRNA gene pairs (the list is tab separated)
for line in sys.stdin:
	line = line.rstrip()
	fields = line.split("\t")

	if len(fields) != 2:
		print("Line \"{lsine}\" does not contain exactly two fields")
		continue
	
	if fields[0] not in G.nodes() and fields[1] in G.nodes():
		print(fields[0] + "\t" + fields[1] + "\tNA\terr_1")
		continue
	elif fields[0] in G.nodes() and fields[1] not in G.nodes():
		print(fields[0] + "\t" + fields[1] + "\tNA\terr_2")
		continue
	elif fields[0] not in G.nodes() and fields[1] not in G.nodes():
		print(fields[0] + "\t" + fields[1] + "\tNA\terr_3")
		continue
	elif fields[0] in G.nodes() and fields[1] in G.nodes():
		# Compute the Sørensen-Dice coefficient for each pair
		try:
			sorensen = sorensen_dice_coefficient(G, fields[0], fields[1])
			for u, v, p in sorensen:
				print(fields[0] + "\t" + fields[1] + "\t" + str(p) + "\t" + ".")
		except Exception as e:
			print("An error occurred:", str(e))
			continue