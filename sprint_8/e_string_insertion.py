def main():
    s = input()
    n = int(input())

    new_strings = {}
    for _ in range(n):
        t, k = input().split()
        new_strings[int(k)] = t

    result = []
    for i in range(len(s)):
        if i in new_strings:
            result.append(new_strings[i])
        result.append(s[i])

    if len(s) in new_strings:
        result.append(new_strings[len(s)])

    print("".join(result))


if __name__ == "__main__":
    main()
