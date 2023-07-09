from collections import defaultdict
from typing import List


# Time limit, O(N^3)
def find_guadriplets(nums: List[int], s: int) -> List[List[int]]:
    if len(nums) < 4:
        return []
    nums.sort()

    results = []

    def two_sum(lo: int, hi: int, i_num: int, j_num: int) -> None:
        complement = s - (i_num + j_num)
        # find pairs from lo to hi which sum equals 'complement'
        while lo < hi:
            current_sum = nums[lo] + nums[hi]
            if current_sum > complement:
                hi -= 1
            elif current_sum < complement:
                lo += 1
            else:
                # update the results
                results.append([i_num, j_num, nums[lo], nums[hi]])

                lo += 1
                hi -= 1

                # skip lowest duplicates
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1

    for i, i_num in enumerate(nums):
        # skip i-th duplicates
        if i == 0 or i_num != nums[i - 1]:
            for j in range(i + 1, len(nums)):
                j_num = nums[j]
                # skip j-th duplicates
                if j == i + 1 or j_num != nums[j - 1]:
                    two_sum(j + 1, len(nums) - 1, i_num, j_num)

    return results


def find_quadriplets_memory(nums: List[int], s: int) -> List[List[int]]:
    results = set()
    if len(nums) < 4:
        return results

    two_sums_cache = defaultdict(list)
    for i, i_num in enumerate(nums):
        for j, j_num in enumerate(nums[i + 1 :], start=i + 1):
            two_sums_cache[i_num + j_num].append([i, j])

    for i, i_num in enumerate(nums):
        for j, j_num in enumerate(nums[i + 1 :], start=i + 1):
            complement = s - (i_num + j_num)
            if complement in two_sums_cache:
                # check indexes
                pairs = two_sums_cache[complement]
                for k, n in pairs:
                    if k != i and k != j and n != i and n != j:
                        results.add(tuple(sorted([i_num, j_num, nums[k], nums[n]])))

    return sorted(results)


def main():
    _ = input()
    s = int(input())
    nums = list(map(int, input().split()))
    results = find_quadriplets_memory(nums, s)
    print(len(results) if results else 0)
    for result in results:
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
