def get_longest_common_prefix(strings):
    s = strings[0]
    l = len(s)

    for i in range(1, len(strings)):
        cur_str = strings[i]
        for j in range(min(l, len(cur_str))):
            if cur_str[j] != s[j]:
                l = j
                break
    return l


def main():
    n = int(input())
    strings = []

    for _ in range(n):
        strings.append(input())

    print(get_longest_common_prefix(strings))


if __name__ == "__main__":
    main()
