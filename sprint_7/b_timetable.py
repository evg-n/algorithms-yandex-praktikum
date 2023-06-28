def get_timetable(meetings):
    results = []

    current_start = i = 0
    while i < len(meetings):
        if meetings[i][0] >= current_start:
            results.append(meetings[i])
            current_start = meetings[i][1]
        i += 1
    return results


def main():
    n = int(input())
    meetings = []
    for _ in range(n):
        start, end = map(float, input().split())
        meetings.append((start, end))

    meetings.sort(key=lambda item: (item[1], item[0]))
    results = get_timetable(meetings)
    print(len(results))
    for result in results:
        # print(" ".join(map(str, result)))
        print(f"{result[0]:g} {result[1]:g}")


if __name__ == "__main__":
    main()
