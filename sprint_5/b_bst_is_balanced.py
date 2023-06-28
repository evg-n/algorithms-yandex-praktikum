# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def check_height(root):
    if not root:
        return 0

    lh = check_height(root.left)
    rh = check_height(root.right)

    if lh is False or rh is False or abs(lh - rh) > 1:
        return False

    return max(lh, rh) + 1


def solution(root) -> bool:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    result = check_height(root)
    return bool(result)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == "__main__":
    test()
