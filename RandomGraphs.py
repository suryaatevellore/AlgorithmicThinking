

import random
from matplotlib import pyplot as plt



def generate_random_graph(nodes,p):
    digraph = {}
    for node in nodes:
        digraph[node]=set([])
        remaining_nodes = set(nodes) - set([node])
        for next_in_line in remaining_nodes:
            if random.random()<p:
                digraph[node].add(next_in_line)
            
    return digraph

def in_degree_distribution(digraph):
    '''This function calulates the indegree distribution for a graph 
        digraph and returns a dictionary. Keys are 
        the degree values and values for the number of nodes that have that degree'''
    in_degree_dist={}
    for node in digraph.keys():
        in_degree_dist.setdefault(node,0)
        for edge in digraph[node]:
            in_degree_dist[edge] = in_degree_dist.get(edge,0)+1
    
    count_edges ={}
    for degree in in_degree_dist.values():
        count_edges[degree] = in_degree_dist.values().count(degree)
    
    return count_edges

def plot_graph(digraph):
    '''This graph plots the degree distribution graph with x axis as the edges and y axis 
    as the corresponding nodes with those degrees'''
    plt.plot(digraph.keys(),digraph.values())
    plt.show()
    plt.xlabel('In Degrees')
    plt.ylabel('No of Nodes')
    
    
    
TRIALS = [ x for x in xrange(100)]

answer_graph = generate_random_graph(TRIALS, 0.5)
print answer_graph
Degree_dist =  in_degree_distribution(answer_graph)
print Degree_dist
plot_graph(Degree_dist)


