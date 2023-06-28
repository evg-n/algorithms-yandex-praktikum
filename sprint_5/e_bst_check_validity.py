# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing
import math

LOCAL = False

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def is_binary_search_tree(root, low=-math.inf, high=math.inf):
    if not root:
        return True

    if low < root.value < high:
        return is_binary_search_tree(
            root.left, low, root.value
        ) and is_binary_search_tree(root.right, root.value, high)

    return False


def solution(root) -> bool:
    return is_binary_search_tree(root)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == "__main__":
    test()
