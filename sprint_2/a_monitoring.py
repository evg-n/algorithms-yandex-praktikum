def main():
    n = int(input())
    m = int(input())

    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    def print_transponed(n, m, matrix):
        for i in range(m):
            line = []
            for j in range(n):
                line.append(matrix[j][i])
            print(" ".join(map(str, line)))

    print_transponed(n, m, matrix)


if __name__ == "__main__":
    main()
