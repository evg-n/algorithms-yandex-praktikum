def find_target_day(x, days):
    if not days:
        return -1

    if x <= days[0]:
        return 1

    left, right = 1, len(days) - 1

    while left <= right:
        middle = (left + right) // 2
        if days[middle] >= x and days[middle - 1] < x:
            return middle + 1
        elif days[middle] < x:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def main():
    n = int(input())
    days = list(map(int, input().split()))
    s = int(input())

    first_day = find_target_day(s, days)
    second_day = find_target_day(s * 2, days)

    print(first_day, second_day)


if __name__ == "__main__":
    main()
