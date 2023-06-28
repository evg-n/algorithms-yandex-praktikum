def add_to_trie(trie, word):
    abbreviation = list(filter(lambda item: item.isupper(), word))
    if not abbreviation:
        if "terminal" not in trie:
            trie["terminal"] = [word]
        else:
            trie["terminal"].append(word)
        return

    for i, ch in enumerate(abbreviation):
        if ch in trie:
            trie = trie[ch]
        else:
            trie[ch] = {}
            trie = trie[ch]

        # last symbol
        if i == len(abbreviation) - 1:
            if "terminal" not in trie:
                trie["terminal"] = [word]
            else:
                trie["terminal"].append(word)


def find_matches(trie, query):
    results = []

    for i, ch in enumerate(query):
        is_last = i == len(query) - 1
        if ch in trie:
            trie = trie[ch]
        else:
            return []

        if is_last:
            if "terminal" in trie:
                results.extend(trie["terminal"])
            add_suggestions(results, trie)

    if not query:
        if "terminal" in trie:
            results.extend(trie["terminal"])
        add_suggestions(results, trie)

    return sorted(results)


def add_suggestions(results, trie):
    queue = []
    for key in trie:
        if key != "terminal":
            queue.append(trie[key])

    while queue:
        curr_trie = queue.pop()

        for key in curr_trie:
            if key == "terminal":
                results.extend(curr_trie["terminal"])
            else:
                queue.append(curr_trie[key])


def main():
    n = int(input())

    trie = {}
    for _ in range(n):
        word = input()
        add_to_trie(trie, word)

    total_res = []
    m = int(input())
    for _ in range(m):
        query = input()
        current_results = find_matches(trie, query)
        if current_results:
            total_res.append(current_results)

    for items in total_res:
        for item in items:
            print("".join(item))


if __name__ == "__main__":
    main()
