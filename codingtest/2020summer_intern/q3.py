def solution(total_sp, skills):
    answer = []
    return answer


class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

class SkillTree:
    def __init__(self, root=None):
        self.root = root
        


def skillTree(skills):
    top_node = None
    for skill in skills:
        if not top_node:
            top_node = Node(skill[0])
            top_node.left = skill[1]
        



skills = [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]
skill_tree = [1, [2, [3, [4, 5, 6]]]]
total_sp = 121
print(solution(total_sp,skills))