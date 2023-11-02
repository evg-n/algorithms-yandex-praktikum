from typing import List, Optional


class Node:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.id = id


def get_tree_border(root: Node) -> List[int]:
    results = []
    cur_level = [root]
    while cur_level:
        next_level = []
        for i, node in enumerate(cur_level):
            if (
                i == 0
                or i == len(cur_level) - 1
                or (node.left is None and node.right is None)
            ):
                results.append(node.id)

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        cur_level = next_level

    return results


def read_tree() -> Node:
    size, root_id = map(int, input().split())
    nodes = [Node() for _ in range(size)]
    for i in range(size):
        left, right = map(int, input().split())
        nodes[i].id = i
        nodes[i].left = nodes[left] if left != -1 else None
        nodes[i].right = nodes[right] if right != -1 else None
    return nodes[root_id]


def main():
    root = read_tree()
    print(" ".join(map(str, get_tree_border(root))))


if __name__ == "__main__":
    main()
