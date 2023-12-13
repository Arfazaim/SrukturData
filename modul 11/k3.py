# class Graph(object):
class Graph(object):
    
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
        
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        
    def __len__(self):
        return self.size
    
    def print_matrix(self):
        print('\n'.join([str(lst) for lst in self.adjMatrix]))

# Creating a graph with size 5
my_graph = Graph(5)

# Adding edges
my_graph.add_edge(0, 1)
my_graph.add_edge(0, 4)
my_graph.add_edge(1, 2)

# Removing an edge
my_graph.remove_edge(1, 4)

# Printing the adjacency matrix
my_graph.print_matrix()
