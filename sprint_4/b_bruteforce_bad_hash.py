from string import ascii_lowercase
from random import choices
from functools import partial
from itertools import product


def calculate_poly_hash(a, m, s):
    if not s:
        return 0

    result = ord(s[0])

    for i in range(1, len(s)):
        result = (ord(s[i]) + a * result) % m

    return result


calculate_partial = partial(calculate_poly_hash, a=1000, m=123987123)


def random_string(len):
    return "".join(choices(ascii_lowercase, k=len))


def next_string():
    i = 2
    while i < 1000:
        for next_string in product(ascii_lowercase, repeat=i):
            yield "".join(next_string)
        i += 1


def brute_force_strings(len=10):
    hash_stat = {}
    string_getter = next_string()
    i = 0
    while True:
        i += 1
        new_generated_string = next(string_getter)
        new_hash = calculate_partial(s=new_generated_string)
        if new_hash in hash_stat:
            return (new_generated_string, hash_stat[new_hash])
        i %= 1000000
        if i == 0:
            print(
                "current len ... ", " last generated string is: ", new_generated_string
            )


s1 = random_string(20)
s1_hash = calculate_partial(s=s1)


def get_same_hash(target_hash, n):
    hash_stat = {}

    while True:
        new_string = random_string(n)
        new_hash = calculate_partial(s=new_string)
        if new_hash in hash_stat:
            return (new_string, hash_stat[new_hash], new_hash)
        else:
            hash_stat[new_hash] = new_string


print(get_same_hash(s1_hash, 20))
