def get_max_substring_len(s):
    if not s:
        return 0

    # value to index
    stat = {}

    lo, res = 0, 0

    for i, ch in enumerate(s):
        if ch in stat:
            lo = max(lo, stat[ch])

        res = max(res, i - lo + 1)
        stat[ch] = i + 1

    return res


if __name__ == "__main__":
    s = input()
    print(get_max_substring_len(s))
