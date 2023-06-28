# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def rec_search(node, l, r):
    if not node:
        return

    if node.value >= l:
        rec_search(node.left, l, r)

    if l <= node.value <= r:
        print(node.value)

    if node.value <= r:
        rec_search(node.right, l, r)


def print_range(node, l, r):
    while node.value < l:
        node = node.right

    rec_search(node, l, r)


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8


if __name__ == "__main__":
    test()
