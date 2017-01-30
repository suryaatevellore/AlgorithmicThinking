"""
Provided code for Application portion of Module 2
"""

# general imports
import urllib2
import random
import time
import math
from matplotlib import pyplot as plt
# from DPAAlgorithm import new_node

# CodeSkulptor import
#import simpleplot
#import codeskulptor
#codeskulptor.set_timeout(60)

# Desktop imports
#import matplotlib.pyplot as plt


"""
Provided code for application portion of module 2

Helper class for implementing efficient version
of UPA algorithm
"""

import random

class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm
    
    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that each node number
        appears in correct ratio
        
        Returns:
        Set of nodes
        """
#         print " Inside run _trial number of nodes " , self._num_nodes
#         print "Inside run_trial intital _node_numbers", self._node_numbers
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
#         print "intial node neighbors", new_node_neighbors
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
#         print "addition of _num_nodes", self._node_numbers
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
#             print "addition from length of new_node_neighbors",self._node_numbers
        self._node_numbers.extend(list(new_node_neighbors))
        
#         print "_node_numbers after addition of neighbors", new_node_neighbors
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

############################################
# Provided code

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    It calculates the maximum degree node and stores the values in the variable max_degree_node
    It then pops that node out of the graph and removes the edges between the node and its neighbors
    Returns:
    A list of nodes,order which contains maximum defree nodes in descending order
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order
    


##########################################################
# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"

def fast_targeted_order(uoldgraph):
    '''Input = Graph g(V,E) with V= {0,1,......,n-1}
    returns a list of nodes in decreasing prder of their degrees'''
    #sets the initial value of all the degrees to an empty set
    
    #Create a new graph from an old graph
    ugraph = copy_graph(uoldgraph)
    
    
    DegreeSets = {}
    for node in range(len(ugraph)):
        DegreeSets[node]=set([])
    
    n = len(ugraph)
    DegreeSets = [set() for _ in xrange(n)]
    #calculates degree per node and appends to DegreeSets[degree]
    #So if a node 5 has degree 1,it's entry would be DegreeSets[1]=[5]
    for node in ugraph:
        degree_node = len(ugraph[node])
        DegreeSets[degree_node].add(node)
    
    order = []
    
    for degree in range(len(ugraph)-1,-1,-1):
        while len(DegreeSets[degree]) != 0:
            max_degree_node = DegreeSets[degree].pop()
#             print "max_degree_node", max_degree_node
            neighbors = ugraph[max_degree_node]
                
            for neighbor in neighbors:
#                 print "neighbor", neighbor
                degree_of_neighbor = len(ugraph[neighbor])
                DegreeSets[degree_of_neighbor].discard(neighbor)
                DegreeSets[degree_of_neighbor-1].add(neighbor)
                ugraph[neighbor].remove(max_degree_node)
                
            order.append(max_degree_node)
                
            ugraph.pop(max_degree_node,None)
    
    return order



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


    
def generate_random_graph(num_nodes,p):
    udigraph = {}
    nodes = xrange(num_nodes)
    for node in nodes:
        udigraph[node] = set([])
    for node in nodes:
        remaining_nodes = set(nodes) - set([node])
        for next_in_line in remaining_nodes:
            if random.random()<p:
                udigraph[node].add(next_in_line)
                udigraph[next_in_line].add(node)
            
    return udigraph

def make_complete_graph(num_nodes):
    '''This function is supposed to build to a completely connected directed graph.
    We are editing it to build a undirected graph'''
    complete_connected_graph = {}
    if num_nodes>0:
        nodes = xrange(0, num_nodes)
        for each_node in nodes:
            complete_connected_graph[each_node] = (set(nodes)-set([each_node]))            
        return complete_connected_graph
    else:
        return complete_connected_graph

'''
compute the set of connected components (CCs) of an undirected graph
as well as determine the size of its largest connected component
'''

# collections.deque module supports O(1) enqueue and dequeue operations
from collections import deque


def bfs_visited(ugraph, start_node):
    '''
    takes the undirected graph ugraph and the node start_node;
    returns the set consisting of all nodes that are
    visited by a breadth-first search that starts at start_node
    '''
    neighbors = deque([start_node])
    visited = set()

    while neighbors:
        node = neighbors.popleft()
        visited.add(node)
        for item in ugraph[node]:
            if item not in visited:
                neighbors.append(item)

    return visited


def cc_visited(ugraph):
    '''
    takes the undirected graph ugraph and returns a list of sets,
    where each set consists of all the nodes (and nothing else) in a connected component,
    and there is exactly one set in the list for each connected component in ugraph and nothing else
    '''
    nodes = set(ugraph.keys())
    connected_components = []
    
    while nodes:
        node = nodes.pop()
        visited = bfs_visited(ugraph, node)
        nodes -= visited
        connected_components.append(visited)

    return connected_components


def largest_cc_size(ugraph):
    '''
    takes the undirected graph ugraph and returns the size (an integer)
    of the largest connected component in ugraph
    '''
    connected_components = cc_visited(ugraph)
    if connected_components:
        return max(list(map(len, connected_components)))
    else:
        return 0


def compute_resilience(ugraph, attack_order):
    '''
    takes the undirected graph ugraph, a list of nodes attack_order and
    iterates through the nodes in attack_order
    '''
    resilience = [largest_cc_size(ugraph)]
    
    for node in attack_order:
        ugraph.pop(node, None)
        for edge in ugraph:
            if node in ugraph[edge]:
                ugraph[edge].remove(node)
        resilience.append(largest_cc_size(ugraph))

    return resilience

def random_order(udigraph):
    '''This function takes in an undirected graph and returns a shuffled list of nodes'''
    shuffled_nodes = udigraph.keys()
    random.shuffle(shuffled_nodes)
    return shuffled_nodes

def create_UPA_graph(n, m):
    '''m = number of nodes added per iteration
       n = total number of nodes'''
    
    udigraph = make_complete_graph(m)
    upa_helper = UPATrial(m)
    for node in range(m,n):
        adj_list = upa_helper.run_trial(m)
        udigraph[node] = set(adj_list)
        for neighbor in adj_list:
            udigraph[neighbor].add(node)
        
    return udigraph

def plot_graph(loaded_graph,upa_graph,random_graph):
    '''x axis : Number of nodes removed
        y axis : length of connected component '''
    x_axis = range(0,1240)
    y_axis_loaded = loaded_graph
    y_axis_upa = upa_graph
    y_axis_random = random_graph
    plt.plot(x_axis,y_axis_loaded,label="Computer Network")
    plt.plot(x_axis, y_axis_upa, label="UPA Graph,m="+str(M))
    plt.plot(x_axis, y_axis_random, label="ER Graph,p="+str(p))
    plt.ylabel('Maximum Connected component length')
    plt.xlabel('No of nodes removed')
    plt.grid(True)
    plt.title("Resilience of different types of graphs")
    plt.legend(loc='upper right')
    plt.show()
    
def first_among_equals(UPA_GRAPH,RANDOM_GRAPH,LOAD_GRAPH):
    '''This function seeks to determine which graph is most resilient. A graph is measured for 
    its resiliency by removing 20% of the nodes. If the length of the max connected component after removal 
    is >25% of the nodes , then graph is resilient'''
    nodes_to_remove = int(math.floor(0.2*len(UPA_GRAPH.keys())))
    print nodes_to_remove
    nodes_to_check_for = 0.25*len(UPA_GRAPH.keys())
    UPA_random = random_order(UPA_GRAPH)
    RANDOM_random = random_order(RANDOM_GRAPH)
    LOAD_random = random_order(LOAD_GRAPH)
    
    
    UPA_resilient_nodes = compute_resilience(UPA_GRAPH, UPA_random[:247])
    RANDOM_resilient_nodes = compute_resilience(RANDOM_GRAPH, RANDOM_random[:247])
    LOAD_resilient_nodes = compute_resilience(LOAD_GRAPH, LOAD_random[:247])
     
    max_connected_component = max(UPA_resilient_nodes[-1],RANDOM_resilient_nodes[-1],LOAD_resilient_nodes[-1])
    if max_connected_component == UPA_resilient_nodes[-1]:
        print "UPA graph is most resilient"
    elif max_connected_component == RANDOM_resilient_nodes[-1]:
        print "RANDOM graph is most resilient"
    else:
        print "LOADED graph is most resilient"

def plot_running_time(targeted_old, targeted_new):
    '''This function has been created specifically for calculating runningTime vs No. of Nodes graphs
    for targeted order and fast targeted order. We are unable to combine all plot related functions into one
    '''
    targeted_x_axis = xrange(10, 1000, 10)
    targeted_y_axis = targeted_old
    
    targeted_new_y_axis = targeted_new
    plt.plot(targeted_x_axis, targeted_y_axis, label = "targeted order")
    plt.plot(targeted_x_axis, targeted_new_y_axis, label = "fast targeted order")
    plt.xlabel("number of nodes")
    plt.ylabel("running times")
    plt.title("Running times of targeted order attacks implementations as on Desktop Python2.7")
    plt.legend(loc='upper right')
    plt.show()
    
def running_time_target():
    '''This function will calculate the running times for a number of iterations for UPA graphs for 
    targeted order and the newly implemented fast_targeted_order'''
    
    running_time_fast = []
    running_time = []
    m = 5
    for random_n in range(10, 1000, 10):
        ugraph = create_UPA_graph(random_n, 5)
        start_time = time.clock()
        targeted_order(ugraph)
        running_time.append(time.clock()-start_time)
        ######################################
        start_time= time.clock()
        fast_targeted_order(ugraph)
        running_time_fast.append(time.clock()-start_time)
        
    return running_time, running_time_fast




M = 3 #Number of nodes that must be added in each iteration
N = 1239 # Only for UPA graph and random graph generation 
p = 0.0040

UPA_GRAPH = create_UPA_graph(N, M)
RANDOM_GRAPH = generate_random_graph(N, p)
LOAD_GRAPH = load_graph(NETWORK_URL)

# print random_order(UPA_GRAPH)
# print UPA_GRAPH.keys()
# print UPA_GRAPH

# old, fast = running_time_target()
#  
# print old, fast
# plot_running_time(old, fast)

# print "################################################################################"
# print fast_targeted_order(UPA_GRAPH)
# 
# upa_graph_resilience = compute_resilience(UPA_GRAPH, random_order(UPA_GRAPH))
# random_graph_resilience = compute_resilience(RANDOM_GRAPH, random_order(RANDOM_GRAPH))
# load_graph_resilience = compute_resilience(LOAD_GRAPH, random_order(LOAD_GRAPH))
 
# upa_graph_resilience = compute_resilience(UPA_GRAPH, targeted_order(UPA_GRAPH))
# random_graph_resilience = compute_resilience(RANDOM_GRAPH, targeted_order(RANDOM_GRAPH))
# load_graph_resilience = compute_resilience(LOAD_GRAPH, targeted_order(LOAD_GRAPH))
# 
# 
# # print fast_targeted_order(UPA_GRAPH)
# plot_graph(load_graph_resilience, upa_graph_resilience, random_graph_resilience)

# print first_among_equals(UPA_GRAPH, RANDOM_GRAPH, LOAD_GRAPH)