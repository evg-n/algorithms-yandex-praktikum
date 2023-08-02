# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0, size=0):
            self.right = right
            self.left = left
            self.value = value
            self.size = size


def get_size(node):
    return node.size if node else 0


def split(root, k):
    if not root:
        return None, None

    if get_size(root.left) + 1 <= k:
        k_updated = k - (get_size(root.left) + 1)
        root.right, right_tree = split(root.right, k_updated)
        root.size -= get_size(right_tree)
        return root, right_tree

    # going to the left subtree
    left_tree, root.left = split(root.left, k)
    root.size -= get_size(left_tree)
    return left_tree, root


def test():
    node1 = Node(None, None, 3, 1)
    node2 = Node(None, node1, 2, 2)
    node3 = Node(None, None, 8, 1)
    node4 = Node(None, None, 11, 1)
    node5 = Node(node3, node4, 10, 3)
    node6 = Node(node2, node5, 5, 6)
    left, right = split(node6, 4)
    assert left.size == 4
    assert right.size == 2


if __name__ == "__main__":
    test()
