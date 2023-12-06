def check_parts(s, i):
    if len(s) % i:
        return 0

    parts = {s[k : k + i] for k in range(0, len(s), i)}
    # print(s, i, parts)
    return 0 if len(parts) > 1 else len(s) // i


# lviiwxaxplviiwxaxp


def get_max_repeat_number(s):
    pi = [0] * len(s)
    k = 0

    for i in range(1, len(s)):
        k = pi[i - 1]

        while k > 0 and s[k] != s[i]:
            k = pi[k - 1]

        if s[k] == s[i]:
            k += 1

        pi[i] = k
        if k * 2 == i + 1:
            result = check_parts(s, k)
            if result:
                return result

    return 1


def main():
    s = input()

    print(get_max_repeat_number(s))


if __name__ == "__main__":
    main()
