def count_profit(prices):
    total_profit = 0

    i = 0
    while i < len(prices) - 1:
        # search low buy price
        while i < len(prices) - 1 and prices[i + 1] < prices[i]:
            i += 1
        buy_price = i

        # search best sell price
        i += 1
        while i < len(prices) - 1 and prices[i + 1] > prices[i]:
            i += 1

        if buy_price < len(prices) and i < len(prices):
            total_profit += prices[i] - prices[buy_price]

    return total_profit


def main():
    _ = input()
    prices = list(map(int, input().split()))

    print(count_profit(prices))


if __name__ == "__main__":
    main()
