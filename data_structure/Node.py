class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeManager:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node.next:
            print(node.data)
            node = node.next
        print(node.data)
