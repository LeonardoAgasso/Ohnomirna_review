#!/usr/bin/env python3

import sys

def read_adjacency_list(filename):
	# nodes are strings, each line has two strings tab-separated, network is undirected
	adjacency_list = {}
	with open(filename) as f:
		for line in f:
			node1, node2 = line.strip().split("\t")
			if node1 not in adjacency_list:
				adjacency_list[node1] = set()
			if node2 not in adjacency_list:
				adjacency_list[node2] = set()
			adjacency_list[node1].add(node2)
			adjacency_list[node2].add(node1)

	return adjacency_list

def intersection(adjacency_list1, adjacency_list2):
	nodes = set(adjacency_list1.keys()) & set(adjacency_list2.keys())
	edges = set()
	for node in nodes:
		edges |= adjacency_list1[node] & adjacency_list2[node]
	return nodes, edges

def main():
	if len(sys.argv) != 3:
		print("Usage: {} <adjacency_list1> <adjacency_list2>".format(sys.argv[0]))
		sys.exit(1)

	adjacency_list1 = read_adjacency_list(sys.argv[1])
	adjacency_list2 = read_adjacency_list(sys.argv[2])

	nodes, edges = intersection(adjacency_list1, adjacency_list2)
	for node in nodes:
		print(node)
	for edge in edges:
		print(edge)

if __name__ == "__main__":
	main()

