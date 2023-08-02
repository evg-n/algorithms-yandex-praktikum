# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def get_paths_sum(root, cur_sum):
    if not root.left and not root.right:
        return cur_sum * 10 + root.value

    updated_sum = cur_sum * 10 + root.value
    result = 0
    if root.left:
        result += get_paths_sum(root.left, updated_sum)
    if root.right:
        result += get_paths_sum(root.right, updated_sum)
    return result


def solution(root) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    return get_paths_sum(root, 0)


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275


if __name__ == "__main__":
    test()
