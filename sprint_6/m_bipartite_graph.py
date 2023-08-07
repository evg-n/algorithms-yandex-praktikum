from copy import copy

from collections import defaultdict


def build_graph(n, m):
    graph = defaultdict(list)
    for _ in range(m):
        u, v = tuple(map(int, input().split()))
        graph[u].append(v)
        graph[v].append(u)
    return graph


def is_bipartite(n, graph):
    colors = [-1] * (n + 1)

    def bipartition(vertex_index):
        left = {vertex_index: True}
        right = {neighbour: True for neighbour in graph[vertex_index]}

        colors[vertex_index] = 1
        queue = [*right]
        while queue:
            curr_vertex = queue.pop()
            colors[curr_vertex] = 1
            is_left = curr_vertex in left
            for neighbour in graph[curr_vertex]:
                if (is_left and neighbour in left) or (
                    not is_left and neighbour in right
                ):
                    return False
                if is_left:
                    right[neighbour] = True
                else:
                    left[neighbour] = True
                if colors[neighbour] == -1:
                    queue.append(neighbour)
        return True

    for i, vertex in enumerate(list(graph), start=1):
        if colors[i] == -1:
            result = bipartition(vertex)
            if not result:
                return False

    return True


def main():
    n, m = map(int, input().split())
    graph = build_graph(n, m)
    print("YES" if is_bipartite(n, graph) else "NO")


if __name__ == "__main__":
    main()
