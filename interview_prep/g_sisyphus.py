from heapq import heapify, heappop, heappush


def get_energy_for_union(stones):
    min_energy = 0
    heapify(stones)

    while len(stones) > 1:
        bigger_stone = heappop(stones) + heappop(stones)
        min_energy += bigger_stone
        heappush(stones, bigger_stone)

    return min_energy


n = int(input())
stones = list(map(int, input().split()))

print(get_energy_for_union(stones))
