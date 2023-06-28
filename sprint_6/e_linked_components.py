def find_linked_components(graph):
    colors = [-1] * len(graph)

    def dfs(node, current_color):
        current_results = []
        stack = [node]
        while stack:
            current_node = stack.pop()
            if colors[current_node] == -1:
                current_results.append(current_node)
            colors[current_node] = current_color

            for i in graph[current_node]:
                if colors[i] == -1:
                    stack.append(i)
        return current_results

    results = []
    for i in range(1, len(graph)):
        if colors[i] == -1:
            results.append(sorted(dfs(i, i)))
    return results


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

    results = find_linked_components(graph)
    print(len(results))

    for result in results:
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
