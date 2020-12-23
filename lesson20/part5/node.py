class Node:
    def __init__(self, descr="", neighbors=None):
        self.descr = descr
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors
