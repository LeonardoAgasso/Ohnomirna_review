#!/usr/bin/env python3

import sys
import networkx as nx
import numpy as np
from scipy.stats import norm
import glob
import multiprocessing


# add edges and nodes to the  and interaction network
def add_edges_nodes(pairs, G_1):
	with open(pairs, 'r') as f:
		for line in f:
			el_1, el_2 = line.strip().split('\t')
			G_1.add_edge(el_1, el_2)


# given a pair, an interaction network and a homology network, this function returns the number of common targets,
# together with the number of targets of each miRNA
def count_singlepair(pair, G_i, G_hg):
	if pair[0] not in G_i or pair[1] not in G_i:
		return 'not_in_G', 'not_in_G', 'not_in_G', 'not_in_G'
	tar_1 = set(G_i.successors(pair[0]))
	tar_2 = set(G_i.successors(pair[1]))
	common_tars = tar_1.intersection(tar_2)
	count = 0
	G_hg = G_hg.subgraph(common_tars)
	count = G_hg.number_of_edges()

	return count, len(tar_1), len(tar_2), len(common_tars)


# main
def main():

	G_int = nx.read_edgelist(sys.stdin, delimiter='\t', create_using=nx.DiGraph())
	G_homo_mirnas, G_homo_genes = nx.Graph(), nx.Graph()

	add_edges_nodes(sys.argv[1], G_homo_mirnas)
	add_edges_nodes(sys.argv[2], G_homo_genes)

	# header
	print("miRNA_1\tmiRNA_2\tn_tar_1\tn_tar_2\tn_common_targets\tmotif_count")

	for pair in list(G_homo_mirnas.edges()):
		param_single_pair = count_singlepair(pair, G_int, G_homo_genes)
		print(str(pair[0]) + "\t" + str(pair[1]) + "\t" + str(param_single_pair[1]) + "\t" + str(param_single_pair[2]) + "\t" + str(param_single_pair[3]) + "\t" + str(param_single_pair[0]))



if __name__ == "__main__":
	main()
