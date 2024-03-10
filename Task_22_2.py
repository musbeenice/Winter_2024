# Вторая задача к двадцать второму занятию

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_binary_tree(nodes):
    node_dct = {}

    for parent, child in nodes:
        if parent not in node_dct:
            node_dct[parent] = Node(parent)
        if child not in node_dct:
            node_dct[child] = Node(child)

    for parent, child in nodes:
        parent_node = node_dct[parent]
        child_node = node_dct[child]
        if not parent_node.left:
            parent_node.left = child_node
        elif not parent_node.right:
            parent_node.right = child_node

    return node_dct[nodes[0][0]]


bin_tree = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8)]

tree = build_binary_tree(bin_tree)

# Поиск максимального пути от вершины до конечного узла:


def find_max_path(node, path):
    if not node:
        return 0

    if not node.left and not node.right:
        return path

    path += 1

    left_sum = find_max_path(node.left, path)
    right_sum = find_max_path(node.right, path)

    return max(right_sum, left_sum)


max_path = find_max_path(tree, 0)
print(f"Максимальный путь от вершины со значением {tree.value} до конечного узла равен {max_path}")
