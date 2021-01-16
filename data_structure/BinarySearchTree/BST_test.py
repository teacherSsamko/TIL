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

# delete 10 nodes
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) < 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

for del_num in delete_nums:
    assert bst.delete(del_num) is not False

# research tree

for x in bst_nums:
    if x not in delete_nums:
        assert bst.search(x) is True
    else:
        assert bst.search(x) is False

print('delete success')
