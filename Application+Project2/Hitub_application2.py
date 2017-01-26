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

print compute_resilience(EX_GRAPH2, [1, 3, 5, 7, 2, 4, 6, 8])