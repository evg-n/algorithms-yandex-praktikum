LIMIT = 10**4


def get_min_banknotes(x, nominals):
    sums = [0] * (x + 1)
    for nominal in nominals:
        if nominal < x:
            sums[nominal] = 1
        elif nominal == x:
            return 1

    for i in range(2, LIMIT):
        for j, num in enumerate(sums):
            if num == i - 1:
                for nominal in nominals:
                    new_sum = j + nominal

                    if new_sum == x:
                        return i

                    if new_sum > x:
                        break
                        # continue

                    if sums[new_sum] == 0:
                        sums[new_sum] = i

    return -1


def main():
    x = int(input())
    _ = int(input())

    nominals = list(sorted(set(map(int, input().split()))))

    print(get_min_banknotes(x, nominals))


if __name__ == "__main__":
    main()
