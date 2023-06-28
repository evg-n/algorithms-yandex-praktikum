from typing import List


def max_partition(nums: List[int]) -> int:
    is_block_closed = True
    max_block_value, counter = 0, 0
    for i, value in enumerate(nums):
        if is_block_closed:
            max_block_value = value
            is_block_closed = False
        else:
            max_block_value = max(max_block_value, value)

        if i == max_block_value:
            counter += 1
            is_block_closed = True

    if not is_block_closed:
        counter += 1

    return counter


def main():
    _ = int(input())
    nums = list(map(int, input().split()))

    print(max_partition(nums))


if __name__ == "__main__":
    main()
