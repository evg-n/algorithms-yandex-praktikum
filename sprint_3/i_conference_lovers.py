from collections import defaultdict
from typing import List


def get_k_max_enrolled_universities(ids: List[int], k: int) -> List[int]:
    stat = defaultdict(int)
    for id in ids:
        stat[id] += 1
    sorted_ids = sorted(stat.items(), key=lambda kv: (-kv[1], kv[0]))
    return [item[0] for item in sorted_ids[:k]]


def main():
    _ = int(input())
    ids = list(map(int, input().split()))
    k = int(input())

    ids = get_k_max_enrolled_universities(ids, k)
    print(" ".join(map(str, ids)))


if __name__ == "__main__":
    main()
