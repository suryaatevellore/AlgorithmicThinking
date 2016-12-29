

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
    
#///////