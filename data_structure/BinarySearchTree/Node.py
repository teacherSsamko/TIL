class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeManager:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        self.current_node = self.root
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.root
        self.parent = self.root
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        """Case 1,2,3
        Case 1: the Node is a Leaf Node
        Csee 2: the Node has one child. replace current node to smallest node of right children.
        Csee 3: the Node has two children
        """
        if self.search(value):
            # CASE 1
            if self.current_node.left == None and self.current_node.right == None:
                if value < self.parent.value:
                    self.parent.left = None
                else:
                    self.parent.right = None
            # CASE 2
            elif self.current_node.right == None and self.current_node.left:
                if value < self.parent.value:
                    self.parent.left = self.current_node.left
                else:
                    self.parent.right = self.current_node.left
            elif self.current_node.left == None and self.current_node.right:
                if value < self.parent.value:
                    self.parent.left = self.current_node.right
                else:
                    self.parent.right = self.current_node.right
            # CASE 3
            # TO DO: make the duplicated code below as a function
            elif self.current_node.left and self.current_node.right:
                # 3-1
                if value < self.parent.value:
                    self.change_node = self.current_node.right
                    self.change_node_parent = self.self.current_node.right

                    while self.change_node.left:
                        self.change_node_parent = self.change_node
                        self.change_node = self.change_node.left

                    if self.change_node.right:
                        self.change_node_parent.left = self.change_node.right
                    else:
                        self.change_node_parent.left = None

                    self.parent.left = self.change_node
                    self.change_node.left = self.current_node.left
                    self.change_node.right = self.current_node.right
                # 3-2
                else:
                    self.change_node = self.current_node.right
                    self.change_node_parent = self.self.current_node.right

                    while self.change_node.left:
                        self.change_node_parent = self.change_node
                        self.change_node = self.change_node.left

                    if self.change_node.right:
                        self.change_node_parent.left = self.change_node.right
                    else:
                        self.change_node_parent.left = None

                    # only following 1 line is different from CASE 3-1
                    self.parent.right = self.change_node

                    self.change_node.left = self.current_node.left
                    self.change_node.right = self.current_node.right

            del self.current_node

        else:
            return False
