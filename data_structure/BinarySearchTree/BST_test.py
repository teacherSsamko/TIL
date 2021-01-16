import random

from Node import Node, NodeManager


bst_nums = set()
while len(bst_nums) < 100:
    bst_nums.add(random.randint(0, 999))

# print(bst_nums)
root = Node(500)
bst = NodeManager(root)
for x in bst_nums:
    bst.insert(x)

for x in bst_nums:
    assert bst.search(x) is True

print('search success')
