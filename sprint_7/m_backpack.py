def get_max_mass(n, m, weights, values):
    dp = [[0] * (m + 1) for _ in range(n)]

    for j in range(m + 1):
        dp[0][j] = 0 if j < weights[0] else values[0]

    for i in range(1, n):
        for j in range(m + 1):
            dp[i][j] = max(
                dp[i - 1][j],
                0
                if j - weights[i] < 0
                else values[i] + dp[i - 1][j - weights[i]],
            )

    results = []

    i, j = n - 1, m

    while i > 0 and j > 0:
        left_weight = j - weights[i]
        if left_weight < 0 or dp[i - 1][j] > values[i] + dp[i - 1][left_weight]:
            i -= 1
        else:
            results.append(i + 1)
            j -= weights[i]
            i -= 1

    if j - weights[i] >= 0:
        # add i'th
        results.append(i + 1)

    return results


def main():
    n, m = map(int, input().split())
    weights = []
    values = []
    for _ in range(n):
        weight, value = map(int, input().split())
        weights.append(weight)
        values.append(value)

    # weights = list(map(int, input().split()))

    results = get_max_mass(n, m, weights, values)
    print(len(results))
    print(" ".join(map(str, results)))


if __name__ == "__main__":
    main()
