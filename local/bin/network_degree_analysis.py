#!/usr/bin/python3

import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import sys
from collections import Counter 


def max_degree(G):
    #initialize the lists
    degree_list1 = []
    degree_list2 = []
    #for each node in the graph
    for node in G.nodes():
        #if the node is in the first set
        if G.nodes[node]['bipartite'] == 0:
            #add the degree of the node to the first list
            degree_list1.append(G.degree(node))
        #if the node is in the second set
        elif G.nodes[node]['bipartite'] == 1:
            #add the degree of the node to the second list
            degree_list2.append(G.degree(node))
    #return the maximum of the two lists
    return max(degree_list1), max(degree_list2)

def average_degree(G):
    #initialize the lists
    degree_list1 = []
    degree_list2 = []
    #for each node in the graph
    for node in G.nodes():
        #if the node is in the first set
        if G.nodes[node]['bipartite'] == 0:
            #add the degree of the node to the first list
            degree_list1.append(G.degree(node))
        #if the node is in the second set
        elif G.nodes[node]['bipartite'] == 1:
            #add the degree of the node to the second list
            degree_list2.append(G.degree(node))
    #return the average of the two lists
    return sum(degree_list1)/len(degree_list1), sum(degree_list2)/len(degree_list2)


def plot_pk(G):
    #initialize the lists
    degree_list1 = []
    degree_list2 = []
    #for each node in the graph
    for node in G.nodes():
        #if the node is in the first set
        if G.nodes[node]['bipartite'] == 0:
            #add the degree of the node to the first list
            degree_list1.append(G.degree(node))
        #if the node is in the second set
        elif G.nodes[node]['bipartite'] == 1:
            #add the degree of the node to the second list
            degree_list2.append(G.degree(node))
    #count the number of nodes with each degree
    degree_count1 = Counter(degree_list1)
    degree_count2 = Counter(degree_list2)
    #initialize the lists
    degree1 = []
    degree2 = []
    #for each degree in the first set
    for degree in degree_count1:
        #add the degree to the list
        degree1.append(degree)
    #for each degree in the second set
    for degree in degree_count2:
        #add the degree to the list
        degree2.append(degree)
    #sort the lists
    degree1.sort()
    degree2.sort()
    #initialize the lists
    pk1 = []
    pk2 = []
    #for each degree in the first set
    for degree in degree1:
        #add the probability to the list
        pk1.append(degree_count1[degree]/len(degree_list1))
    #for each degree in the second set
    for degree in degree2:
        #add the probability to the list
        pk2.append(degree_count2[degree]/len(degree_list2))
    
    #plot the degree distribution of the first set
    plt.plot(degree1, pk1, color = 'blue', alpha = 0.5)
    plt.title("Degree distribution of the first set of nodes")
    plt.xlabel("Degree")
    plt.ylabel("Probability")
    plt.xscale('linear')
    plt.yscale('linear')
    plt.show()
    
    #plot the degree distribution of the second set
    plt.plot(degree2, pk2, color = 'red', alpha = 0.5)
    plt.title("Degree distribution of the second set of nodes")
    plt.xlabel("Degree")
    plt.ylabel("Probability")
    plt.xscale('linear')
    plt.yscale('linear')
    plt.show()

def plot_hist_degree_distribution_loglog(G):
    #initialize the lists
    degree_list1 = []
    degree_list2 = []
    #for each node in the graph
    for node in G.nodes():
        #if the node is in the first set
        if G.nodes[node]['bipartite'] == 0:
            #add the degree of the node to the first list
            degree_list1.append(G.degree(node))
        #if the node is in the second set
        elif G.nodes[node]['bipartite'] == 1:
            #add the degree of the node to the second list
            degree_list2.append(G.degree(node))
    
    #dplot the degree distribution of the first set
    plt.hist(degree_list1, bins = 100, color = 'blue', alpha = 0.5)
    plt.title("Degree distribution of the first set of nodes")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    
    #degree distribution of the second set
    plt.hist(degree_list2, bins = 100, color = 'red', alpha = 0.5)
    plt.title("Degree distribution of the second set of nodes")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

def plot_hist_degree_distribution(G):
    #initialize the lists
    degree_list1 = []
    degree_list2 = []
    #for each node in the graph
    for node in G.nodes():
        #if the node is in the first set
        if G.nodes[node]['bipartite'] == 0:
            #add the degree of the node to the first list
            degree_list1.append(G.degree(node))
        #if the node is in the second set
        elif G.nodes[node]['bipartite'] == 1:
            #add the degree of the node to the second list
            degree_list2.append(G.degree(node))
    
    #degree distribution of the first set
    plt.hist(degree_list1, bins = 100, color = 'blue', alpha = 0.5)
    plt.title("Degree distribution of the first set of nodes (genes)")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    plt.show()

    #degree distribution of the second set
    plt.hist(degree_list2, bins = 100, color = 'red', alpha = 0.5)
    plt.title("Degree distribution of the second set of nodes (miRNAs)")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    plt.show()

#def degree_list(G, set):
    #initialize the list
    degree_list = []
    #for each node in the graph
    for node in G.nodes():
        #if the node is in the set
        if G.nodes[node]['bipartite'] == set:
            #add the node and its degree to the list
            degree_list.append((node, G.degree(node)))
    #sort the list according to the degree
    degree_list.sort(key = lambda x: x[1], reverse = True)
    #return the list
    return degree_list

def number_of_nodes(G):
    #initialize the lists
    nodes1 = []
    nodes2 = []
    #for each node in the graph
    for node in G.nodes():
        #if the node is in the first set
        if G.nodes[node]['bipartite'] == 0:
            #add the node to the first list
            nodes1.append(node)
        #if the node is in the second set
        elif G.nodes[node]['bipartite'] == 1:
            #add the node to the second list
            nodes2.append(node)
    #return the number of nodes in each set
    return len(nodes1), len(nodes2)

def number_of_edges(G):
    #initialize the list
    edges = []
    #for each edge in the graph
    for edge in G.edges():
        #add the edge to the list
        edges.append(edge)
    #return the number of edges
    return len(edges)

def project_onto_first_set(G):
    #project the graph onto the first set of nodes
    G1 = bipartite.projected_graph(G, [node for node in G.nodes() if G.nodes[node]['bipartite'] == 0])
    #return the projected graph
    return G1

def project_onto_second_set(G):
    #project the graph onto the second set of nodes
    G2 = bipartite.projected_graph(G, [node for node in G.nodes() if G.nodes[node]['bipartite'] == 1])
    #return the projected graph
    return G2

def plot_hist_degree_distribution_unipartite(G):
    #initialize the list
    degree_list = []
    #for each node in the graph
    for node in G.nodes():
        #add the degree of the node to the list
        degree_list.append(G.degree(node))
    
    #degree distribution
    plt.scatter(degree_list, bins = 100, color = 'blue', alpha = 0.5)
    plt.title("Degree distribution of the nodes of the unipartite graph")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    plt.xscale('linear')
    plt.yscale('linear')
    plt.show()

#function that shows the unipartite graph with the circular layout
def show_unipartite_graph(G):
    #draw the graph
    nx.draw_circular(G, with_labels = True)
    #show the graph
    plt.show()





def main():

    #read in the file
    file = sys.argv[1]
    f = open(file, 'r')
    lines = f.readlines()

    #initialize the graph
    G = nx.Graph()

    #add the nodes
    for line in lines:
        line = line.strip()
        nodes = line.split()
        G.add_node(nodes[0], bipartite = 0)
        G.add_node(nodes[1], bipartite = 1)

    #add the edges
    for line in lines:
        line = line.strip()
        nodes = line.split()
        G.add_edge(nodes[0], nodes[1])
    
    print("Number of nodes in the first set of nodes (genes): ", number_of_nodes(G)[0])
    print("Number of nodes in the second set of nodes (miRNAs): ", number_of_nodes(G)[1])

    print("Number of edges in the graph: ", number_of_edges(G))

    print("Average degree of the first set of nodes (genes): ", round(average_degree(G)[0],3))
    print("Average degree of the second set of nodes (miRNAs): ", round(average_degree(G)[1],3))

    print("Maximum degree of the first set of nodes (genes): ", max_degree(G)[0])
    print("Maximum degree of the second set of nodes (miRNAs): ", max_degree(G)[1])

    #print("The ten nodes with the highest degree in the first set of nodes (genes) are: ", degree_list(G, 0)[:10])
    #print("The ten nodes with the highest degree in the second set of nodes (miRNAs) are: ", degree_list(G, 1)[:10])

    plot_hist_degree_distribution(G)
    plot_hist_degree_distribution_loglog(G)

    plot_pk(G)

    #project the graph onto the second set of nodes (miRNAs)
    #G2 = project_onto_second_set(G)

    #plot_degree_distribution_unipartite(G2)

    #show_unipartite_graph(G2)

if __name__=='__main__':
    main()
