#!/usr/bin/env python

"""
digraph.py: abstract class to represents the directed graph structure.
"""

from graph.absgraph import AbsGraph
from graph.undigraph import UnDiGraph

__author__ = "Gabriela Cavalcante"
__email__ = "gabicavalcantesilva@gmail.com"


class DiGraph(AbsGraph):
    def __init__(self, nodes):
        super(DiGraph, self).__init__(nodes)
        self._inDegree = [0] * nodes

    def add(self, origin, destination):
        if destination not in self._adjacencyList[origin]:
            self._adjacencyList[origin].append(destination)
            self._nbEdges += 1
            self._inDegree[destination] += 1

    def remove(self, origin, destination):
        if destination in self._adjacencyList[origin]:
            self._adjacencyList[origin].remove(destination)
            self._nbEdges -= 1
            self._inDegree[destination] -= 1

    def show(self):
        for u in range(0, self.nb_vertices):
            for v in self.adjacent_list(u):
                print str(u) + " -> " + str(v)

    def degree(self, node):
        return len(self.adjacent_list(node)) + self._inDegree[node]

    def connected(self):
        """
        checks if the graph is connected
        """
        path = [0] * self.nb_vertices
        for u in range(0, self.nb_vertices):
            path[u] = 1
            for v in self.adjacent_list(u):
                self.make_path(v, path)

            if 0 in path:
                return False
            path = [0] * self.nb_vertices
        return True

    def in_degree(self, node):
        """
        calculates the indegree
        :param node: calculates the node's indegree
        :return: the indegree
        """
        return self._inDegree[node]

    def out_degree(self, node):
        """
        calculates the outdegree
        :param node: calculates the node's outdegree
        :return: the outdegree
        """
        return len(self.adjacent_list(node))

    def strongly_connected(self):
        """
        checks if the undigraph made from the original digraph is connected
        :return: true if it's connected, false otherwise
        """
        g = self.__undigraph()
        return g.connected()

    def __undigraph(self):
        """
        creates a undigraph from the original digraph
        :return: undigraph from the original digraph
        """
        graph = UnDiGraph(self.nb_vertices)
        for u in range(0, self.nb_vertices):
            for v in self.adjacent_list(u):
                graph.add(u, v)
        return graph


g = DiGraph(3)
g.add(0, 1)
g.add(0, 2)
g.bfs()
g.dfs()