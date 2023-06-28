def calculate_poly_hash(a, m, s):
    if not s:
        return 0

    result = ord(s[0])

    for i in range(1, len(s)):
        result = (ord(s[i]) + a * result) % m

    return result


if __name__ == "__main__":
    a = int(input())
    m = int(input())
    s = input()

    print(calculate_poly_hash(a, m, s))
