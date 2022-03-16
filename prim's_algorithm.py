import timeit
from collections import defaultdict
from heapq import *
 
def prim(start_node, edges):
    mst = list() # create a list for mst
    adjacent_edges = defaultdict(list)

    for n1, n2, weight in edges:
        adjacent_edges[n1].append((n1, n2, weight)) # create an undirected graph
        adjacent_edges[n2].append((n2, n1, weight)) # create an undirected graph
 
    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)
    total_weight = 0 
    
    while candidate_edge_list:
        n1, n2, weight = heappop(candidate_edge_list) # pop an edge who has least weight
        if n2 not in connected_nodes: # if not visited
            connected_nodes.add(n2) # add the node to connected_nodes (visited == 1 now)
            mst.append((n1, n2, weight)) # append to mst
            total_weight += weight # update the total weight
            
            for edge in adjacent_edges[n2]: # search for next edge
                if edge[1] not in connected_nodes: # if not visited
                    heappush(candidate_edge_list, edge) # add edge to priority queue
 
    return mst, total_weight

# helper function to load data in from file
def get_data(filename):
    with open(filename, 'r') as rf:
        # transform file into string and split along new line
        lines = rf.read().split("\n") # read the text file line by line which is splited by a new line

        # separate each line along the space characters
        data = [line.split(" ") for line in lines]
    return data

# load data in from file
mygraph = get_data('C:/Users/Saeah Go/OneDrive/Desktop/Fa2021/CS350/HW8/city-pairs.txt')

'''
for i in mygraph:
    temp = i[2]
    i[2] = i[0]
    i[0] = temp
'''
for weight in mygraph:
    weight[2] = int(weight[2])

start = timeit.default_timer()	
mst, total_weight = prim('Albany', mygraph)
#mst, total_weight = prim('A', mygraph)
end = timeit.default_timer()

print("MST is: ", mst)
print("Weight is:" , total_weight)
print("Running time is: ", end - start)