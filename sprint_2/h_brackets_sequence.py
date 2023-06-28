def is_correct_bracket_seq(seq):
    BRACKETS_MAP = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    if not seq:
        return True

    stack = []
    for s in seq:
        if s in BRACKETS_MAP:
            stack.append(s)
        else:
            if not stack:
                return False
            top_bracket = stack.pop()
            if BRACKETS_MAP[top_bracket] != s:
                return False
    return not stack


def main():
    s = input()
    print(is_correct_bracket_seq(s))


if __name__ == "__main__":
    main()
