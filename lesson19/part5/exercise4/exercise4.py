from tree import Tree
from binarySearchTree import BinarySearchTree

t = Tree()
t.insert_root("A")
t.insert_left(t.root, "B")
t.insert_right(t.root, "C")
t.insert_left(t.root.left, "D")
t.insert_right(t.root.left, "E")
t.insert_left(t.root.right, "F")
print(t)


t2 = BinarySearchTree()
t2.insert(2)
t2.insert(5)
t2.insert(8)
t2.insert(11)
t2.insert(1)
t2.insert(7)
print(t2)
print(t2.inorder())