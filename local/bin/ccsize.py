#!/usr/bin/env python3

import sys
import networkx as nx

def new_adj_list(adj_list, a, b):
	
	G = nx.Graph()

	lines = adj_list.splitlines()

	for line in lines:
		if line.strip():
			parts = line.split()
			if len(parts) >= 2:
				node1 = parts[a-1]
				node2 = parts[b-1]
				G.add_edge(node1, node2)

	components = list(nx.connected_components(G))

	result = []

	for line in lines:
		if line.strip():
			parts = line.split()
			if len(parts) >= 2:
				node1 = parts[a-1]
				node2 = parts[b-1]
				for component in components:
					if node1 in component and node2 in component:
						result.append(line + "\t" + str(len(component)))

	return result


if __name__ == "__main__":

	adj_list_contents = sys.stdin.read()
	
	a = int(sys.argv[1])
	b = int(sys.argv[2])

	result = new_adj_list(adj_list_contents, a, b)

	for line in result:
		print(line)