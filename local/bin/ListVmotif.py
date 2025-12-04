#!/usr/bin/env python3

import sys
import networkx as nx

# add edges and nodes to the and interaction network
def add_edges_nodes(pairs, G_1):
    with open(pairs, 'r') as f:
        for line in f:
            el_1, el_2 = line.strip().split('\t')
            G_1.add_edge(el_1, el_2)
 
def main():
    if len(sys.argv) != 3:
        print("Usage: ListVmotif interaction_network miRNA_homologs")
        sys.exit(1)

    G_int = nx.read_edgelist(sys.argv[1], delimiter='\t', create_using=nx.DiGraph())
    G_homo_mirnas = nx.Graph()

    add_edges_nodes(sys.argv[2], G_homo_mirnas)

    print("miRNA_1\tmiRNA_2\ttarget")

    for pair in G_homo_mirnas.edges():
        if pair[0] not in G_int or pair[1] not in G_int:
            print(f"{pair[0]}\t{pair[1]}\tnot_in_G")
            continue

        targets_1 = set(G_int.successors(pair[0]))
        targets_2 = set(G_int.successors(pair[1]))
        common_targets = targets_1.intersection(targets_2)

        for target in common_targets:
            print(f"{pair[0]}\t{pair[1]}\t{target}")

if __name__ == "__main__":
    main()
