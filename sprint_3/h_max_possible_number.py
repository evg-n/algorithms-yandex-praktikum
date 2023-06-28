from functools import cmp_to_key


def compare(x, y):
    return -1 if str(x) + str(y) < str(y) + str(x) else 1


def max_possible_number(nums):
    nums.sort(key=cmp_to_key(compare), reverse=True)
    return "".join(map(str, nums))


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(max_possible_number(nums))
