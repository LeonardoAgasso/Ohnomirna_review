#!/usr/bin/env python3

import sys
import networkx as nx
import numpy as np
import glob
import multiprocessing


# add edges and nodes to the  and interaction network
def add_edges_nodes(pairs, G_1, G_int):
	with open(pairs, 'r') as f:
		for line in f:
			el_1, el_2 = line.strip().split('\t')
			if el_1 not in G_int.nodes() or el_2 not in G_int.nodes():
				continue
			G_1.add_edge(el_1, el_2)


# given a pair, an interaction network and a homology network, this function returns the number of common targets,
# together with the number of targets of each miRNA
def count_singlemirna(mirna, G_i, G_hg):
	if mirna not in G_i:
		return 'not_in_G', 'not_in_G'
	targets = set(G_i.successors(mirna))
	count = 0
	G_hg = G_hg.subgraph(targets)
	count = G_hg.number_of_edges()

	return count, len(targets)


# given a pair, a homology network and a folder with random networks, this function returns the mean, the standard deviation and the number of times 
# the count of the motif on a random network returned a number of motif larger than (or equal to) the count of the motif on the real network
def nm_parameters_singlepair(mirna, G_hg, nm_folder_path, n_rand_nets, true_c):

	count_vec = []
	n_maj_true = 0

	for nm_file in glob.glob(nm_folder_path + '/*.edge'):
		if n_rand_nets == 0:
			break
		temp_G = nx.read_edgelist(nm_file, delimiter='\t', create_using=nx.DiGraph())
		cs = count_singlemirna(mirna, temp_G, G_hg)[0]
		if type(cs)==int:
			if cs>=true_c:
				n_maj_true += 1
		else:
			pass

		count_vec.append(cs)
		n_rand_nets -= 1

	# if count_vec is empty, return 'not_in_G' for mu and sigma
	if len(count_vec)==0:
		mu = 'not_in_G'
		sigma = 'not_in_G'
	else:
		mu = np.mean(count_vec)
		sigma = np.std(count_vec)

	return mu, sigma, n_maj_true


# Leverage the parallelization to process a given pairs and return all the useful information
def process_mirna(mirna, G_int, G_homo_genes, nm_folder, n_rand_nets):

	true_c, len_tar = count_singlemirna(mirna, G_int, G_homo_genes)

	if type(true_c)!=int:
		mu, sigma, n_maj, z_score = 'not_in_G', 'not_in_G', 'not_in_G', 'not_in_G'
	else:
		mu, sigma, n_maj = nm_parameters_singlepair(mirna, G_homo_genes, nm_folder, n_rand_nets, true_c)
		if sigma==0 and true_c>=1:
			z_score = "sigma_err"
		elif sigma==0 and true_c==0:
			z_score = "sigma_err"
		else:
			z_score = (true_c-mu)/sigma

	return (mirna, len_tar, mu, sigma, true_c, n_maj, z_score)


# main - takes the number of cores
def main(n_cores):
	nm_folder = sys.argv[4]
	n_rand_nets = int(sys.argv[5])
	mirna_list = []

	with open(sys.argv[2], 'r') as f:
		for line in f:
			mirna_list.append(line.strip())


	G_int = nx.read_edgelist(sys.stdin, delimiter='\t', create_using=nx.DiGraph())
	G_homo_genes = nx.Graph()

	add_edges_nodes(sys.argv[3], G_homo_genes, G_int)

	# header
	print("miRNA\tn_targets\tmu\tsigma\tn_relevant_delta\tn_maj_true\tZ-score\tpValue (nm size="+str(n_rand_nets)+")")

	pool = multiprocessing.Pool(processes=n_cores)

	results = pool.starmap(process_mirna, [(mirna, G_int, G_homo_genes, nm_folder, n_rand_nets) for mirna in mirna_list])

	pool.close()
	pool.join()

	for result in results:
		print("\t".join(map(str, result)))


if __name__ == "__main__":
	n = sys.argv[1]
	main(int(n))
