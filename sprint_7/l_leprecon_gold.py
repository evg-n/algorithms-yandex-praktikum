def backpack(m, weights):
    dp = [0] * (m + 1)
    n = len(weights)
    for i in range(n):
        for j in range(m, weights[i] - 1, -1):
            dp[j] = max(dp[j], weights[i] + dp[j - weights[i]])
    return dp[m]


def main():
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))

    print(backpack(m, weights))


if __name__ == "__main__":
    main()
