#!/usr/bin/env python3

import sys
import networkx as nx

def add_edges_nodes(pairs, G_1):
    with open(pairs, 'r') as f:
        for line in f:
            el_1, el_2 = line.strip().split('\t')
            G_1.add_edge(el_1, el_2)
 
def main():
    if len(sys.argv) != 5:
        print("Usage: ListPPIBifan interaction_network miRNA_homologs gene_homologs PPI_network")
        sys.exit(1)

    G_int = nx.read_edgelist(sys.argv[1], delimiter='\t', create_using=nx.DiGraph())
    G_homo_mirnas, G_homo_genes, G_ppi = nx.Graph(), nx.Graph(), nx.Graph()

    add_edges_nodes(sys.argv[2], G_homo_mirnas)
    add_edges_nodes(sys.argv[3], G_homo_genes)
    add_edges_nodes(sys.argv[4], G_ppi)

    print("miRNA_1\tmiRNA_2\tPPI_bifan_target_1\tPPI_bifan_target_2")

    for pair in G_homo_mirnas.edges():
        if pair[0] not in G_int or pair[1] not in G_int:
            print(f"{pair[0]}\t{pair[1]}\tnot_in_G\tnot_in_G")
            continue

        targets_1 = set(G_int.successors(pair[0]))
        targets_2 = set(G_int.successors(pair[1]))
        common_targets = targets_1.intersection(targets_2)
        
        G_induced = G_homo_genes.subgraph(common_targets)

        for edge in G_induced.edges():
            if edge[0] in G_ppi and edge[1] in G_ppi[edge[0]]:
                print(f"{pair[0]}\t{pair[1]}\t{edge[0]}\t{edge[1]}")

if __name__ == "__main__":
    main()
