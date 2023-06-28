def is_equal(shift, a, b):
    # a[i] + shift == b[i]
    return list(map(lambda item: item + shift, a)) == b


def find_index(template, numbers, start=0):
    for i in range(start, len(numbers) - len(template) + 1):
        shift = template[0] - numbers[i]
        if is_equal(shift, numbers[i : i + len(template)], template):
            return i
    return -1


def find(template, numbers):
    # cycle with search positions
    start = 0
    results = []
    while True:
        result = find_index(template, numbers, start)
        if result == -1:
            break
        start = result + 1
        results.append(start)

    return results


def main():
    _ = input()
    numbers = list(map(int, input().split()))
    _ = input()
    template = list(map(int, input().split()))
    indexes = find(template, numbers)
    print(" ".join(map(str, indexes)))


if __name__ == "__main__":
    main()
