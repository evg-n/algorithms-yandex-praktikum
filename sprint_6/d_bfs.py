from collections import deque


def bfs(graph, node):
    colors = ["white"] * (len(graph))
    colors[node] = "gray"

    results = []
    queue = deque([node])
    while queue:
        current_node = queue.pop()
        results.append(current_node)
        for i in graph[current_node]:
            if colors[i] == "white":
                colors[i] = "gray"
                queue.appendleft(i)

        colors[current_node] = "black"

    return results


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
    results = bfs(graph, start_node)
    # print(len(results))

    # for result in results:
    print(" ".join(map(str, results)))


if __name__ == "__main__":
    main()
