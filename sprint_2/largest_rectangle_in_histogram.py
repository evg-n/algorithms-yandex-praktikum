# https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import List


def calculate_borders(hist: List[int], left=True):
    stack = [0 if left else len(hist) - 1]
    borders = [-1 if left else len(hist)]

    if left:
        indexes = range(1, len(hist))
    else:
        indexes = range(len(hist) - 2, -1, -1)

    for i in indexes:
        cur_height = hist[i]

        while stack and hist[stack[-1]] >= cur_height:
            stack.pop()
        if not stack:
            borders.append(-1 if left else len(hist))
        else:
            borders.append(stack[-1])
        stack.append(i)

    return borders if left else list(reversed(borders))


def get_largest_rectangle_in_histogram(hist: List[int]) -> int:
    left = calculate_borders(hist)
    right = calculate_borders(hist, left=False)

    max_area = -1
    for i, height in enumerate(hist):
        max_area = max(max_area, height * (right[i] - left[i] - 1))
    return max_area


def main(*args, **kwargs):
    return get_largest_rectangle_in_histogram(*args, **kwargs)


if __name__ == "__main__":
    assert 30 == main(hist=[2, 7, 6, 9, 7, 5, 7, 3, 5])
    assert 14 == main(hist=[7, 7])
    assert 7 == main(hist=[7])
