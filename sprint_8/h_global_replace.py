def replace_all(pattern, s, replace_with=None):
    # result = []
    result_string = []
    dummy_s = pattern + "#" + s
    p = [None] * (len(pattern))
    p[0] = 0

    p_prev = 0
    start = end = 0
    for i in range(1, len(dummy_s)):
        k = p_prev

        while k > 0 and dummy_s[k] != dummy_s[i]:
            k = p[k - 1]

        if dummy_s[i] == dummy_s[k]:
            k += 1
        if i < len(pattern):
            p[i] = k

        p_prev = k
        if k == len(pattern):
            end = i - len(pattern) * 2
            # print("PART: ", start, end, k)
            result_string.append(s[start:end])
            result_string.append(replace_with)
            start = end + len(pattern)

    if start < len(s):
        result_string.append(s[start:])
    return result_string


def main():
    s = input()
    pattern = input()
    replace_with = input()

    result = replace_all(pattern, s, replace_with)
    # result = replace_all("gogol", "nnnnnngogogol")
    print("".join(result))


if __name__ == "__main__":
    main()
