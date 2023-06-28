def prefix_function(s):
    p = [None] * len(s)
    p[0] = 0

    for i in range(1, len(s)):
        k = p[i - 1]

        while k > 0 and s[k] != s[i]:
            k = p[k - 1]

        if s[k] == s[i]:
            k += 1
        p[i] = k

    return p


def main():
    s = input()
    p = prefix_function(s)
    print(" ".join(map(str, p)))


if __name__ == "__main__":
    main()
