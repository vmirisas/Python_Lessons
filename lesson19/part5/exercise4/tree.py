class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        n = Node(data)
        self.root = n

    def insert_left(self, node, data):
        n = Node(data)
        node.left = n

    def insert_right(self, node, data):
        n = Node(data)
        node.right = n

    def __str__(self):
        st = ""

        def rec_str(n):
            nonlocal st
            if n is None:
                st += "_"
            else:
                st += str(n.data)
                st += "("
                rec_str(n.left)
                st += ","
                rec_str(n.right)
                st += ")"

        rec_str(self.root)
        return st

