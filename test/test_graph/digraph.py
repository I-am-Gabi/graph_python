import unittest

from graph.digraph import DiGraph


class TestDiGraph(unittest.TestCase):
    def test_initialize(self):
        g = DiGraph(3)
        self.assertEqual(g.nb_edges, 0)
        self.assertEqual(g.nb_vertices, 3)

    def test_add_edges(self):
        g = DiGraph(2)
        g.add(0, 1)
        g.add(0, 0)
        g.add(1, 0)
        self.assertEqual(g.adjacent_list(0)[0], 1)
        self.assertEqual(g.adjacent_list(0)[1], 0)
        self.assertEqual(g.adjacent_list(1)[0], 0)

    def test_remove_edges(self):
        g = DiGraph(2)
        g.add(0, 1)
        self.assertEqual(g.adjacent_list(0)[0], 1)
        g.remove(0, 1)
        self.assertEqual(g.nb_edges, 0)

    def test_degrees(self):
        g = DiGraph(4)
        g.add(0, 0)
        g.add(0, 1)
        g.add(0, 2)
        g.add(1, 1)
        g.add(1, 2)
        g.add(3, 0)
        g.add(3, 2)

        # node 0
        self.assertEqual(g.degree(0), 5)
        self.assertEqual(g.in_degree(0), 2)
        self.assertEqual(g.out_degree(0), 3)
        # node 1
        self.assertEqual(g.degree(1), 4)
        self.assertEqual(g.in_degree(1), 2)
        self.assertEqual(g.out_degree(1), 2)
        # node 2
        self.assertEqual(g.degree(2), 3)
        self.assertEqual(g.in_degree(2), 3)
        self.assertEqual(g.out_degree(2), 0)
        # node 3
        self.assertEqual(g.degree(3), 2)
        self.assertEqual(g.in_degree(3), 0)
        self.assertEqual(g.out_degree(3), 2)

    def test_strongly_connected(self):
        g = DiGraph(2)
        g.add(0, 0)
        g.add(0, 1)
        g.add(1, 0)
        g.add(1, 1)
        self.assertTrue(g.connected())
        self.assertTrue(g.strongly_connected())

        g = DiGraph(4)
        g.add(0, 1)
        g.add(0, 2)
        g.add(1, 1)
        g.add(2, 3)
        self.assertFalse(g.connected())
        self.assertTrue(g.strongly_connected())

    # TODO: use mock to handle with random
    # TODO: improve the execution control
    def test_bfs(self):
        g = DiGraph(3)
        g.add(0, 1)
        g.add(0, 2)
        seq, dist, comp = g.bfs()
        self.assertEqual(dist[0], 0)
        if seq[0] is not 0:
            if seq[1] is not 0:
                self.assertEqual(dist[1], 0)
                self.assertEqual(dist[2], 0)
            elif seq[2] is 1:
                self.assertEqual(dist[1], 1)
                self.assertEqual(dist[2], 0)
            else:
                self.assertEqual(dist[1], 0)
                self.assertEqual(dist[2], 1)
        else:
            self.assertEqual(dist[0], 0)
            self.assertEqual(dist[1], 1)
            self.assertEqual(dist[2], 1)


if __name__ == '__main__':
    unittest.main()
