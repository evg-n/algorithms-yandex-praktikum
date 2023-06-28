import math


def get_points(n, m):
    points = []
    for _ in range(n):
        points.append(list(map(int, list(input()))))
    return points


def get_dp(n, m):
    return [[-math.inf] * (m + 1) for _ in range(n + 1)]


def calculate_most_flowers(points, n, m):
    dp = get_dp(n, m)
    for i in range(n - 1, -1, -1):
        for j in range(1, m + 1):
            dp[i][j] = points[i][j - 1] + max(0, dp[i][j - 1], dp[i + 1][j])

    print(dp[0][-1])
    return backtrack_path(dp, n, m)


def backtrack_path(dp, n, m):
    path = []
    i = 0
    j = m

    while i != n - 1 or j != 1:
        # left >= down, go left
        if dp[i][j - 1] >= dp[i + 1][j]:
            path.append("R")
            j -= 1
        else:
            path.append("U")
            i += 1
    return reversed(path)


def main():
    n, m = map(int, input().split())
    points = get_points(n, m)

    path = calculate_most_flowers(points, n, m)
    print("".join(path))


if __name__ == "__main__":
    main()
