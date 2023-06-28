def memoize(f):
    cache = {}

    def inner(*args):
        args_hash = hash(frozenset(args))
        if args_hash in cache:
            return cache[args_hash]
        result = f(*args)
        cache[args_hash] = result
        return result

    return inner


@memoize
def get_fib(n):
    if n == 0 or n == 1:
        return 1
    return get_fib(n - 1) + get_fib(n - 2)


if __name__ == "__main__":
    n = int(input())
    print(get_fib(n))
