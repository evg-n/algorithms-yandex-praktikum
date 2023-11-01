from typing import List


def get_longest_increasing_path(matrix: List[List[int]]) -> int:
    n, m = len(matrix), len(matrix[0])

    computed = [[0] * m for _ in range(n)]

    def traverse_point(i, j):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
            return 0

        current = matrix[i][j]
        current_max_path = 0
        # left
        if j > 0 and matrix[i][j - 1] > current:
            if computed[i][j - 1]:
                current_max_path = max(current_max_path, computed[i][j - 1])
            else:
                current_max_path = max(
                    current_max_path, traverse_point(i, j - 1)
                )

        # top
        if i > 0 and matrix[i - 1][j] > current:
            if computed[i - 1][j]:
                current_max_path = max(current_max_path, computed[i - 1][j])
            else:
                current_max_path = max(
                    current_max_path, traverse_point(i - 1, j)
                )

        # right
        if j < m - 1 and matrix[i][j + 1] > current:
            if computed[i][j + 1]:
                current_max_path = max(current_max_path, computed[i][j + 1])
            else:
                current_max_path = max(
                    current_max_path, traverse_point(i, j + 1)
                )

        # down
        if i < n - 1 and matrix[i + 1][j] > current:
            if computed[i + 1][j]:
                current_max_path = max(current_max_path, computed[i + 1][j])
            else:
                current_max_path = max(
                    current_max_path, traverse_point(i + 1, j)
                )

        computed[i][j] = current_max_path + 1
        return computed[i][j]

    max_computed = 0
    for i in range(n):
        for j in range(m):
            if not computed[i][j]:
                traverse_point(i, j)
            max_computed = max(max_computed, computed[i][j])

    return max_computed


def read_matrix() -> List[List[int]]:
    n, m = map(int, input().split())
    matrix = []
    if n == 0 or m == 0:
        return [[]]
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix


matrix = read_matrix()
print(get_longest_increasing_path(matrix))
