#!/usr/bin/env python

"""
undigraph.py: abstract class to represents the undirected graph structure.
"""
import logging

from graph.absgraph import AbsGraph

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

    def connected(self):
        """
        checks if the graph is connected
        """
        path = [0] * self.nb_vertices
        opt = []
        u = 0
        path[u] = 1
        for v in self.adjacent_list(u):
            self.make_path(v, path, opt)

        if 0 in path:
            return False
        else:
            return True

    def make_path(self, node, path, opt=None):
        """
        aux method to build the path among the nodes
        :param node: current node
        :param path: path in progress
        :return:
        """
        if path[node] == 1 and node not in opt:
            return
        path[node] = 1
        for v in self.adjacent_list(node):
            if v not in opt:
                self.make_path(v, path, opt)
            else:
                path[v] = 1

    def path_to(self, from_, to_):
        print from_, to_
        status = [0] * self.nb_vertices
        status[from_] = 1
        path = [from_]
        for node in self.adjacent_list(from_):
            if self.aux_path_to(node, to_, status, path):
                return path
        return False

    def aux_path_to(self, from_, to_, status, path):
        print from_, to_, status[from_]
        if status[from_] is 1:
            return False

        status[from_] = 1
        path.append(from_)

        if from_ == to_:
            return True

        for node in self.adjacent_list(from_):
            if self.aux_path_to(node, to_, status, path):
                return True
        path.remove(from_)


g = UnDiGraph(4)
g.add(0, 1)
g.add(0, 2)
g.add(1, 1)
g.add(2, 3)
g.connected()
