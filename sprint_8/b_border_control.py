def can_pass(target, source):
    if abs(len(target) - len(source)) > 1:
        return False

    once_failed = False
    i = j = 0
    while i < len(target):
        if target[i] != source[j]:
            if once_failed:
                return False

            # try replace
            if len(target) == len(source):
                i += 1
                j += 1
            # try delete from target
            elif len(target) == len(source) + 1:
                i += 1
            # try insert to target
            else:
                j += 1
            once_failed = True
        else:
            i += 1
            j += 1

    return True


def main():
    passport_name = input()
    db_name = input()

    print("OK" if can_pass(passport_name, db_name) else "FAIL")


if __name__ == "__main__":
    main()
