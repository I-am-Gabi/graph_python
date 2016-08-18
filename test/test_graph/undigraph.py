import unittest

from graph.undigraph import UnDiGraph


class TestUnDiGraph(unittest.TestCase):
    def test_initialize(self):
        g = UnDiGraph(3)
        self.assertEqual(g.nb_edges, 0)
        self.assertEqual(g.nb_vertices, 3)

    def test_add_edges(self):
        g = UnDiGraph(2)
        g.add(0, 1)
        self.assertEqual(g.nb_edges, 1)
        self.assertEqual(g.adjacent_list(0)[0], 1)
        self.assertEqual(g.adjacent_list(1)[0], 0)
        g.add(1, 0)
        self.assertEqual(g.nb_edges, 1)

    def test_remove_edges(self):
        g = UnDiGraph(2)
        g.add(0, 1)
        self.assertEqual(g.nb_edges, 1)
        g.remove(0, 1)
        self.assertEqual(g.nb_edges, 0)

    def test_degrees(self):
        g = UnDiGraph(3)
        g.add(0, 0)
        g.add(0, 1)
        g.add(0, 2)

        # node 0
        self.assertEqual(g.degree(0), 3)
        # node 1
        self.assertEqual(g.degree(1), 1)
        # node 2
        self.assertEqual(g.degree(2), 1)

    def test_connected(self):
        g = UnDiGraph(2)
        g.add(0, 0)
        g.add(0, 1)
        g.add(1, 1)
        self.assertTrue(g.connected())

        g = UnDiGraph(4)
        g.add(0, 0)
        g.add(0, 1)
        g.add(0, 2)
        g.add(1, 2)
        self.assertFalse(g.connected())

        g = UnDiGraph(4)
        g.add(0, 1)
        g.add(0, 2)
        g.add(1, 1)
        g.add(2, 3)
        self.assertTrue(g.connected())

if __name__ == '__main__':
    unittest.main()
