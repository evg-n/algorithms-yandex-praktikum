import math


def optimal_coupons_usage(prices):
    def calc_rec(i, activated_idxs, total_price=0, current_coupons=0):
        if i == len(prices):
            return (total_price, activated_idxs)

        skip_price, skip_idx = calc_rec(
            i + 1,
            activated_idxs,
            total_price + prices[i],
            current_coupons + 1 if prices[i] > 500 else current_coupons,
        )

        if current_coupons:
            add_price, add_idx = calc_rec(
                i + 1,
                activated_idxs[:] + [i + 1],
                total_price,
                current_coupons - 1,
            )
            return (
                (add_price, add_idx)
                if add_price < skip_price
                else (skip_price, skip_idx)
            )

        return (skip_price, skip_idx)

    return calc_rec(0, [])


def optimal_coupons_usage_dp(prices):
    n = len(prices)
    dp = [[math.inf] * (n + 1) for _ in range(n + 1)]

    dp[0][0] = 0
    for j in range(n):
        for i in range(j + 1):
            if i > 0:
                dp[i - 1][j + 1] = min(dp[i - 1][j + 1], dp[i][j])

            if prices[j] > 500:
                dp[i + 1][j + 1] = dp[i][j] + prices[j]
            else:
                dp[i][j + 1] = dp[i][j] + prices[j]

    j, i = n, 0
    while dp[i][j] == math.inf:
        i += 1
    min_price = dp[i][j]
    results = []
    while j:
        if i < n and dp[i + 1][j - 1] == dp[i][j]:
            results.append(j)
            i += 1
            j -= 1
        else:
            # move down left
            if prices[j - 1] > 500:
                i -= 1
                j -= 1
            else:
                j -= 1

    return min_price, list(reversed(results))


def main():
    n = int(input())
    prices = []
    for _ in range(n):
        prices.append(int(input()))
    # prices = [500, 501, 300]
    # prices = [502, 501, 503, 504]
    price, idxs = optimal_coupons_usage_dp(prices)
    print(price, len(idxs))
    print(" ".join(map(str, idxs)))


if __name__ == "__main__":
    main()
