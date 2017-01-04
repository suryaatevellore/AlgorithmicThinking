"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
from __future__ import division
import urllib2
import matplotlib.pyplot as plt

# Set timeout for CodeSkulptor if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

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
    
    '''This loop will normalise the degree distribution by doing number_of_nodes_per_degree/total_nodes'''    
    for degree in count_edges.keys():
        count_edges[degree] = count_edges[degree]/27770
        
    return count_edges

def plot_graph(distribution_dict, title=''):
    '''This graph plots the degree distribution graph with x axis as the edges and y axis 
    as the corresponding nodes with those degrees'''
    coords = dict_to_lists(distribution_dict)
    plt.loglog(coords[0], coords[1], 'ro')
    plt.ylabel('Frequency')
    plt.xlabel('In-degree')
    plt.grid(True)
    plt.title(title)
    plt.show()
    
    
def dict_to_lists(input_dict):
    '''
    Input is a dictionary whose keys are comparable.
    The function returns a list with two elements.
    The first element is the keys of the dictionary, sorted
    in ascending order. The second element are the the corresponding
    values. The values are normalized such that sum of all values equals 1.
    '''
    keys = sorted(input_dict.keys())
    values = [input_dict[key] for key in keys]
    return [normalize(keys), normalize(values)]   



def normalize(in_list):
    '''
    Given a list of numbers, normalize the values in the list so 
    values in the list sum to 1. 
`    '''
    if len(in_list) < 1:
        return float('nan')
    divisor = float(sum(in_list))
    return [element / divisor for element in in_list] 




def find_out_degree(digraph):
    out_degree_sum = 0                                                                                        
    for edge in digraph.values():
        out_degree_sum+=len(edge)
    
    return out_degree_sum/len(digraph.keys())

citation_graph =  load_graph(CITATION_URL)
# print find_out_degree(citation_graph)
Degree_Distribution = in_degree_distribution(citation_graph)

plot_graph(Degree_Distribution,'Citation Graph in-degree log/log distribution')

# 


