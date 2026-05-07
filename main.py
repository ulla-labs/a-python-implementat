from src.graph import Graph
from src.bfs import breadth_first_search

def main():
    # Initialize Graph
    g = Graph()
    
    # Constructing a sample graph
    # 0 -> 1, 2
    # 1 -> 2
    # 2 -> 0, 3
    # 3 -> 3
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    start_node = 2
    print(f"Starting Breadth First Search from node: {start_node}")
    
    result = breadth_first_search(g, start_node)
    
    print("BFS Traversal Order:", " -> ".join(map(str, result)))

if __name__ == "__main__":
    main()