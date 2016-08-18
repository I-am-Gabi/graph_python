#!/usr/bin/env python

"""
edge.py: class to represents the edges structure of a graph.
"""

__author__ = "Gabriela Cavalcante"
__email__ = "gabicavalcantesilva@gmail.com"


class Edge:
    def __init__(self, o, d):
        self.__origin = o
        self.__destination = d

    def origin(self):
        """
        return the origin of the edges
        :return: origin of the edges
        """
        return self.__origin

    def destination(self):
        """
        return the destination of the edges
        :return: destination of the edges
        """
        return self.__destination

    def __str__(self):
        """
        override method to return the edges infos
        :return: edges infos
        """
        return "(" + str(self.__origin) + ", " + str(self.__destination) + ")"

    def __eq__(self, other):
        """
        compare two edges
        :param other: another edges to compare with self
        :return: true if they are equals, false otherwise
        """
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
