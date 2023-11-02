from node import Node

# Comment it before submitting
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.neighbours = []


def cloneGraph(node) -> Node:
    if not node:
        return None
    c_node = Node(node.val)

    queue = set([(node, c_node)])
    visited = {}
    materialized = {node: c_node}
    while queue:
        vertice, c_vertice = queue.pop()
        visited[vertice] = True

        for n in vertice.neighbours:
            if n in materialized:
                neighbour = materialized[n]
            else:
                neighbour = Node(n.val)
                materialized[n] = neighbour
            c_vertice.neighbours.append(neighbour)
            if n not in visited:
                queue.add((n, neighbour))
    return c_node
