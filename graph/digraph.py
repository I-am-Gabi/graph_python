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

    def components(self):
        path = [0] * self.nb_vertices
        m = [[0] * self.nb_vertices] * self.nb_vertices
        for u in range(0, self.nb_vertices):
            path[u] = 1
            for v in self.adjacent_list(u):
                self.make_path(v, path, [])
                m[u] = path
            path = [0] * self.nb_vertices

        cont = 1
        comp = [0] * self.nb_vertices
        for i in range(0, self.nb_vertices):
            for j in range(0, self.nb_vertices):
                if m[i][j] == 1 and m[j][i] == 1:
                    if comp[i] != 0:
                        comp[j] = comp[i]
                    elif comp[j] != 0:
                        comp[i] = comp[j]
                    else:
                        comp[i] = comp[j] = cont
                        cont += 1
        return m, comp

    def strongly_connected(self):
        """
        checks if the graph is connected
        """
        path = [0] * self.nb_vertices
        opt = []
        for u in range(0, self.nb_vertices):
            path[u] = 1
            for v in self.adjacent_list(u):
                if v not in opt:
                    self.make_path(v, path, opt)
                else:
                    path = [1] * self.nb_vertices
                    break

            if 0 in path:
                return False
            else:
                opt.append(u)

            path = [0] * self.nb_vertices
        return True

    def make_path(self, node, path, opt=None):
        """
        aux method to build the path among the nodes
        :param opt:
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

    def connected(self):
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

    def topological_sort(self):
        queue = []
        final_queue = []
        for u in range(0, self.nb_vertices):
            if self._inDegree[u] == 0:
                queue.append(u)

        while queue:
            u = queue.pop()
            final_queue.append(u)
            for v in self.adjacent_list(u):
                self._inDegree[v] -= 1
                if self._inDegree[v] == 0:
                    queue.append(v)
        return final_queue

    def cyclic(self):
        q = self.topological_sort()
        if q is not self.nb_vertices:
            return True
        return False



g = DiGraph(6)
g.add(0, 1)
g.add(0, 2)
g.add(1, 2)
g.add(2, 0)
g.add(3, 4)
g.add(4, 3)
m, comp = g.components()
print m
print comp