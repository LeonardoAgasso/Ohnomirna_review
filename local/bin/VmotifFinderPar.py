#!/usr/bin/env python3

import sys
import networkx as nx
import numpy as np
from scipy.stats import norm
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
def count_singlepair(pair, G_i):
	if pair[0] not in G_i or pair[1] not in G_i:
		return 'not_in_G', 'not_in_G', 'not_in_G', 'not_in_G'
	tar_1 = set(G_i.successors(pair[0]))
	tar_2 = set(G_i.successors(pair[1]))

	common_tars = tar_1.intersection(tar_2)
	
	count = len(common_tars)

	return count, len(tar_1), len(tar_2), len(common_tars)


# given a pair, a homology network and a folder with random networks, this function returns the mean, the standard deviation and the number of times 
# the count of the motif on a random network returned a number of motif larger than (or equal to) the count of the motif on the real network
def nm_parameters_singlepair(pair, nm_folder_path, n_rand_nets, true_c):

	count_vec = []
	n_maj_true = 0

	for nm_file in glob.glob(nm_folder_path + '/*.edge'):
		if n_rand_nets == 0:
			break
		temp_G = nx.read_edgelist(nm_file, delimiter='\t', create_using=nx.DiGraph())
		cs = count_singlepair(pair, temp_G)[0]
		if type(cs)==int and cs>=true_c:
			n_maj_true += 1
		else:
			pass

		count_vec.append(cs)
		n_rand_nets -= 1
	mu = np.mean(count_vec)
	sigma = np.std(count_vec)

	return mu, sigma, n_maj_true


# Leverage the parallelization to process a given pairs and return all the useful information
def process_pair(pair, G_int, nm_folder, n_rand_nets):

	print("processing pair", pair[0], "-", pair[1], file=sys.stderr)

	true_c, len_tar_1, len_tar_2, len_com_tar  = count_singlepair(pair, G_int)

	if type(true_c)!=int:
		mu, sigma, n_maj, z_score, p_value = 'not_in_G', 'not_in_G', 'not_in_G', 'not_in_G', 'not_in_G'
	else:
		mu, sigma, n_maj = nm_parameters_singlepair(pair, nm_folder, n_rand_nets, true_c)
		if sigma==0 and true_c>=1:
			z_score = "sigma_err"
			p_value = "<1/"+str(n_rand_nets)
		elif sigma==0 and true_c==0:
			z_score = "sigma_err"
			p_value = 1.0
		else:
			z_score = (true_c-mu)/sigma
			p_value = 1 - norm.cdf(z_score)

	return (pair[0], pair[1], len_tar_1, len_tar_2, len_com_tar, mu, sigma, true_c, n_maj, z_score, p_value)


# main - takes the number of cores
def main(n_cores):

    nm_folder = sys.argv[3]
    n_rand_nets = int(sys.argv[4])

    G_int = nx.read_edgelist(sys.stdin, delimiter='\t', create_using=nx.DiGraph())
    G_homo_mirnas = nx.Graph()

    add_edges_nodes(sys.argv[2], G_homo_mirnas, G_int)

    # header
    print("miRNA_1\tmiRNA_2\tn_tar_1\tn_tar_2\tn_common_targets\tmu\tsigma\tn_vmotif\tn_maj_true\tZ-score\tpValue (nm size="+str(n_rand_nets)+")")

    pool = multiprocessing.Pool(processes=n_cores)

    results = pool.starmap(process_pair, [(pair, G_int, nm_folder, n_rand_nets) for pair in list(G_homo_mirnas.edges())])

    pool.close()
    pool.join()

    for result in results:
        print("\t".join(map(str, result)))


if __name__ == "__main__":
	n = sys.argv[1]
	main(int(n))
