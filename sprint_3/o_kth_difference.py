from typing import List


# Naive implementation
def get_kth_difference(k: int, areas: List[int]) -> int:
    def insert(a: List[int], x: int):
        a[-1] = x
        i = len(a) - 2
        while i >= 0 and x < a[i]:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = x

    results = []
    for i, left in enumerate(areas):
        for j in range(i + 1, len(areas)):
            current_diff = abs(left - areas[j])
            if len(results) < k:
                results.append(current_diff)
                if len(results) == k:
                    results.sort()
            elif current_diff < results[-1]:
                insert(results, current_diff)

    return results[k - 1]


# Optimal implementation
# W - [0, nums[-1] - nums[0]]
# N - len of nums
# TC: O(N lg N + N lg W). First is for sorring, second is for (lg W) runs of `possible`
# function, which takes linear N time.
def get_kth_difference_binary_search(k: int, nums: List[int]) -> int:
    def possible(guess, nums):
        left = count = 0
        for right, x in enumerate(nums):
            while x - nums[left] > guess:
                left += 1
            count += right - left
        return count >= k

    nums.sort()
    left, right = 0, nums[-1] - nums[0]

    while left < right:
        mid = (left + right) // 2
        if possible(mid, nums):
            right = mid
        else:
            left = mid + 1
    return left


def main():
    _ = input()
    areas = list(map(int, input().split()))
    k = int(input())
    print(get_kth_difference_binary_search(k, areas))


if __name__ == "__main__":
    main()
