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
            # print(dp)
    return dp[0][-1]


def main():
    n, m = map(int, input().split())
    points = get_points(n, m)

    print(calculate_most_flowers(points, n, m))


if __name__ == "__main__":
    main()
