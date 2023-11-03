# import fractions


def is_on_the_same_line(points):
    points = list(points)
    if len(points) < 2:
        return True

    ax, ay = points[0]
    bx, by = points[1]

    i = 1
    if ax == bx:
        while i < len(points):
            if ax != points[i][0]:
                return False
            i += 1
        return True

    k = (ay - by) / (ax - bx)
    b = ay - k * ax

    # i += 1
    while i < len(points):
        cur_x, cur_y = points[i]
        if cur_y != cur_x * k + b and abs(cur_y - cur_x * k + b) > 0.01:
            return False
        i += 1

    return True


def main():
    n = int(input())
    points = {}
    for _ in range(n):
        coords = tuple(map(int, input().split()))
        points[coords] = True
    print("YES" if is_on_the_same_line(points) else "NO")


if __name__ == "__main__":
    main()
