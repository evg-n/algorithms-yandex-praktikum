# from collections import defaultdict, deque


# # def get_topological_sort(graph, n):
# #     colors = ["white"] * n
# #     results = []

# #     def dfs(start_node):
# #         stack = [start_node]
# #         r = []
# #         while stack:
# #             current_node = stack.pop()
# #             if colors[current_node] == "white":
# #                 stack.append(current_node)
# #                 colors[current_node] = "gray"

# #                 for i in graph[current_node]:
# #                     if colors[i] == "white":
# #                         stack.append(i)

# #             elif colors[current_node] == "gray":
# #                 colors[current_node] = "black"
# #                 r.append(current_node)
# #         return r

# #     for i in range(1, n):
# #         if colors[i] == "white":
# #             results.extend(reversed(dfs(i)))

# #     return results

# def get_topological_sort_rec(graph, n):
#     colors = ["white"] * n
#     results = []

#     def dfs(node):

#         # if colors[node] == "white":
#         colors[node] = "gray"

#         for i in graph[node]:
#             if colors[i] == "white":
#                 dfs(i)
#         # elif colors[node] == "gray":
#         colors[node] = "black"
#         results.append(node)

#     for i in range(1, n):
#         if colors[i] == "white":
#             dfs(i)

#     return results

# def recursive_topological_sort(graph, node):
#     result = []
#     seen = set()

#     print(graph)
#     def recursive_helper(node):
#         for neighbor in graph[node]:
#             if neighbor not in seen:
#                 seen.add(neighbor)
#                 recursive_helper(neighbor)
#         result.insert(0, node)              # this line replaces the result.append line

#     for i in list(graph):
#         if i not in seen:
#             print('calling rec.. ', i)
#             recursive_helper(i)
#     return result

# def build_graph(m):
#     graph = defaultdict(list)
#     graph[1] = []
#     for _ in range(m):
#         vertex_from, vertex_to = map(int, input().split())
#         graph[vertex_from].append(vertex_to)

#     # for value in graph.values():
#         # value.sort(reverse=True)
#     return graph


# def main():
#     n, m = map(int, input().split())

#     graph = build_graph(m)
#     # results = get_topological_sort_rec(graph, n + 1)
#     results = recursive_topological_sort(graph, 1)

#     print(" ".join(map(str, results)))


# if __name__ == "__main__":
#     main()

from collections import defaultdict, deque


def recursive_topological_sort(n, graph):
    visited = [False] * n

    results = deque()

    def dfs(node):
        visited[node] = True
        for nei in graph[node]:
            if visited[nei] is False:
                dfs(nei)

        # if visited[node] == False:
        results.appendleft(node)

    for i in range(1, n):
        if visited[i] is False:
            dfs(i)
    return results


def build_graph(n, m):
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        vertex_from, vertex_to = map(int, input().split())
        graph[vertex_from].append(vertex_to)
    return graph


def main():
    n, m = map(int, input().split())
    graph = build_graph(n, m)

    # results = get_topological_sort_rec(graph, n + 1)
    results = recursive_topological_sort(n + 1, graph)
    print(" ".join(map(str, results)))


if __name__ == "__main__":
    main()
