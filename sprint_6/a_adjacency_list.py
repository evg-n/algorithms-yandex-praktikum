def main():
    n, m = map(int, input().split())

    results = [None] * (n + 1)
    for _ in range(m):
        vertex_from, vertex_to = map(int, input().split())
        if results[vertex_from] is None:
            results[vertex_from] = [vertex_to]
        else:
            results[vertex_from].append(vertex_to)

    for val in results[1:]:
        if val:
            print(f"{len(val)} {' '.join(map(str, sorted(val)))}")
        else:
            print(0)


if __name__ == "__main__":
    main()
