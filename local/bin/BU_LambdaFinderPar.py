#!/usr/bin/env python3

import sys
import networkx as nx
import numpy as np
from scipy.stats import norm
import glob
import multiprocessing


# add edges and nodes to the interaction network
def add_edges_nodes(pairs, G_1, G_2):
	with open(pairs, 'r') as f:
		for line in f:
			el_1, el_2 = line.strip().split('\t')
			if el_1 in G_2:
				if el_2 in G_2:
					# add the edge to G_1
					G_1.add_edge(el_1, el_2)


def count_singlepair(mirna, G_i, G_hg):
	
	# common targets
	if mirna not in G_i:
		return "not_in_G", "not_in_G"
	
	targets = set(G_i.successors(mirna))
	# count if among the common targets there are pairs of genes that are connected in G_hg by a simple edge
	count = 0
	# Remove from G_hg the nodes that are not in the common targets
	G_hg = G_hg.subgraph(targets)
	# return the number of edges in the subgraph
	count = G_hg.number_of_edges()

	return count, len(targets)


def nm_params_singlepair(pair, G_hg, nm_folder_path, n_rand_nets, true_c):

	count_vec = []
	n_maj_true = 0
	
	# iterate over every file in nm_folder_path
	for nm_file in glob.glob(nm_folder_path + '/*.edge'):
		print(nm_file)
		if n_rand_nets == 0:
			break
		# define a temp_G to store the network
		temp_G = nx.read_edgelist(nm_file, delimiter='\t', create_using=nx.DiGraph())
		cs = count_singlepair(pair, temp_G, G_hg)
		if cs[0] >= true_c:
			n_maj_true += 1
		count_vec.append(cs[0])
		n_rand_nets -= 1


	mu = np.mean(count_vec)
	sigma = np.std(count_vec)

	return mu, sigma, n_maj_true


def process_single(mirna, G_int, G_homo_genes, nm_folder, n_rand_nets):
	
	true_c, len_tar  = count_singlepair(mirna, G_int, G_homo_genes)
    
	if true_c == 'not_in_G':
		mu, sigma, n_maj, z_score, p_value = 'not_in_G', 'not_in_G', 'not_in_G', 'not_in_G', 'not_in_G'
	
	else:
		mu, sigma, n_maj = nm_params_singlepair(mirna, G_homo_genes, nm_folder, n_rand_nets, true_c)
    
		if sigma==0 and true_c>=1:
			z_score = "sigma_err"
			p_value = "<1/"+str(n_rand_nets)
		elif sigma==0 and true_c==0:
			z_score = "sigma_err"
			p_value = 1.0
		else:
			z_score = (true_c-mu)/sigma
			p_value = 1 - norm.cdf(z_score)

	return (mirna, len_tar, mu, sigma, true_c, n_maj, z_score, p_value)


def main(n_proc):
	nm_folder = sys.argv[4]
	n_rand_nets = int(sys.argv[5])
	single_mirnas = sys.argv[2]

	G_int = nx.read_edgelist(sys.stdin, delimiter='\t', create_using=nx.DiGraph())
	G_homo_genes = nx.Graph()
	mirna_list = []

	with open(single_mirnas, 'r') as mirna_file:
	# Read lines from the file and append them to mirna_list
		mirna_list = [line.strip() for line in mirna_file]

	add_edges_nodes(sys.argv[3], G_homo_genes, G_int)
	

	print("miRNA\tn_targets\tmu\tsigma\tn_relevant_lambda\tn_maj_true\tZ-score\tpValue (nm size="+str(n_rand_nets)+")")

    # Create a pool of workers
	pool = multiprocessing.Pool(processes=n_proc)

    # Use the pool to parallelize the processing of pairs
	results = pool.starmap(process_single, [(mirna, G_int, G_homo_genes, nm_folder, n_rand_nets) for mirna in mirna_list])

    # Close the pool to free resources
	pool.close()
	pool.join()

    # Print results
	for result in results:
		print("\t".join(map(str, result)))


if __name__ == "__main__":
	n = sys.argv[1]
	main(int(n))
