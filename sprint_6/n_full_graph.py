def main():
    n, m = list(map(int, input().split()))

    graph = [set() for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        if x != y:
            graph[x - 1].add(y - 1)
            graph[y - 1].add(x - 1)

    unique_target = (n * n - n) / 2
    if m < unique_target:
        return "NO"

    for vertex in graph:
        if n - len(vertex) != 1:
            return "NO"
    return "YES"


if __name__ == "__main__":
    print(main())
