from collections import defaultdict


def read_simluator_view():
    SIMULATOR_LINES = 4
    stat = defaultdict(int)
    for _ in range(SIMULATOR_LINES):
        # skip all except digits on input
        digits = list(map(int, filter(lambda x: x.isdigit(), input())))

        # build cache for later processing by each round
        for digit in digits:
            stat[digit] += 1
    return stat


def count_score(stat, k):
    return sum(bool(stat[i]) and k * 2 >= stat[i] for i in range(1, 10))


def main():
    k = int(input())
    sim_view = read_simluator_view()

    print(count_score(sim_view, k))


if __name__ == "__main__":
    main()
