
"""
Provided code for application portion of module 1

Helper class for implementing efficient version
of DPA algorithm
"""

# general imports
from __future__ import division
import random
from matplotlib import pyplot as plt

class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        #Just for trial. Guessing but need to know what exacty it does
        print "This is what the new nodes are intialised to ", new_node_neighbors
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors
    




def make_complete_graph(num_nodes):
    '''This function is supposed to build to a completely connected directed graph'''
    complete_connected_graph = {}
    if num_nodes>0:
        nodes = xrange(0, num_nodes)
        for each_node in nodes:
            complete_connected_graph[each_node] = (set(nodes)-set([each_node]))            
        return complete_connected_graph
    else:
        return complete_connected_graph

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

 
def create_dpa_algorithm(n,m):
    if not m<=n:
        print "The increase in nodes must be less than the final size of the graph\
        You see, we can add only so much water till the glass gets full."
        exit(-1)
    
    Connected_Graph = make_complete_graph(m)
#     print Connected_Graph
    dpa_helper = DPATrial(m)
    
    for node in range(m,n):
        adj_list = dpa_helper.run_trial(m)
        Connected_Graph[node] = set(adj_list)
    
    return Connected_Graph


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



dpa_graph = create_dpa_algorithm(27770, 12)
in_degree_dpa = in_degree_distribution(dpa_graph)
plot_graph(in_degree_dpa,'DPA in-degree log/log distribution')

    
    
        
    