from heapq import heappush, heappop


def get_max_capital(m, k, props):
    props.sort()
    i, j, capital = 0, 0, m

    p_heap = []
    while i < len(props) and j < k:
        if props[i][0] > capital:
            if not p_heap:
                return capital

            most_valuable = heappop(p_heap)
            capital += -most_valuable[0]
            j += 1
        else:
            heappush(p_heap, (-props[i][1], props[i][0]))
            i += 1

    while p_heap and j < k:
        capital += -heappop(p_heap)[0]
        j += 1

    return capital


def main():
    n, k = list(map(int, input().split()))
    properties = []
    for _ in range(n):
        c, p = list(map(int, input().split()))
        properties.append((c, p))
    m = int(input())
    result = get_max_capital(m, k, properties)
    print(result)


if __name__ == "__main__":
    main()
