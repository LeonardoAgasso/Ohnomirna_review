import numpy as np
import networkx as nx
from scipy import sparse

#############################
#       SIMILARITIES        #
#############################


#function that calculates the values of target similarity
def Target_Sim(G, cp_paral, jaccard=False, relative=False):

    regsim = {}

    for g1, g2 in cp_paral:

        if G.has_node(g1) and G.has_node(g2):

            reg1 = set(G.successors(g1))
            reg2 = set(G.successors(g2))

            coreg = set.intersection(reg1,reg2)

            if 0 != len(reg1) and 0 != len(reg2):

                if jaccard:

                    union = set.union(reg1,reg2)
                    if relative:
                        regsim[(g1,g2)] = (len(coreg)/len(union))/(min(len(reg1), len(reg2))/max(len(reg1), len(reg2)))
                    else:
                        regsim[(g1,g2)] = len(coreg)/len(union)

                else:
                    if relative:
                        regsim[(g1,g2)] = len(coreg)/min(len(reg1), len(reg2))
                    else:
                        regsim[(g1,g2)] = 2*len(coreg)/(len(reg1)+len(reg2))

    return regsim


#function that calculates the values of regulator similarity
def Regulator_Sim(G, cp_paral, jaccard=False, relative=False):

    regsim = {}

    for g1, g2 in cp_paral:

        if G.has_node(g1) and G.has_node(g2):

            reg1 = set(G.predecessors(g1))
            reg2 = set(G.predecessors(g2))

            coreg = set.intersection(reg1,reg2)

            if 0 != len(reg1) and 0 != len(reg2):

                if jaccard:

                    union = set.union(reg1,reg2)
                    if relative:
                        regsim[(g1,g2)] = (len(coreg)/len(union))/(min(len(reg1), len(reg2))/max(len(reg1), len(reg2)))
                    else:
                        regsim[(g1,g2)] = len(coreg)/len(union)

                else:
                    if relative:
                        regsim[(g1,g2)] = len(coreg)/min(len(reg1), len(reg2))
                    else:
                        regsim[(g1,g2)] = 2*len(coreg)/(len(reg1)+len(reg2))

    return regsim


#function that calculates the values of contact similarity
def Contact_Sim(G, cp_paral, jaccard=False, relative=False):

    regsim = {}

    for g1, g2 in cp_paral:

        if G.has_node(g1) and G.has_node(g2):

            reg1 = set(G.neighbors(g1))
            reg2 = set(G.neighbors(g2))

            coreg = set.intersection(reg1,reg2)

            if 0 != len(reg1) and 0 != len(reg2):

                if jaccard:

                    union = set.union(reg1,reg2)
                    if relative:
                        regsim[(g1,g2)] = (len(coreg)/len(union))/(min(len(reg1), len(reg2))/max(len(reg1), len(reg2)))
                    else:
                        regsim[(g1,g2)] = len(coreg)/len(union)

                else:
                    if relative:
                        regsim[(g1,g2)] = len(coreg)/min(len(reg1), len(reg2))
                    else:
                        regsim[(g1,g2)] = 2*len(coreg)/(len(reg1)+len(reg2))

    return regsim





#############################
#     FAST SIMILARITIES     #
#############################

def TargetSim_fast(G,G_ssd,G_wgd):

    A = nx.adjacency_matrix(G, nodelist=sorted(G))

    coreg = A.dot(A.T)

    out_degs = np.diag(coreg.todense())

    x,y,common = sparse.find(sparse.triu(coreg,1))

    sim = (2*common/(out_degs[x]+out_degs[y])).astype(np.float32)


    d = dict(zip(range(G.number_of_nodes()),sorted(G)))

    ssd_sim = []
    wgd_sim = []
    nodup_sim = []

    for g1,g2,s in zip(x,y,sim):
        g1 = d[g1]
        g2 = d[g2]
        if G_ssd.has_edge(g1,g2):
            ssd_sim.append(s)
        elif G_wgd.has_edge(g1,g2):
            wgd_sim.append(s)
        else:
            nodup_sim.append(s)

    return ssd_sim,wgd_sim,nodup_sim



def RegSim_fast(G,G_ssd,G_wgd):

    A = nx.adjacency_matrix(G, nodelist=sorted(G))

    coreg = A.T.dot(A)

    in_degs = np.diag(coreg.todense())

    x,y,common = sparse.find(sparse.triu(coreg,1))

    sim = (2*common/(in_degs[x]+in_degs[y])).astype(np.float32)


    d = dict(zip(range(G.number_of_nodes()),sorted(G)))

    ssd_sim = []
    wgd_sim = []
    nodup_sim = []

    for g1,g2,s in zip(x,y,sim):
        g1 = d[g1]
        g2 = d[g2]
        if G_ssd.has_edge(g1,g2):
            ssd_sim.append(s)
        elif G_wgd.has_edge(g1,g2):
            wgd_sim.append(s)
        else:
            nodup_sim.append(s)

    return ssd_sim,wgd_sim,nodup_sim



def ContactSim_fast(G,G_ssd,G_wgd):

    A = nx.adjacency_matrix(G, nodelist=sorted(G))

    coreg = A.dot(A.T)

    degs = np.diag(coreg.todense())

    x,y,common = sparse.find(sparse.triu(coreg,1))

    sim = (2*common/(degs[x]+degs[y])).astype(np.float32)


    d = dict(zip(range(G.number_of_nodes()),sorted(G)))

    ssd_sim = []
    wgd_sim = []
    nodup_sim = []

    for g1,g2,s in zip(x,y,sim):
        g1 = d[g1]
        g2 = d[g2]
        if G_ssd.has_edge(g1,g2):
            ssd_sim.append(s)
        elif G_wgd.has_edge(g1,g2):
            wgd_sim.append(s)
        else:
            nodup_sim.append(s)

    return ssd_sim,wgd_sim,nodup_sim




#############################
#       DELTA DEGREE        #
#############################


def Dk(G, cp_paral, deg_type=None):

    Dk = {}

    if None == deg_type:

        for g1, g2 in cp_paral:

            d1 = G.degree(g1)
            d2 = G.degree(g2)

            if 0 != d1 or 0 != d2:
                Dk[(g1,g2)] = abs(d1-d2)

    elif 'in' == deg_type:

        for g1, g2 in cp_paral:

            d1 = G.in_degree(g1)
            d2 = G.in_degree(g2)

            if 0 != d1 or 0 != d2:
                Dk[(g1,g2)] = abs(d1-d2)

    elif 'out' == deg_type:

        for g1, g2 in cp_paral:

            d1 = G.out_degree(g1)
            d2 = G.out_degree(g2)

            if 0 != d1 or 0 != d2:
                Dk[(g1,g2)] = abs(d1-d2)


    return Dk



#############################
#       PPI OVERLAP         #
#############################

def PPIOverlap(G, cp, relative=True):

    n_overlaps = np.sum([G.has_edge(g1,g2) for g1,g2 in cp])

    if relative:
        return n_overlaps/len(cp)
    else:
        return n_overlaps
