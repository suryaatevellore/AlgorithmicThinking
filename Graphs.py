#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Graphs -- 
It defines methods to create directed graphs and find in degree distributions

@author:     surahuja

@copyright:  CISCO. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''


from collections import defaultdict

EX_GRAPH0 = {0:set([1,2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]), 4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), 8:set([1,2]), 9:set([0,3,4,5,6,7])}


def make_complete_graph(num_nodes):
    '''This function is supposed to build to a completely connected directed graph'''
    complete_connected_graph = {}
    if num_nodes>0:
        nodes = xrange(0, num_nodes)
        for each_node in xrange(len(nodes)):
            complete_connected_graph[each_node] = (set(nodes)-set([each_node]))            
        return complete_connected_graph
    else:
        return complete_connected_graph
    

def compute_in_degrees(digraph):
    '''This function calculates the indegree for variable digraph and returns a dictionary. Keys would be \
    the name of the node and values is the indgree of that node'''
    degree_dist={}
    for node in digraph.keys():
        degree_dist.setdefault(node,0)
        for edge in digraph[node]:
            degree_dist[edge] = degree_dist.get(edge,0)+1
    
    return degree_dist 
        

def in_degree_distribution(digraph):
    '''This function calulates the indegree distribution for a graph digraph and returns a dictionary. Keys are \
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
