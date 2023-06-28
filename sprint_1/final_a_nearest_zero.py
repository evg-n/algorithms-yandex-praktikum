def read_input():
    n = int(input())
    house_numbers = list(map(int, input().split()))
    return (n, house_numbers)


def compute_distances_to_empty(n, nums):
    results = [n] * n  # filling the distances with the default large value

    # 1 pass: traverse and compute distances from left to right
    cur_dist_to_empty = None
    for i, num in enumerate(nums):
        if num == 0:
            results[i] = cur_dist_to_empty = 0
        elif cur_dist_to_empty is not None:
            cur_dist_to_empty += 1
            results[i] = cur_dist_to_empty

    # 2 pass: traverse and compute distances from right to left, choose min
    cur_dist_to_empty = None
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            cur_dist_to_empty = 0
        elif cur_dist_to_empty is not None:
            cur_dist_to_empty += 1
            results[i] = min(results[i], cur_dist_to_empty)

    return results


def print_results(results):
    # format and output the results
    print(" ".join(map(str, results)))


def main():
    n, house_numbers = read_input()
    print_results(compute_distances_to_empty(n, house_numbers))


if __name__ == "__main__":
    main()
