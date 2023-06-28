from typing import List


def get_max_houses_to_buy_number(k: int, prices: List[int]) -> int:
    prices.sort()

    i = 0
    while i < len(prices) and prices[i] <= k:
        k -= prices[i]
        i += 1
    return i


def main():
    _, k = map(int, input().split())
    prices = list(map(int, input().split()))
    print(get_max_houses_to_buy_number(k, prices))


if __name__ == "__main__":
    main()
