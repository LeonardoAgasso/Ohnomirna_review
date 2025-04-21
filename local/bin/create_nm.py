#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../bin')

import numpy as np
import networkx as nx
from multiprocessing import Pool
from tqdm import tqdm
import os


def double_edge_swap_directed(G, nswap=1, inplace=True):
    """
    
    METHOD INHERITED FROM: 
    Mottes, F., et al. (2021), The impact of whole genome duplications on the human gene regulatory networks
    https://pubmed.ncbi.nlm.nih.gov/34871317/
    
    
    Swap two edges in the graph while keeping the node degrees fixed.

    A double-edge swap removes two randomly chosen edges u-v and x-y
    and creates the new edges u-x and v-y::

     u->v            u->y
            becomes  
     x->y            x->v

    For a valid edge swap all nodes must be different and edges u->y and x->v 
    must not aready exist. The graph G is modified in place by default.

    Parameters
    ----------
    G : graph
       An undirected graph

    nswap : integer (optional, default=1)
       Number of double-edge swaps to perform

    inplace : bool (default=True)
       Whether to modify G in place or to return a shuffled copy.

    Returns
    -------
    G_null : graph
       The graph after double edge swaps.

    Notes
    -----
    Does not enforce any connectivity constraints.

    The graph G is modified in place.
    """
    if not G.is_directed():
        raise nx.NetworkXError(\
            "double_edge_swap_directed() not defined for undirected graphs. Use double_edge_swap_undiected() instead.")

    if len(G) < 4:
        raise nx.NetworkXError("Graph has less than four nodes.")
        
        
    np.random.seed() #set random seed

        
    if inplace:
        G_null = G
    else:
        G_null = G.copy()
    
    
    edgelist = dict(zip(range(G_null.number_of_edges()), G_null.edges()))

    
    swapcount=0
    while swapcount < nswap:
        
        #choose two random indices for edges
        valid_edges = False
        while not valid_edges:
            
            e1, e2 = np.random.randint(0, len(edgelist), 2)
        
            if e1 != e2:
                
                u,v = edgelist[e1]
                x,y = edgelist[e2]
                
                if u != x  and u != y and v != x and v != y:
                    if not G_null.has_edge(y,u) and not G_null.has_edge(v,x):
                        if not G_null.has_edge(u,y) and not G_null.has_edge(x,v):
                            valid_edges = True
                    
        #perform actual swap
        G_null.remove_edges_from([(u,v),(x,y)])
        G_null.add_edges_from([(u,y),(x,v)])
                    
        edgelist[e1] = (u,y)
        edgelist[e2] = (x,v)
        
        swapcount += 1
    
    
    return G_null



def main():
     
	network_file = sys.argv[1]
	n_nm = int(sys.argv[2])

	with open(network_file, 'r') as fh:
		edgelist_G = np.loadtxt(fh, delimiter='\t', dtype=str)


	G = nx.DiGraph()
	G.add_edges_from(edgelist_G)
	G.remove_edges_from(nx.selfloop_edges(G))

	for i in tqdm(np.arange(n_nm)):

		if os.path.exists('./nm_' + str(i) + '.edge'):
			continue
			
		#create null model
		G_null = double_edge_swap_directed(G, nswap=3*G.number_of_edges(), inplace=False)

		#save null model - this procedure will overwrite files with existing name if existent!
		with open( './nm_' + str(i) + '.edge', 'wb') as fh:
			nx.write_edgelist(G_null, fh, delimiter='\t', data=False)
 



if __name__ == "__main__":
    main()
