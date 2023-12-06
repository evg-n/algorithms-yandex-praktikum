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
