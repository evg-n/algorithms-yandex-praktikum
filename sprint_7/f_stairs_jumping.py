def calculate_jumping_ways(n, k):
    MODULUS = 10**9 + 7

    dp = [0] * n
    i = 1
    while i < n and i <= k:
        dp[i] = 1
        i += 1

    for i in range(2, n):
        for j in range(i - k if i - k > 0 else 0, i):
            dp[i] += dp[j] % MODULUS

    return dp[-1] % MODULUS


def main():
    n, k = map(int, input().split())
    print(calculate_jumping_ways(n, k))


if __name__ == "__main__":
    main()
