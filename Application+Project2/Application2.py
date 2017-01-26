
from collections import deque

def bfs_visited(ugraph, start_node):
    ''' This node implements the BFS visited algorithm
    Input : Undirected graph ugraph, source node
    Output: Set of visited nodes starting from start_node
    ''' 
#     print "Here is the ugraph",ugraph
    d = deque([start_node]) #Original queue
    Visited = set([])
#     Visited.add(start_node)
    
    while d:
        j = d.popleft()
        Visited.add(j)
        neighbors = ugraph.get(j,None)
        for neighbor in neighbors:
            if neighbor not in Visited:
#                 Visited.add(neighbor)
                d.append(neighbor)
#         
        
    return Visited

def cc_visited(ugraph):
    '''This function will take as input an undirected graph G=(V,E)
    and return the list of all connected components'''
    remaining_nodes = ugraph.keys()
    connected_comp_list = []
    
    for node in remaining_nodes:
        working_set = bfs_visited(ugraph, node)
        if working_set not in connected_comp_list:
            connected_comp_list.append(working_set)
   
#     for node in connected_comp_list:
#         if len(node)==1:
#             connected_comp_list.remove(node)
            
    return connected_comp_list
           

def largest_cc_size(ugraph):
    '''This function will take the output of the cc_visited function and return 
    the length of the most connected component'''
    connected_component_list = cc_visited(ugraph)
    Max_connected_component = max([len(node) for node in connected_component_list])
    return Max_connected_component
#     print "Connected Component", connected_component_list,Max_connected_component

def compute_resilience(ugraph, attack_order):
    '''This function calculates the reslience of the current graph ugraph
    The motive is to simulate a network where #attack_order nodes mean the nodes which have 
    to be removed from the network. This would help in designing a real world automated threat protection 
    device which disconnects nodes when a virus hits depending on the size of their connected component
    The more a device is connected the more it is viable for disconnection'''
    connected_components_size = []
    original_largest_component_length = largest_cc_size(ugraph)
    connected_components_size.append(original_largest_component_length)
    
    for node_removed in attack_order:
        ugraph.pop(node_removed,None)
        for current_item in ugraph.keys():
            if node_removed in ugraph[current_item]:
                ugraph[current_item].remove(node_removed)

        large_component = largest_cc_size(ugraph)
#         print "Result of largest component", large_component  
        connected_components_size.append(large_component)
        
    return connected_components_size

# 
# EX_GRAPH0 = {0: set([1,2]),
#              1: set([]),
#              2: set([])}
# EX_GRAPH1 = {0: set([1,4,5]),
#              1: set([2,6]),
#              2: set([3]),
#              3: set([]),
#              4: set([1]),
#              5: set([2]),
#              6: set([])}
EX_GRAPH2 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3,7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1,2]),
             9: set([0,3,4,5,6,7])}
# 
# 
# # print bfs_visited(EX_GRAPH0, 0)
# # print cc_visited(EX_GRAPH2)
# 
# # print compute_resilience(EX_GRAPH2, [0,1])
print compute_resilience(EX_GRAPH2, [1, 3, 5, 7, 2, 4, 6, 8])
