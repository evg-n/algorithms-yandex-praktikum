from functools import lru_cache


def get_cash_variants(banknotes, m):
    @lru_cache(maxsize=None)
    def get_cash_rec(sum, start_index=0):
        if sum == 0:
            return 1
        if sum < 0:
            return 0

        variants = 0
        for i in range(start_index, len(banknotes)):
            variants += get_cash_rec(sum - banknotes[i], i)
        return variants

    return get_cash_rec(m)


def get_cache_variants_dp(banknotes, m):
    dp = [0] * (m + 1)
    dp[0] = 1
    for nominal in banknotes:
        for i in range(nominal, m + 1):
            dp[i] += dp[i - nominal]

    return dp[m]


def main():
    m = int(input())
    _ = int(input())
    banknotes = list(map(int, input().split()))
    # print(get_cash_variants(banknotes, m))
    print(get_cache_variants_dp(banknotes, m))


if __name__ == "__main__":
    main()
