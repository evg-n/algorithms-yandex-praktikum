from typing import List


def get_max_digits(numbers):
    max_val = max(numbers)
    digits = 0
    while max_val:
        max_val >>= 1
        digits += 1
    return digits


def get_max_xor(numbers: List[int]) -> int:
    max_digits = get_max_digits(numbers)

    max_xor = 0
    for i in reversed(range(max_digits)):
        max_xor <<= 1
        cur_xor = max_xor | 1

        # build a prefix set
        prefixes = {n >> i for n in numbers}

        max_xor |= any(prefix ^ cur_xor in prefixes for prefix in prefixes)
    return max_xor


n = int(input())
numbers = list(map(int, input().split()))
print(get_max_xor(numbers))
