from collections import defaultdict
from typing import Tuple
from functools import lru_cache

NEAR_LIMIT = 20
NEAR_LIMIT_SQUARED = NEAR_LIMIT**2

COORDINATES = Tuple[int, int]


def get_distance(a: COORDINATES, b: COORDINATES) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def get_area_hash(point: COORDINATES):
    return (point[0] - point[0] % NEAR_LIMIT, point[1] - point[1] % NEAR_LIMIT)


def get_neighbors(metro: COORDINATES, bus_stations_areas):
    x, y = get_area_hash(metro)
    adjacent_areas = {
        "TOP_LEFT": (x - NEAR_LIMIT, y + NEAR_LIMIT),
        "TOP_CENTER": (x, y + NEAR_LIMIT),
        "TOP_RIGHT": (x + NEAR_LIMIT, y + NEAR_LIMIT),
        "CENTER_LEFT": (x - NEAR_LIMIT, y),
        "CENTER_CENTER": (x, y),
        "CENTER_RIGHT": (x + NEAR_LIMIT, y),
        "BOTTOM_LEFT": (x - NEAR_LIMIT, y - NEAR_LIMIT),
        "BOTTOM_CENTER": (x, y - NEAR_LIMIT),
        "BOTTOM_RIGHT": (x + NEAR_LIMIT, y - NEAR_LIMIT),
    }

    neighbors = []
    for area in adjacent_areas.values():
        neighbors.extend(bus_stations_areas[area])
    return neighbors


@lru_cache(maxsize=None)
def is_near(a, b):
    ax, ay = a
    bx, by = b

    if abs(ax - bx) + abs(ay - by) >= (14 + 15):
        return False

    if not -20 <= ax - bx <= 20 or not -20 <= ay - by <= 20:
        return False

    return get_distance(a, b) <= NEAR_LIMIT_SQUARED


def get_metro_exit_with_most_bus_stations(metro_exits, bus_stations_areas):
    target_metro_exit_index = -1
    target_metro_exit_stations_count = -1
    for i, metro in enumerate(metro_exits, start=1):
        neighbors = get_neighbors(metro, bus_stations_areas)

        if len(neighbors) <= target_metro_exit_stations_count:
            continue

        neighbors_count = 0
        for neighbor in neighbors:
            if is_near(metro, neighbor):
                neighbors_count += 1

        if neighbors_count > target_metro_exit_stations_count:
            target_metro_exit_index = i
            target_metro_exit_stations_count = neighbors_count

    return target_metro_exit_index


def main():
    n = int(input())
    metro_exits = []
    for _ in range(n):
        metro_exits.append(tuple(map(int, input().split())))

    m = int(input())
    bus_stations_areas = defaultdict(list)
    for _ in range(m):
        station_point = tuple(map(int, input().split()))
        bus_stations_areas[get_area_hash(station_point)].append(station_point)

    print(
        get_metro_exit_with_most_bus_stations(metro_exits, bus_stations_areas)
    )


if __name__ == "__main__":
    main()
