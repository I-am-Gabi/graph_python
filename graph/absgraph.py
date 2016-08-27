#!/usr/bin/env python

"""
absgraph.py: simple abstract class to represents the graph structure.

To represent a finite graph, we used a adjacency list.
Each list contain a set of neighbors of a vertex in the graph.
"""
import random as rand
from abc import ABCMeta, abstractmethod
import logging
from collections import deque

from enum import Enum

# from graph.undigraph import UnDiGraph

__author__ = "Gabriela Cavalcante"
__email__ = "gabicavalcantesilva@gmail.com"
logging.basicConfig(filename='trace.log', level=logging.DEBUG)


class Status(Enum):
    gray = 0
    white = 1
    black = 2


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

    @abstractmethod
    def connected(self):
        """
        checks if the graph is connected
        """
        pass

    @abstractmethod
    def make_path(self, node, path, opt=None):
        """
        aux method to build the path among the nodes
        :param node: current node
        :param path: path in progress
        :return:
        """
        pass

    def bfs(self):
        """
        complexity: O(|V| + |E|)
            To each vertex u, the algorithm will pass by each edge from u to v, so that (u, v)
        :return:
        """
        status = []
        sequence = []
        distance = []
        cont_components = 1
        # initializes status
        for node in range(0, self.nb_vertices):
            status.append(Status.white)
            distance.append(-1)
        # takes a random vertex
        n = rand.randint(0, self.nb_vertices - 1)
        # changes status and distance
        status[n] = Status.gray
        distance[n] = 0
        # adds initial vertex into queue
        queue = deque([n])
        # calls aux method bfs
        self.__aux_bfs(queue, status, sequence, distance)

        # if there is a node not visited
        while Status.white in status:
            n = 0
            while status[n] != Status.white: n += 1
            status[n] = Status.gray
            distance[n] = 0
            queue = deque([n])
            self.__aux_bfs(queue, status, sequence, distance)
            cont_components += 1
        return sequence, distance, cont_components

    def __aux_bfs(self, queue, status, sequence, distance):
        while queue:
            u = queue.popleft()
            sequence.append(u)
            print u
            for v in self.adjacent_list(u):
                if status[v] is Status.white:
                    status[v] = Status.gray
                    distance[v] = distance[u] + 1
                    queue.append(v)
            status[u] = Status.black

    def dfs(self):
        status = []
        # initializes status
        for node in range(0, self.nb_vertices):
            status.append(Status.white)
        self.__aux_dfs(status, rand.randint(0, self.nb_vertices - 1))
        for v in range(0, self.nb_vertices):
            if status[v] is Status.white:
                self.__aux_dfs(status, v)

    def __aux_dfs(self, status, node):
        status[node] = Status.gray
        print node
        for v in self.adjacent_list(node):
            if status[v] is Status.white:
                status[v] = Status.gray
                self.__aux_dfs(status, v)
        status[node] = Status.black

    @abstractmethod
    def show(self):
        """
        prints the graph
        """
        pass
