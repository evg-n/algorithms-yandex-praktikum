from collections import defaultdict


def dfs(n, graph, start_node):
    def inner_dfs(node):
        stack = [node]

        results = []
        while stack:
            current_node = stack.pop()
            if colors[current_node] == "white":
                colors[current_node] = "grey"
                results.append(current_node)
                stack.append(current_node)

                for i in graph[current_node]:
                    if colors[i] == "white":
                        stack.append(i)

            elif colors[current_node] == "grey":
                colors[current_node] = "black"
        return results

    colors = ["white"] * (n + 1)
    return inner_dfs(start_node)


def build_graph(m):
    graph = defaultdict(list)
    for _ in range(m):
        vertex_from, vertex_to = map(int, input().split())
        graph[vertex_from].append(vertex_to)
        graph[vertex_to].append(vertex_from)

    for indexes in graph.values():
        indexes.sort(reverse=True)
    return graph


def main():
    n, m = map(int, input().split())
    graph = build_graph(m)

    start_node = int(input())
    results = dfs(n, graph, start_node)
    print(" ".join(map(str, results)))


if __name__ == "__main__":
    main()
