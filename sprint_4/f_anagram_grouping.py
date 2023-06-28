def get_anagram_groups(s):
    # len to list of indexes
    groups = {}

    for i, word in enumerate(s):
        l = len(word)
        sorted_word = "".join(sorted(word))
        if l in groups:
            if sorted_word in groups[l]:
                groups[l][sorted_word].append(i)
            else:
                groups[l][sorted_word] = [i]
        else:
            groups[l] = {sorted_word: [i]}

    return groups


def print_groups(index_groups):
    # sort inside and concatenate groups
    results = []
    for groups_by_len in index_groups.values():
        for group in groups_by_len.values():
            results.append(group)

    return sorted(results, key=lambda item: item[0])


if __name__ == "__main__":
    _ = int(input())
    s = list(input().split())
    results = print_groups(get_anagram_groups(s))

    for result in results:
        print(" ".join(map(str, result)))
