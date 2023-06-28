# pink - 0
# yellow - 1
# crimson - 2


def count_sort(colors):
    stat = [0] * 3

    for color in colors:
        stat[color] += 1

    results = []
    for i, color_count in enumerate(stat):
        results.extend([i] * color_count)

    return results


if __name__ == "__main__":
    n = input()
    colors = map(int, input().split())
    results = count_sort(colors)
    print(" ".join(map(str, results)))
