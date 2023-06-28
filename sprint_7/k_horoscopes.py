def get_longest_common_subsequence(str1, str2):
    dp = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

    for j in reversed(range(len(str1))):
        for i in reversed(range(len(str2))):
            if str1[j] == str2[i]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

    # restore the sequence
    i = j = 0
    print(dp[i][j])
    if dp[i][j] == 0:
        return

    str1_indexes = []
    str2_indexes = []
    while dp[i][j] != 0:
        if str1[j] == str2[i]:
            i += 1
            j += 1
            str1_indexes.append(j)
            str2_indexes.append(i)
        else:
            if dp[i][j + 1] > dp[i + 1][j]:
                j += 1
            else:
                i += 1
    print(" ".join(map(str, str1_indexes)))
    print(" ".join(map(str, str2_indexes)))


def main():
    _ = input()
    str1 = input().split()

    _ = input()
    str2 = input().split()
    get_longest_common_subsequence(str1, str2)


if __name__ == "__main__":
    main()
