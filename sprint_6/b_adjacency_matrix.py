def main():
    n, m = map(int, input().split())
    a = [[False] * n for _ in range(n)]

    for _ in range(m):
        vertex_from, vertex_to = map(int, input().split())
        a[vertex_from - 1][vertex_to - 1] = True

    for i in range(n):
        for j in range(n):
            print(int(a[i][j]), end=" ")
        print()


if __name__ == "__main__":
    main()
