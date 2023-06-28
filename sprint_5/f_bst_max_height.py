# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def get_max_height(root):
    if not root:
        return 0

    return 1 + max(get_max_height(root.left), get_max_height(root.right))


def solution(root) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    return get_max_height(root)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5) == 3


if __name__ == "__main__":
    test()
