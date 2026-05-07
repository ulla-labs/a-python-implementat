import unittest
from src.graph import Graph
from src.bfs import breadth_first_search

class TestBFS(unittest.TestCase):
    def test_bfs_traversal(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        
        # Starting BFS from node 2
        expected_path = [2, 0, 3, 1]
        self.assertEqual(breadth_first_search(g, 2), expected_path)

    def test_single_node(self):
        g = Graph()
        g.add_edge(0, 0)
        self.assertEqual(breadth_first_search(g, 0), [0])

if __name__ == '__main__':
    unittest.main()