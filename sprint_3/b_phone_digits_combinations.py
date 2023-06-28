DIGITS_TO_LETTERS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def print_possible_letters_combinations(digits, i=0, prefix=[]):
    if i == len(digits):
        print("".join(prefix), end=" ")
        return

    current_letters = DIGITS_TO_LETTERS[digits[i]]
    for letter in current_letters:
        prefix.append(letter)
        print_possible_letters_combinations(digits, i + 1, prefix)
        prefix.pop()


if __name__ == "__main__":
    digits = input()
    print_possible_letters_combinations(digits)
    print()
