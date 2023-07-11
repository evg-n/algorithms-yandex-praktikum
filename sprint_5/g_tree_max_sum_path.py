# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


max_val = float("-inf")


def inner(root):
    global max_val

    if not root:
        return float("-inf")

    left_sum = inner(root.left)
    right_sum = inner(root.right)

    max_val = max(
        max_val, left_sum, right_sum, left_sum + right_sum + root.value
    )

    return max(root.value, left_sum + root.value, right_sum + root.value)


def solution(root) -> int:
    result = inner(root)
    return max(max_val, result)


def test():
    node1 = Node(5, None, None)
    node2 = Node(1, None, None)
    node3 = Node(-3, node2, node1)
    node4 = Node(2, None, None)
    node5 = Node(2, node4, node3)
    assert solution(node5) == 6


if __name__ == "__main__":
    test()
