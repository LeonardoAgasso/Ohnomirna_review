#!/usr/bin/env python3

import sys
import networkx as nx

# add edges and nodes to the homology or interaction network
def add_edges_nodes(pairs, G):
	with open(pairs, 'r') as f:
		for line in f:
			n1, n2 = line.strip().split('\t')
			G.add_edge(n1, n2)

# given a miRNA pair, find motifs and return them explicitly
def find_motifs(pair, G_i, G_hg):
	mirna1, mirna2 = pair
	if mirna1 not in G_i or mirna2 not in G_i:
		return []

	targets_1 = set(G_i.successors(mirna1))
	targets_2 = set(G_i.successors(mirna2))
	common_targets = targets_1.intersection(targets_2)

	motifs = []
	# find pairs of homologous common targets explicitly
	for tgt1 in common_targets:
		for tgt2 in common_targets:
			if tgt1 < tgt2 and G_hg.has_edge(tgt1, tgt2):
				motifs.append((mirna1, mirna2, tgt1, tgt2))
	return motifs


def main():
	G_int = nx.read_edgelist(sys.stdin, delimiter='\t', create_using=nx.DiGraph())
	G_homo_mirnas, G_homo_genes = nx.Graph(), nx.Graph()

	add_edges_nodes(sys.argv[1], G_homo_mirnas)
	add_edges_nodes(sys.argv[2], G_homo_genes)

	# header
	print("miRNA_1\tmiRNA_2\ttarget_1\ttarget_2")

	for mirna_pair in G_homo_mirnas.edges():
		motifs = find_motifs(mirna_pair, G_int, G_homo_genes)
		for motif in motifs:
			print("\t".join(motif))


if __name__ == "__main__":
	main()
