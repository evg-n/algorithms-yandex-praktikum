def max_contiguous_subarray(a):
    stat = {
        0: -1,
    }
    count = max_len = 0
    for i, val in enumerate(a):
        count += -1 if not val else 1

        if count in stat:
            max_len = max(max_len, i - stat[count])
        else:
            stat[count] = i
    return max_len


# print(max_contiguous_subarray([0, 0, 1, 0, 1, 1, 1, 0, 0, 0]))

if __name__ == "__main__":
    _ = int(input())
    results = list(map(int, input().split()))

    print(max_contiguous_subarray(results))
