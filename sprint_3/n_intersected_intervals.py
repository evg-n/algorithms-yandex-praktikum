def process_intervals(a):
    if not a:
        return
    a.sort(key=lambda item: (item[0], -item[1]))
    results = [a[0]]

    for i in range(1, len(a)):
        cur = a[i]

        if cur[0] > results[-1][1]:
            results.append(cur)
        else:
            prev = results.pop()
            results.append([prev[0], max(prev[1], cur[1])])
    return results


def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    results = process_intervals(a)
    for result in results:
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
