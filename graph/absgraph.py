#!/usr/bin/env python

"""
absgraph.py: simple abstract class to represents the graph structure.

To represent a finite graph, we used a adjacency list.
Each list contain a set of neighbors of a vertex in the graph.
"""

from abc import ABCMeta, abstractmethod
import logging

__author__ = "Gabriela Cavalcante"
__email__ = "gabicavalcantesilva@gmail.com"
logging.basicConfig(filename='trace.log', level=logging.DEBUG)


class AbsGraph:
    __metaclass__ = ABCMeta

    def __init__(self, nodes):
        self._nbEdges = 0
        self._adjacencyList = []
        for i in range(0, nodes):
            self._adjacencyList.append([])

    @property
    def nb_vertices(self):
        """
        returns number of vertices
        :return: number of vertices
        """
        return len(self._adjacencyList)

    @property
    def nb_edges(self):
        """
        returns number of edges
        :return: number of edges
        """
        return self._nbEdges

    def adjacent_list(self, node):
        """
        returns the adjacency list of a node
        :param node:
        :return:
        """
        return self._adjacencyList[node]

    def add_edge(self, e):
        """
        adds edge e to the graph
        :param e: new edge
        """
        self.add(e.origin(), e.destination())

    @abstractmethod
    def add(self, origin, destination):
        """
        adds edge (origin, destination) to the graph
        :param origin: origin node
        :param destination: destination node
        """
        pass

    def remove_edge(self, e):
        """
        removes the edge e from the graph
        :param e: edge to remove
        """
        self.add(e.origin(), e.destination())

    @abstractmethod
    def remove(self, origin, destination):
        """
        removes the edge (origin, destination) from the graph
        :param origin: origin node
        :param destination: destination node
        """
        pass

    @abstractmethod
    def degree(self, node):
        """
        returns the total degree of node
        :param node: node to calculate degree
        """
        pass

    def connected(self):
        """
        checks if the graph is connected
        """
        path = [0] * self.nb_vertices
        logging.debug('vertices > ' + str(range(0, self.nb_vertices)))
        for u in range(0, self.nb_vertices):
            path[u] = 1
            for v in self.adjacent_list(u):
                self.make_path(v, path)

            logging.debug(str(u) + ' connected with ' + str(path))
            if 0 in path: return False
            path = [0] * self.nb_vertices
        return True

    def make_path(self, node, path):
        """
        aux method to build the path among the nodes
        :param node: current node
        :param path: path in progress
        :return:
        """
        if path[node] == 1: return
        path[node] = 1
        for adj in self.adjacent_list(node):
            self.make_path(adj, path)
            path[adj] = 1

    @abstractmethod
    def show(self):
        """
        prints the graph
        """
        pass
