# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root1, root2) -> bool:
    queue1 = [root1]
    queue2 = [root2]

    while queue1 and queue2:
        first = queue1.pop()
        second = queue2.pop()

        if not first and not second:
            continue

        if first and not second or second and not first:
            return False

        if first.value != second.value:
            return False

        queue1.append(first.left)
        queue1.append(first.right)
        queue2.append(second.left)
        queue2.append(second.right)

    if queue1 or queue2:
        return False

    return True


def test():
    node1 = Node(1, None, None)
    node2 = Node(2, None, None)
    node3 = Node(3, node1, node2)

    node4 = Node(1, None, None)
    node5 = Node(2, None, None)
    node6 = Node(3, node4, node5)

    assert solution(node3, node6)


if __name__ == "__main__":
    test()
