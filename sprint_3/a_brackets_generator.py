def generate_brackets_sequence(n, opened=0, closed=0, prefix=""):
    if n == 0:
        if opened == closed:
            print(prefix)
        return

    if closed > opened:
        return

    generate_brackets_sequence(n - 1, opened + 1, closed, prefix + "(")
    generate_brackets_sequence(n - 1, opened, closed + 1, prefix + ")")


if __name__ == "__main__":
    n = int(input())
    if n > 0:
        generate_brackets_sequence(2 * n)
