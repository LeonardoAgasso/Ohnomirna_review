#!/usr/bin/env python3

import sys
import networkx as nx

# read the graph from the input
G = nx.read_adjlist(sys.argv[1], create_using=nx.Graph(), delimiter='\t')

# find the connected components
components = nx.connected_components(G)

# for each connected component
for component in components:
	# print all the possible pairs of nodes without repetitions of the same pair
	for node1 in component:
		for node2 in component:
			if node1 > node2:
				print(str(node1)+"\t"+str(node2))

	