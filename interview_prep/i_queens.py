def apply_color(grid, x, y, color):
    if not grid[x][y]:
        grid[x][y] = color


def clear_color(grid, x, y, color):
    if grid[x][y] == color:
        grid[x][y] = 0


def place_queen(grid, i, j, color, func):
    n = len(grid)

    # one diagonal
    x = y = 0
    if i > j:
        x = i - j
    elif j > i:
        y = j - i
    while x < n and y < n:
        func(grid, x, y, color)
        x += 1
        y += 1

    # second diagonal
    x, y = 0, n - 1
    if i < (n - 1 - j):
        y = j + i
    else:
        x = i - (n - 1 - j)
    while y >= 0 and x < n:
        func(grid, x, y, color)
        y -= 1
        x += 1

    # horizontal
    x, y = i, 0
    while y < n:
        func(grid, x, y, color)
        y += 1

    # vertical
    x, y = 0, j
    while x < n:
        func(grid, x, y, color)
        x += 1


def get_all_peaceful_combinations(n):
    grid = [[0] * n for _ in range(n)]
    results = []

    def place_queen_rec(queens_prefix=None, level=1):
        if not queens_prefix:
            queens_prefix = []

        for i in range(n):
            if not grid[level - 1][i]:
                if level == n:
                    queens_prefix.append(i + 1)
                    results.append(" ".join(map(str, queens_prefix)))
                    queens_prefix.pop()
                else:
                    queens_prefix.append(i + 1)
                    place_queen(grid, level - 1, i, level, apply_color)

                    place_queen_rec(queens_prefix, level + 1)

                    queens_prefix.pop()
                    place_queen(grid, level - 1, i, level, clear_color)

    place_queen_rec()
    return results


# improved current cell check using sets for diagonals/anti-diagonals, rows and columns
def get_all_peaceful_combination_quick_check(n):
    results = []

    def place_queen_rec(
        queens_prefix=None,
        rows=None,
        cols=None,
        diagonals=None,
        anti_diagonals=None,
    ):
        if not queens_prefix:
            queens_prefix = []
        if not rows:
            rows = set()
        if not cols:
            cols = set()
        if not diagonals:
            diagonals = set()
        if not anti_diagonals:
            anti_diagonals = set()

        row = len(rows)

        for col in range(n):
            diagonal = row - col
            anti_diagonal = row + col
            if (
                row not in rows
                and col not in cols
                and diagonal not in diagonals
                and anti_diagonal not in anti_diagonals
            ):
                if row == n - 1:
                    queens_prefix.append(col + 1)
                    results.append(" ".join(map(str, queens_prefix)))
                    queens_prefix.pop()
                else:
                    # fill the used sets
                    queens_prefix.append(col + 1)

                    rows.add(row)
                    cols.add(col)
                    diagonals.add(diagonal)
                    anti_diagonals.add(anti_diagonal)

                    place_queen_rec(
                        queens_prefix, rows, cols, diagonals, anti_diagonals
                    )

                    # backtrack the used sets
                    queens_prefix.pop()

                    rows.remove(row)
                    cols.remove(col)
                    diagonals.remove(diagonal)
                    anti_diagonals.remove(anti_diagonal)

    place_queen_rec()
    return results


def get_all_peaceful_combination_quick_cleaner(n):
    results = []

    def place_queen_rec(row, queens_prefix, cols, diagonals, anti_diagonals):
        for col in range(n):
            diagonal = row - col
            anti_diagonal = row + col
            if (
                col not in cols
                and diagonal not in diagonals
                and anti_diagonal not in anti_diagonals
            ):
                if row == n - 1:
                    queens_prefix.append(col + 1)
                    results.append(" ".join(map(str, queens_prefix)))
                    queens_prefix.pop()
                else:
                    # fill the used sets
                    queens_prefix.append(col + 1)

                    cols.add(col)
                    diagonals.add(diagonal)
                    anti_diagonals.add(anti_diagonal)

                    place_queen_rec(
                        row + 1, queens_prefix, cols, diagonals, anti_diagonals
                    )

                    # backtrack the used sets
                    queens_prefix.pop()

                    cols.remove(col)
                    diagonals.remove(diagonal)
                    anti_diagonals.remove(anti_diagonal)

    place_queen_rec(0, [], set(), set(), set())
    return results


n = int(input())
# combinations = get_all_peaceful_combinations(n)
# combinations = get_all_peaceful_combination_quick_check(n)
combinations = get_all_peaceful_combination_quick_cleaner(n)

print(len(combinations))
for combination in combinations:
    print(combination)
