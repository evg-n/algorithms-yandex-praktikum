def get_longest_palindrome(s):
    middle_element = ""
    n = len(s)
    s = sorted(s)
    result = []

    i = 0
    while i < n - 1:
        if s[i + 1] == s[i]:
            i += 1
            result.append(s[i])
        else:
            if not middle_element:
                middle_element = s[i]
        i += 1

    if i < n and not middle_element:
        middle_element = s[i]

    return "".join(result + [middle_element] + list(reversed(result)))


def main():
    s = input()
    print(get_longest_palindrome(s))


if __name__ == "__main__":
    main()
