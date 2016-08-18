import unittest
from graph.edge import Edge


class TestEdge(unittest.TestCase):
    def test_nodes(self):
        e = Edge(1, 2)
        self.assertEqual(e.origin(), 1)
        self.assertEqual(e.destination(), 2)

    def test_str(self):
        e = Edge(1, 2)
        e_str = e.__str__()
        expected_str = "(" + str(1) + ", " + str(2) + ")"
        self.assertEqual(e_str, expected_str)

    def test_eq(self):
        e1 = Edge(1, 2)
        e2 = Edge(1, 2)
        self.assertTrue(e1, e2)

if __name__ == '__main__':
    unittest.main()
