if __name__ == "__main__":
    n = int(input())

    memo = {}
    results = []
    for _ in range(n):
        activity_name = input()
        if activity_name not in memo:
            memo[activity_name] = True
            results.append(activity_name)

    for activity in results:
        print(activity)
