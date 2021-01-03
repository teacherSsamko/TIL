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

# lec2

node = head
node3 = Node(3.5)
search = True
while search:
    if node.data == 3:
        search = False
    else:
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)
