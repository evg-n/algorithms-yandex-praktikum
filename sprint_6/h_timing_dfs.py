from collections import defaultdict


def timed_dfs(n, graph, start_node):
    tin = [None] * n
    tout = [None] * n
    colors = ["white"] * n

    def dfs(start_node):
        time = 0
        stack = [start_node]
        while stack:
            current_node = stack.pop()

            if colors[current_node] == "white":
                # step-in

                colors[current_node] = "gray"
                tin[current_node] = time
                time += 1
                stack.append(current_node)

                for i in graph[current_node]:
                    if colors[i] == "white":
                        stack.append(i)

            elif colors[current_node] == "gray":
                tout[current_node] = time
                time += 1
                colors[current_node] = "black"

    dfs(start_node)

    return zip(tin[1:], tout[1:])


def build_graph(m):
    graph = defaultdict(list)

    for _ in range(m):
        vertex_from, vertex_to = map(int, input().split())
        graph[vertex_from].append(vertex_to)

    for value in graph.values():
        value.sort(reverse=True)
    return graph


def main():
    n, m = map(int, input().split())

    graph = build_graph(m)
    results = timed_dfs(n + 1, graph, 1)
    for result in results:
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
