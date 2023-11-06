def get_brackets_sequences(n):
    if n == 0 or n % 2:
        return []

    results = []

    def get_seq(seq, stack):
        if len(seq) == n:
            if not stack:
                results.append("".join(seq[:]))
            return

        if "[" not in stack:
            seq.append("(")
            get_seq(seq, stack[:] + ["("])
            seq.pop()

        seq.append("[")
        get_seq(seq, stack[:] + ["["])
        seq.pop()

        if not stack:
            return

        if stack[-1] == "(":
            seq.append(")")
            get_seq(seq, stack[:-1])
            seq.pop()
        elif stack[-1] == "[":
            seq.append("]")
            get_seq(seq, stack[:-1])
            seq.pop()

    get_seq([], [])
    return results


def main():
    n = int(input())
    sequences = get_brackets_sequences(n)
    for seq in sequences:
        print(seq)


if __name__ == "__main__":
    main()
