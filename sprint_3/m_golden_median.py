# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List


# O(logN+logM) = O(log(N*M))
def get_golden_median(a: List[int], b: List[int]) -> int:
    def solve(k: int, a_left: int, a_right: int, b_left: int, b_right: int) -> int:
        # base condition
        if a_left > a_right:
            return b[k - a_left]
        if b_left > b_right:
            return a[k - b_left]

        a_index, b_index = (a_left + a_right) // 2, (b_left + b_right) // 2
        a_value, b_value = a[a_index], b[b_index]
        if a_index + b_index < k:
            # reduce the left smaller part
            if a_value > b_value:
                return solve(k, a_left, a_right, b_index + 1, b_right)
            else:
                return solve(k, a_index + 1, a_right, b_left, b_right)
        else:
            # reduce the right bigger part
            if a_value > b_value:
                return solve(k, a_left, a_index - 1, b_left, b_right)
            else:
                return solve(k, a_left, a_right, b_left, b_index - 1)

    na, nb = len(a), len(b)
    n = na + nb
    if n % 2:
        return solve(n // 2, 0, na - 1, 0, nb - 1)
    else:
        n1 = solve(n // 2 - 1, 0, na - 1, 0, nb - 1)
        n2 = solve(n // 2, 0, na - 1, 0, nb - 1)
        return (n1 + n2) / 2


# O(log(min(N,M)))
def get_golden_median_improved(a: List[int], b: List[int]) -> int:
    m, n = len(a), len(b)
    if m > n:
        return get_golden_median_improved(b, a)

    left, right = 0, m

    while left <= right:
        partitionA = (left + right) // 2
        partitionB = (n + m + 1) // 2 - partitionA

        # setup 4 elements
        minRightA = float("inf") if partitionA == m else a[partitionA]
        maxLeftA = float("-inf") if partitionA == 0 else a[partitionA - 1]

        minRightB = float("inf") if partitionB == n else b[partitionB]
        maxLeftB = float("-inf") if partitionB == 0 else b[partitionB - 1]

        # compare 4 elements
        if maxLeftA <= minRightB and maxLeftB <= minRightA:
            # found the partition, return results
            if (n + m) % 2:
                return max(maxLeftA, maxLeftB)
            else:
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2

        elif maxLeftA > minRightB:
            # going left, decreasing maxLeftA, increasing minRightB
            right = partitionA - 1
        else:
            left = partitionA + 1


def main(*args, **kwargs):
    return get_golden_median_improved(*args, **kwargs)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    a_sorted = list(map(int, input().split()))
    b_sorted = list(map(int, input().split()))
    print(f"{main(a_sorted, b_sorted):g}")
