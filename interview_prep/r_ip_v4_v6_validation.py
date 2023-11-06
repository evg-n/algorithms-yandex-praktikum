def is_ipv6_item_valid(s):
    n = len(s)
    if not n or n > 4:
        return False

    return all(i.isnumeric() or i in "abcdefABCDEF" for i in s)


def is_ipv4_item_valid(s):
    n = len(s)
    if not n or n > 3:
        return False

    if n == 1:
        return s[0].isnumeric()
    elif n == 2:
        return s[0] != "0" and s[0].isnumeric() and s[1].isnumeric()
    else:
        return (
            s[0] != "0"
            and s[1] != "0"
            and all(i.isnumeric() for i in s)
            and int(s) < 256
        )


def ip_check(s):
    if "." in s:
        ipv4 = s.split(".")
        print(
            "IPv4"
            if len(ipv4) == 4 and all(is_ipv4_item_valid(i) for i in ipv4)
            else "Error"
        )
    elif ":" in s:
        ipv6 = s.split(":")
        print(
            "IPv6"
            if len(ipv6) == 8 and all(is_ipv6_item_valid(i) for i in ipv6)
            else "Error"
        )
    else:
        print("Error")


def main():
    s = input()
    ip_check(s)


if __name__ == "__main__":
    main()
