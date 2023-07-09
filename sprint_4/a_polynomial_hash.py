def calculate_poly_hash(base: int, m: int, s: str) -> int:
    if not s:
        return 0

    result = ord(s[0])

    for i in range(1, len(s)):
        result = (ord(s[i]) + base * result) % m

    return result


def main():
    a = int(input())
    m = int(input())
    s = input()

    print(calculate_poly_hash(a, m, s))


if __name__ == "__main__":
    main()
