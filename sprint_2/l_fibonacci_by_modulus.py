def get_fib_last_digits(n, k):
    target_limiter = 10**k
    a, b, is_more_than_k = 1, 1, False
    while n > 1:
        b, a = b + a, b
        if b >= target_limiter:
            is_more_than_k = True
        b = b % target_limiter
        n -= 1

    return b, is_more_than_k


def main():
    n, k = list(map(int, (input().split())))
    result, is_more_than_k = get_fib_last_digits(n, k)
    result_digits = len(str(result))
    if result_digits < k and is_more_than_k:
        print(f"{'0' * (k - result_digits)}{result}")
    else:
        print(result)


if __name__ == "__main__":
    main()
