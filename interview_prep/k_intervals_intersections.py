def get_intersections(a, b):
    results = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i][0] == b[j][0]:
            if a[i][1] == b[j][1]:
                results.append(a[i])
                i += 1
                j += 1
            elif a[i][1] > b[j][1]:
                results.append(b[j])
                j += 1
            else:
                results.append(a[i])
                i += 1
        elif a[i][1] < b[j][0]:
            i += 1
        elif b[j][1] < a[i][0]:
            j += 1
        elif a[i][0] < b[j][0]:
            if b[j][1] >= a[i][1]:
                results.append((b[j][0], a[i][1]))
                i += 1
            else:
                results.append(b[j])
                j += 1
        else:
            if a[i][1] >= b[j][1]:
                results.append((a[i][0], b[j][1]))
                j += 1
            else:
                results.append(a[i])
                i += 1

    return results


def main():
    n = int(input())
    n_intervals = []
    for _ in range(n):
        x, y = list(map(int, input().split()))
        n_intervals.append((x, y))

    m_intervals = []
    m = int(input())
    for _ in range(m):
        x, y = list(map(int, input().split()))
        m_intervals.append((x, y))

    results = get_intersections(n_intervals, m_intervals)
    for interval in results:
        print(" ".join(map(str, interval)))


if __name__ == "__main__":
    main()
