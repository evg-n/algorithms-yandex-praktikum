from typing import Dict
from collections import defaultdict


class Node:
    # feel free to change fields
    def __init__(self, weight, parent) -> None:
        self.weight = weight
        self.parent = parent
        self.children = []


def get_number_of_upgoing_paths(root: Node, x: int) -> int:
    cnt = 0

    def traverse(root):
        if not root:
            return []

        nonlocal cnt
        prefixes = [root.weight]

        if root.weight == x:
            cnt += 1

        for child in root.children:
            child_prefixes = traverse(child)
            for i, child_sum in enumerate(child_prefixes):
                if child_sum + root.weight == x:
                    cnt += 1

                child_prefixes[i] += root.weight
                prefixes.append(child_prefixes[i])

        return prefixes

    traverse(root)
    return cnt


def get_number_of_upgoing_paths_prefix_sums(root: Node, x: int) -> int:
    stat = defaultdict(int)
    stat[0] = 1

    def traverse(root, prefix_sums):
        if not root:
            return 0

        if not prefix_sums:
            prefix_sums.append(root.weight)
        else:
            prefix_sums.append(prefix_sums[-1] + root.weight)

        results = stat.get(prefix_sums[-1] - x, 0)
        stat[prefix_sums[-1]] += 1

        for child in root.children:
            results += traverse(child, prefix_sums)
        # results += traverse(root.right, prefix_sums)
        stat[prefix_sums[-1]] -= 1
        prefix_sums.pop()

        return results

    return traverse(root, [])


def read_tree(tree_size: int) -> Node:
    nodes = []
    root = None
    for i in range(tree_size):
        p, w = map(int, input().split())
        nodes.append(Node(w, p))
        if p == -1:
            root = nodes[i]
    for i in range(tree_size):
        if nodes[i].parent != -1:
            nodes[nodes[i].parent].children.append(nodes[i])
    return root


n, x = map(int, input().split())
tree = read_tree(n)
print(get_number_of_upgoing_paths_prefix_sums(tree, x))
