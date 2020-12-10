from tree import Tree
from tree import Node


class BinarySearchTree(Tree):
    def __init__(self):
        super(BinarySearchTree, self).__init__()

    def insert(self, data):
        if self.root is None:
            self.insert_root(data)
            print(str(data) + " inserted!")

        node = self.root
        while True:
            if data == node.data:
                print(f"{node.data} is already in the tree")
                break
            elif data < node.data:
                if node.left is None:
                    node.left = Node(data)
                    print(str(data) + " inserted")
                    break
                else:
                    node = node.left
            else:  # data > node.data
                if node.right is None:
                    node.right = Node(data)
                    print(str(data) + " inserted")
                    break
                else:
                    node = node.right

    def inorder(self):
        ret_list = []

        def rec_inorder(node):
            nonlocal ret_list
            if node is not None:
                rec_inorder(node.left)
                ret_list += [node.data]
                rec_inorder(node.right)

        rec_inorder(self.root)
        return ret_list
