def get_card_count_brute_force(n, k, cards) -> int:
    def get_card_rec(l, r, left_moves, curr_sum=0):
        if not left_moves:
            return curr_sum

        return max(
            get_card_rec(l + 1, r, left_moves - 1, curr_sum + cards[l]),
            get_card_rec(l, r - 1, left_moves - 1, curr_sum + cards[r]),
        )

    return get_card_rec(0, len(cards) - 1, k)


def get_card_count_prefix_sum(n, k, cards) -> int:
    prefix_left = [0]
    prefix_right = [0]
    for i in range(k):
        prefix_left.append(prefix_left[-1] + cards[i])
        prefix_right.append(prefix_right[-1] + cards[len(cards) - 1 - i])

    max_sum = 0
    for i in range(k + 1):
        max_sum = max(max_sum, prefix_left[k - i] + prefix_right[i])

    return max_sum


n = int(input())
k = int(input())
cards = list(map(int, input().split()))

print(get_card_count_prefix_sum(n, k, cards))
