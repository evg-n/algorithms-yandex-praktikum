def is_on_the_same_line(points):
    points = list(points)
    if len(points) < 2:
        return True

    ax, ay = points[0]
    bx, by = points[1]

    for i in range(2, len(points)):
        cur_x, cur_y = points[i]
        if (by - ay) * (cur_x - bx) != (bx - ax) * (cur_y - by):
            return False

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
