class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

# Creating a graph with 5 vertices
my_graph = Graph(5)

# Adding edges
my_graph.add_edge(0, 1)
my_graph.add_edge(0, 4)
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(1, 4)
my_graph.add_edge(2, 3)
my_graph.add_edge(3, 4)

# Printing the adjacency list representation
my_graph.print_agraph()
