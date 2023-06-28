import math


def relax(weights, current_node, neighbour_node, weight):
    if weights[neighbour_node] > weights[current_node] + weight:
        weights[neighbour_node] = weights[current_node] + weight


def get_min_non_visited(paths, visited):
    min_idx = None
    for i, weight in enumerate(paths):
        if not visited[i]:
            if min_idx is None or weight < paths[min_idx]:
                min_idx = i

    return min_idx


def dijkstra(graph, start_node):
    visited = [False] * len(graph)
    weights = [math.inf] * len(graph)
    weights[start_node] = 0

    while True:
        next_min_node = get_min_non_visited(weights, visited)
        if next_min_node is None:
            break

        visited[next_min_node] = True

        for i, weight in graph[next_min_node]:
            relax(weights, next_min_node, i, weight)

    return map(lambda item: -1 if item == math.inf else item, weights[1:])


def dijkstra_run(graph):
    for i in range(1, len(graph)):
        print(" ".join(map(str, dijkstra(graph, i))))


def build_graph(n, m):
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        vertex_from, vertex_to, weight = map(int, input().split())
        graph[vertex_from].append((vertex_to, weight))
        graph[vertex_to].append((vertex_from, weight))

    return graph


def main():
    n, m = map(int, input().split())
    graph = build_graph(n, m)

    dijkstra_run(graph)


if __name__ == "__main__":
    main()
