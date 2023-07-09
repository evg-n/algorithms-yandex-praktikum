from collections import defaultdict
from typing import List


BASE = 1337
MOD = 10**15 + 7


def precalculate_powers(q, n, m):
    pow_storage = [1]
    for _ in range(n - 1):
        pow_storage.append((pow_storage[-1] * q) % m)
    return pow_storage


def find_all_n_k_substrings(s: str, window_size: int, k: int) -> List[int]:
    pow_storage = precalculate_powers(BASE, window_size, MOD)
    cache = defaultdict(int)
    cache_start_indexes = {}

    current_hash = 0
    for i in range(window_size):
        current_hash = (current_hash * BASE + ord(s[i])) % MOD

    cache[current_hash] += 1
    cache_start_indexes[current_hash] = 0

    def get_next_hash(prev_hash, x, y):
        current_hash = (prev_hash - pow_storage[-1] * ord(s[x])) % MOD
        return (current_hash * BASE + ord(s[y])) % MOD

    for i in range(1, len(s) - window_size + 1):
        current_hash = get_next_hash(current_hash, i - 1, i + window_size - 1)
        if current_hash not in cache:
            cache_start_indexes[current_hash] = i

        cache[current_hash] += 1

    return [cache_start_indexes[key] for key, val in cache.items() if val >= k]


def main():
    window_size, k = list(map(int, input().split()))
    s = input()
    results = find_all_n_k_substrings(s, window_size, k)
    print(" ".join(map(str, results)))


if __name__ == "__main__":
    main()
