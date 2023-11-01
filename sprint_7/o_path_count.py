from collections import defaultdict

MOD = 1000000007


def get_path_count_dp(a, b, graph, n):
    dp = [0] * (n + 1)
    dp[b] = 1

    visited = {}

    def dfs(v_from, graph):
        neighbours = graph.get(v_from, {})
        for j, conn_count in neighbours.items():
            if j not in visited:
                dfs(j, graph)
            dp[v_from] = (dp[v_from] + (dp[j] * conn_count)) % MOD
        visited[v_from] = True

    dfs(a, graph)
    return dp[a]


def main():
    n, m = list(map(int, input().split()))
    graph = defaultdict(dict)
    for _ in range(m):
        v_from, v_to = list(map(int, input().split()))
        if v_to not in graph[v_from]:
            graph[v_from][v_to] = 1
        else:
            graph[v_from][v_to] += 1

    a, b = list(map(int, input().split()))
    count = get_path_count_dp(a, b, graph, n)
    print(count)


if __name__ == "__main__":
    main()
