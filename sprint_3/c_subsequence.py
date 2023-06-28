def find_ch(ch, left, right, s):
    for i in range(left, min(right, len(s))):
        if ch == s[i]:
            return i
    return -1


def is_subsequence(s, t):
    if len(t) < len(s):
        return False

    left, right = 0, len(t) - len(s) + 1
    for i in range(len(s)):
        ch = s[i]
        result = find_ch(ch, left, right, t)
        if result == -1:
            return False

        left, right = result + 1, right + 1
    return True


def is_subseq_faster(s, t):
    if len(s) > len(t):
        return False
    it = iter(t)
    return all(any(ch_t == ch_s for ch_t in it) for ch_s in s)


def is_subseq_faster_2(s, t):
    if not s:
        return True

    if len(s) > len(t):
        return False

    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


if __name__ == "__main__":
    s = input()
    t = input()
    print(is_subseq_faster(s, t))
