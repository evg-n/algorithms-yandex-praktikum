from collections import defaultdict


def get_number_of_good_pairs(numbers) -> int:
    count = 0
    stat = defaultdict(int)
    for number in numbers:
        reduced = number % 200
        if reduced not in stat:
            stat[reduced] = 0
        else:
            stat[reduced] += 1
            count += stat[reduced]
    return count


n = int(input())
numbers = list(map(int, input().split()))
print(get_number_of_good_pairs(numbers))
