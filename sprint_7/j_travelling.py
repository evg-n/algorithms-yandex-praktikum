def get_longest_increasing_subsequence(r):
    dp = [1] * len(r)
    results = []

    for i, num in enumerate(r):
        for j in range(i):
            if r[j] >= num:
                continue
            dp[i] = max(dp[i], 1 + dp[j])
    max_value = max(dp)
    for i in reversed(range(len(dp))):
        if dp[i] == max_value:
            results.append(i + 1)
            max_value -= 1
    return list(reversed(results))


def main():
    _ = int(input())
    r = list(map(int, input().split()))
    results = get_longest_increasing_subsequence(r)
    print(len(results))
    print(" ".join(map(str, results)))


if __name__ == "__main__":
    main()
