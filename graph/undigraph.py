#!/usr/bin/env python

"""
undigraph.py: abstract class to represents the undirected graph structure.
"""
from graph.absgraph import AbsGraph
import logging

__author__ = "Gabriela Cavalcante"
__email__ = "gabicavalcantesilva@gmail.com"


class UnDiGraph(AbsGraph):
    def __init__(self, nodes):
        super(UnDiGraph, self).__init__(nodes)

    def add(self, origin, destination):
        if destination not in self._adjacencyList[origin]:
            self._adjacencyList[origin].append(destination)
            if destination is not origin:
                self._adjacencyList[destination].append(origin)
            self._nbEdges += 1

    def remove(self, origin, destination):
        if destination in self._adjacencyList[origin]:
            self._adjacencyList[origin].remove(destination)
            self._adjacencyList[destination].remove(origin)
            self._nbEdges -= 1

    def degree(self, node):
        return len(self.adjacent_list(node))

    def show(self):
        for u in range(0, self.nb_vertices):
            for v in self.adjacent_list(u):
                print str(u) + " <-> " + str(v)


g = UnDiGraph(4)
g.add(0, 1)
g.add(0, 2)
g.add(1, 1)
g.add(2, 3)
logging.info("connected: " + str(g.connected()))

g = UnDiGraph(4)
g.add(0, 1)
g.add(1, 1)
g.add(1, 2)
logging.info("connected: " + str(g.connected()))

g = UnDiGraph(4)
g.add(0, 1)
g.add(0, 2)
g.add(1, 1)
g.add(2, 3)
logging.info("connected: " + str(g.connected()))