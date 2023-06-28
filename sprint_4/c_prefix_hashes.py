def precalculate_prefix_hashes(a, m, s):
    if not s:
        return {}

    stat = [ord(s[0])]
    for i in range(1, len(s)):
        new_sum = ((stat[-1] * a) + ord(s[i])) % m
        stat.append(new_sum)
    return stat


def calculate_hash(l, r, stat, a, m, powers):
    if l == 0:
        return stat[r] % m

    return (stat[r] - (stat[l - 1]) * (powers[r - l + 1] % m)) % m


def precalculate_powers(a, n, m):
    pow_storage = [1]

    for _ in range(n - 1):
        pow_storage.append((pow_storage[-1] * a) % m)
    return pow_storage


if __name__ == "__main__":
    a = int(input())
    m = int(input())

    s = input()
    hashes = precalculate_prefix_hashes(a, m, s)
    powers = precalculate_powers(a, len(s), m)

    t = int(input())
    for _ in range(t):
        l, r = list(map(int, input().split()))
        print(calculate_hash(l - 1, r - 1, hashes, a, m, powers))
