from collections import deque

def breadth_first_search(graph, start_node):
    """
    Performs a BFS traversal starting from start_node.
    Returns a list of nodes in the order they were visited.
    """
    visited = set()
    queue = deque([start_node])
    traversal_order = []

    visited.add(start_node)

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)

        for neighbor in graph.get_neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order