#!/usr/bin/env python3

import sys
import networkx as nx

def connected_components(adj_list, len_name, perc, n_edges):
	G = nx.Graph()

	lines = adj_list.splitlines()
	for line in lines:
		if line.strip():
			parts = line.split()
			if len(parts) >= 2:
				node1 = parts[0]
				node2 = parts[1]
				G.add_edge(node1, node2)

	components = list(nx.connected_components(G))

	result = []
	for component in components:
		component_list = list(component)
		if len(component_list) <= len_name:
			name = ';'.join(component_list)
		else:
			name = ';'.join(component_list[:len_name])
			name += ';...'
            
		result.append(f"{name}\t{len(component_list)}")

	#	
		if(perc=="-p"):
			# assign to p the number of edges in the component divided by the number of possible edges. Round to 2 decimal places
			n_nodes = len(G.subgraph(component_list).nodes())
			p = len(G.subgraph(component_list).edges())
			p = p/(n_nodes*(n_nodes-1)/2)
			p = round(p, 6)
			result[-1] += f"\t{p}"

		if(n_edges=="-n"):
			# assign to n the number of edges in the component
			n = len(G.subgraph(component_list).edges())
			result[-1] += f"\t{n}"
			
	return result

def writeheader(perc, n_edges):
	header = "#component\tsize"
	if(perc=="-p"):
		header += "\tfraction_of_all_possible_edges"
	if(n_edges=="-n"):
		header += "\tnumber_of_edges"
	return header

if __name__ == "__main__":

	adj_list_contents = sys.stdin.read()
	
	len_name = int(sys.argv[1])
	
	n_edges = False
	perc = False

	if len(sys.argv) > 2:
		if sys.argv[2] == "-p":
			perc = sys.argv[2]
		elif sys.argv[2] == "-n":
			n_edges = sys.argv[2]
		else:
			raise ValueError("Available options are -p and -n")

	if len(sys.argv) > 3:
		if sys.argv[2] == "-p" and sys.argv[3] == "-n":
			perc = sys.argv[2]
			n_edges = sys.argv[3]
		elif sys.argv[2] == "-n" and sys.argv[3] == "-p":
			perc = sys.argv[3]
			n_edges = sys.argv[2]
		else:
			raise ValueError("Available options are -p and -n")

	result = connected_components(adj_list_contents, len_name, perc, n_edges)

	result.sort(key=lambda x: int(x.split()[1]), reverse=True)

	header = writeheader(perc, n_edges)

	print(header)
	for line in result:
		print(line)

