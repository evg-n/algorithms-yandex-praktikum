def calculate_max_money(m, piles):
    result = i = 0
    while m >= 0 and i < len(piles):
        price, volume = piles[i]
        if m >= volume:
            result += price * volume
            m -= volume
        else:
            result += price * m
            m = 0

        i += 1
    return result


if __name__ == "__main__":
    m = int(input())
    n = int(input())

    piles = []
    for _ in range(n):
        price, volume = map(int, input().split())
        piles.append((price, volume))

    piles.sort(key=lambda item: item[0], reverse=True)
    print(calculate_max_money(m, piles))
