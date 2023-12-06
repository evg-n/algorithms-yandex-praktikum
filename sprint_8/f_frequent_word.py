from collections import defaultdict


def main():
    n = int(input())

    max_freq = 0
    stat = defaultdict(int)

    for _ in range(n):
        s = input()
        stat[s] += 1
        if stat[s] > max_freq:
            max_freq = stat[s]

    stat = sorted([k for k, v in stat.items() if v == max_freq])
    print(stat[0])


if __name__ == "__main__":
    main()
