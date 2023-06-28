def count_unique_trees(n):
    cache = [1] * (n + 1)

    for num in range(2, n + 1):
        result = 0
        for root in range(1, num + 1):
            left_count = root - 1
            right_count = num - root
            result += cache[left_count] * cache[right_count]
        cache[num] = result

    return cache[n]


if __name__ == "__main__":
    n = int(input())
    print(count_unique_trees(n))
