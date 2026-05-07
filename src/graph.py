from collections import defaultdict

class Graph:
    """
    A simple directed graph representation using an adjacency list.
    """
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        """Adds a directed edge from node u to node v."""
        self.adj_list[u].append(v)

    def get_neighbors(self, node):
        return self.adj_list[node]