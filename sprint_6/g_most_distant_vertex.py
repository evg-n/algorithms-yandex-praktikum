from collections import deque


def find_max_distance(graph, s):
    distance = [None] * len(graph)
    distance[s] = 0

    seen = [False] * len(graph)
    seen[s] = True

    queue = deque([s])

    max_distance = 0
    while queue:
        current_node = queue.pop()
        # seen[current_node] = True

        for i in graph[current_node]:
            if not seen[i]:
                # modify the variables
                distance[i] = distance[current_node] + 1
                max_distance = max(max_distance, distance[i])
                seen[i] = True
                queue.appendleft(i)

    return max_distance


def build_graph(n, m):
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        vertex_from, vertex_to = map(int, input().split())
        graph[vertex_from].append(vertex_to)
        graph[vertex_to].append(vertex_from)

    for i in range(1, n + 1):
        graph[i].sort()
    return graph


def main():
    n, m = map(int, input().split())
    graph = build_graph(n, m)

    start_node = int(input())
    results = find_max_distance(graph, start_node)
    print(results)

    # for result in results:
    # print(" ".join(map(str, results)))


if __name__ == "__main__":
    main()
