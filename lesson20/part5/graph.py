from node import Node


class Graph:
    def __init__(self):
        self.nodes = []

    def add_vertex(self, descr="", neighbors=None):
        if neighbors is None:
            neighbors = []

        self.nodes += [Node(descr, neighbors)]

    # Private function to find the possition of a node with description {descr} in nodes[]
    def __index_of(self, descr):
        for i in range(len(self.nodes)):
            if descr == self.nodes[i].descr:
                return i

    def add_edge(self, descr1, descr2):
        index1 = self.__index_of(descr1)
        index2 = self.__index_of(descr2)

        node1 = self.nodes[index1]
        node2 = self.nodes[index2]
        node1.neighbors += [node2]
        node2.neighbors += [node1]
        # or else it could be written like this
        # self.nodes[index1].neighbors += [self.nodes[index2]]
        # self.nodes[index2].neighbors += [self.nodes[index1]]

    def neighbors(self, descr):
        return self.nodes[self.__index_of(descr)].neighbors

    def __str__(self):
        st = ""
        for node in self.nodes:
            st += f"\n{node.descr}: "
            for neighbor in node.neighbors:
                st += f"{neighbor.descr} "
        return st
