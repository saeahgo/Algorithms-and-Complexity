import timeit # to measure the execution time

parent = {}
rank = {}

# make each vertice as an independent set
def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

# connect two vertices
def union(v, u):
    root1 = find(v)
    root2 = find(u)
    
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(graph):    
    for v in graph['vertices']:
        make_set(v)
    
    mst = []
    total_weight = 0
    
    edges = graph['edges']
    edges.sort()
    
    for edge in edges:
        weight, v, u = edge
                
        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
            total_weight += weight
    
    return mst, total_weight


'''
graph = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
'edges': [
    (7, 'A', 'B'),
    (5, 'A', 'D'),
    (7, 'B', 'A'),
    (8, 'B', 'C'),
    (9, 'B', 'D'),
    (7, 'B', 'E'),
    (8, 'C', 'B'),
    (5, 'C', 'E'),
    (5, 'D', 'A'),
    (9, 'D', 'B'),
    (7, 'D', 'E'),
    (6, 'D', 'F'),
    (7, 'E', 'B'),
    (5, 'E', 'C'),
    (15, 'E', 'D'),
    (8, 'E', 'F'),
    (9, 'E', 'G'),
    (6, 'F', 'D'),
    (8, 'F', 'E'),
    (11, 'F', 'G'),
    (9, 'G', 'E'),
    (11, 'G', 'F'),
    ]
}

graph = {
'vertices': ['A', 'B', 'C', 'D'],
'edges': [
    (5, 'A', 'B'),
    (3, 'B', 'D'),
    (10, 'A', 'D'),
    (8, 'C', 'D'),
    (1, 'A', 'C'),
    ]
}

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 
    'edges': [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), 
    (7, 'B', 'E'), (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G'),
    ]
}

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F'], 
    'edges': [
    (3, 'A', 'E'), (6, 'C', 'E'),
    (2, 'A', 'B'), (4, 'D', 'E'), 
    (5, 'A', 'C'), (8, 'D', 'F'),
    (2, 'A', 'D'), (0, 'B', 'D'),
    (1, 'C', 'D')
    ]
}

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 
    'edges' : [
    (3, 'A', 'D'), (1, 'D', 'E'),
    (6, 'A', 'B'), (7, 'E', 'F'), 
    (4, 'B', 'C'), (12, 'C', 'F'),
    (2, 'B', 'E'), (8, 'D', 'G'),
    (9, 'E', 'H'), (10, 'F', 'I'),
    (11, 'G', 'H'), (5, 'H', 'I')
    ]
}

# 4 vertices best case (already mst)
graph = {
'vertices': ['A', 'B', 'C', 'D'],
'edges': [
    (5, 'A', 'B'),
    (3, 'B', 'D'),
    (1, 'A', 'C'),
    ]
}

# 4 vertices worst case (complete graph)
graph = {
'vertices': ['A', 'B', 'C', 'D'],
'edges': [
    (5, 'A', 'B'),
    (3, 'B', 'D'),
    (10, 'A', 'D'),
    (8, 'C', 'D'),
    (1, 'A', 'C'),
    (7, 'B', 'C')
    ]
}
'''
# helper function to load data in from file
def get_data(filename):
    with open(filename, 'r') as rf:

        # transform file into string and split along new line
        lines = rf.read().split("\n") # read the text file line by line which is splited by a new line

        # separate each line along the space characters
        data = [line.split(" ") for line in lines]

    return data

# load data in from file
graph = get_data('C:/Users/Saeah Go/OneDrive/Desktop/Fa2021/CS350/HW8/city-pairs.txt')
# print(graph)

d = {}

for path in graph:
    current_level = d
    for part in path:
        if part not in current_level:
            current_level[part] = {}
        current_level = current_level[part]

'''
for weight in mygraph:
    weight[2] = int(weight[2])

mygraph = [tuple(i) for i in mygraph]
'''

start = timeit.default_timer()	
mst, total_weight = kruskal(graph)
end = timeit.default_timer()

print("MST is: ", mst)
print("Total weight is: ", total_weight)
print("Running time is: ", end - start)