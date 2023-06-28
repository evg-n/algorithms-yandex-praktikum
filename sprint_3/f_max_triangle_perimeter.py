def main():
    _ = int(input())
    lens = list(map(int, input().split()))
    lens.sort(reverse=True)

    i = 0
    while lens[i] >= lens[i + 1] + lens[i + 2]:
        i += 1

    print(sum(lens[i : i + 3]))


if __name__ == "__main__":
    main()
