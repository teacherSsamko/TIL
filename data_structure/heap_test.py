import random

from heap_ import Heap

# TO DO: why duplicated numbers are inserted?

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
heap.pop()
print(heap.heap_array)
heap.pop()
print(heap.heap_array)

insert_nums = set()
first = random.randint(1, 100)
insert_nums.add(first)
heap = Heap(first)
while len(insert_nums) < 10:
    insert_nums.add(random.randint(1, 15))

insert_nums = list(insert_nums)
while insert_nums:
    heap.insert(insert_nums.pop())

print(heap.heap_array)
