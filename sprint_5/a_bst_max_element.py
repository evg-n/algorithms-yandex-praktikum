# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing
from collections import deque

LOCAL = False

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    max_el = root.value
    queue = deque([root])

    while len(queue):
        current_node = queue.pop()

        if current_node.value is not None:
            max_el = max(max_el, current_node.value)
        if current_node.left:
            queue.appendleft(current_node.left)
        if current_node.right:
            queue.appendleft(current_node.right)

    return max_el


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == "__main__":
    test()
