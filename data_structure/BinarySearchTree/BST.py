from Node import Node, NodeManager

head = Node(1)
BST = NodeManager(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

print(BST.search(8))
print(BST.search(7))
