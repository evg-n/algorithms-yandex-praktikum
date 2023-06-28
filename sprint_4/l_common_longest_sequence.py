from collections import defaultdict


def get_common_len(a, b, a_start, b_start):
    result = 0
    while a_start < len(a) and b_start < len(b) and a[a_start] == b[b_start]:
        a_start += 1
        b_start += 1
        result += 1
    return result


def get_longest_common_sequence(a, b):
    a_hash = defaultdict(list)
    i = 0
    while i < len(a):
        a_val = a[i]
        a_hash[a_val].append(i)
        while i < len(a) - 1 and a[i + 1] == a_val:
            i += 1
        i += 1
    result = 0
    i = 0

    while i < len(b):
        b_val = b[i]

        if b_val in a_hash:
            possible_starts = a_hash[b_val]
            for start in possible_starts:
                cur_len = get_common_len(a, b, a_start=start, b_start=i)
                result = max(result, cur_len)

                if result >= (len(b) - i):
                    return result
            while i < len(b) - 1 and b[i + 1] == b_val:
                i += 1

        i += 1
    return result


# b_1 = [3, 2, 1, 5, 6, 100, 9, 9, 9, 9, 9, 9, 9]
# a_1 = [9, 9, 9, 3, 2, 1, 5, 6, 101, 9, 9, 9, 9, 9, 9, 9]
# print(get_longest_common_sequence(a_1, b_1))

if __name__ == "__main__":
    n = int(input())
    n_scores = list(map(int, input().split()))
    m = int(input())
    m_scores = list(map(int, input().split()))

    print(get_longest_common_sequence(n_scores, m_scores))
