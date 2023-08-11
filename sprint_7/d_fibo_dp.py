MOD_VALUE = 10**9 + 7


def get_nth_fibo(n, mod=MOD_VALUE):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD_VALUE
    return dp[n]


def main():
    n = int(input())
    print(get_nth_fibo(n))


if __name__ == "__main__":
    main()
