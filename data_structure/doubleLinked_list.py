from DoblelinkedNode import NodeManager

double_linked_list = NodeManager(0)
for data in range(1, 10):
    double_linked_list.insert(data)

double_linked_list.desc()
double_linked_list.insert_before(2, 1.5)
double_linked_list.desc()
