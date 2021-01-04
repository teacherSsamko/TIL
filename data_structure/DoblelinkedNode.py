class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class NodeManager:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def insert_before(self, prev_data, data):
        if self.head == None:
            self.head = Node(data)
            return True

        node = self.tail
        while node.data != prev_data:
            node = node.prev
            if node == None:
                return False
        new = Node(data)
        prev_new = node.prev
        prev_new.next = new
        new.next = node
        new.prev = prev_new
        node.prev = new
        return True

    def search_from_head(self, data):
        if self.head == None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

        return False

    def search_from_tail(self, data):
        if self.tail == None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev

        return False

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
