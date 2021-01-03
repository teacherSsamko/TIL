class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)


node1 = Node(1)
head = node1

for idx in range(2, 10):
    add(idx)

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)
