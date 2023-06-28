from collections import deque


def get_shortest_path(path, t):
    count = 0
    while path[t] is not None:
        count += 1
        t = path[t]

    return count


def get_shortest_distance(graph, s, t):
    if s == t:
        return 0
    seen = [False] * len(graph)
    seen[s] = True

    previous = [None] * len(graph)

    queue = deque([s])

    while queue:
        node = queue.pop()

        for i in graph[node]:
            if not seen[i]:
                seen[i] = True
                previous[i] = node
                if i == t:
                    # found
                    return get_shortest_path(previous, t)
                queue.appendleft(i)

    return -1


def build_graph(n, m):
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        vertex_from, vertex_to = map(int, input().split())
        graph[vertex_from].append(vertex_to)
        graph[vertex_to].append(vertex_from)

    return graph


def main():
    n, m = map(int, input().split())
    graph = build_graph(n, m)

    s, t = map(int, input().split())
    results = get_shortest_distance(graph, s, t)
    print(results)


if __name__ == "__main__":
    main()
