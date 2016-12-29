
"""
Provided code for application portion of module 1

Helper class for implementing efficient version
of DPA algorithm
"""

# general imports
import random


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
    
def create_dpa_algorithm(n,m):
    if not m<=n:
        print "The increase in nodes must be less than the final size of the graph\
        You see, we can add only so much water till the glass gets full."
        exit(-1)
    
    Connected_Graph = make_complete_graph(m)
    dpa_helper = DPATrial(m)
    
    for node in range(m,n):
        adj_list = dpa_helper.run_trial(m)
        Connected_Graph[node] = set(adj_list)
    
    return Connected_Graph

print create_dpa_algorithm(3,2)
    
    
        
    
# print make_complete_graph(10)