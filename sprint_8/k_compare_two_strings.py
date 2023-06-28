def is_even_position(l):
    return (ord(l) - ord("a") + 1) % 2 == 0


def main():
    s1 = input()
    s2 = input()

    s1_filtered = "".join(filter(is_even_position, s1))
    s2_filtered = "".join(filter(is_even_position, s2))

    if s1_filtered == s2_filtered:
        print(0)
    elif s1_filtered < s2_filtered:
        print(-1)
    else:
        print(1)


if __name__ == "__main__":
    main()
