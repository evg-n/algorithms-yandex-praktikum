def are_strangely_equal(s, t):
    if len(s) != len(t):
        return False
    mem = {}
    used = set()
    for i in range(min(len(s), len(t))):
        if s[i] in mem:
            expected_t = mem[s[i]]
            if t[i] != expected_t:
                return False
        elif t[i] in used:
            return False
        else:
            mem[s[i]] = t[i]
            used.add(t[i])
    return True


if __name__ == "__main__":
    s = input()
    t = input()
    print("YES" if are_strangely_equal(s, t) else "NO")
