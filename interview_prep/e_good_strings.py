def convert_to_good_string(probably_bad_string: str) -> str:
    if len(probably_bad_string) < 2:
        return probably_bad_string

    result = []

    for s in probably_bad_string:
        if not result or (
            s.lower() != result[-1].lower()
            or (s.lower() == result[-1].lower() and s == result[-1])
        ):
            result.append(s)
        else:
            result.pop()

    return "".join(result)


probably_bad_string = input()
print(convert_to_good_string(probably_bad_string))
