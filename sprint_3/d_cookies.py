from typing import List


def get_happy_child_number(cookies: List[int], greedy_coefficients: List[int]) -> int:
    cookies.sort()
    greedy_coefficients.sort()

    happy_children_counter = 0
    for gc in reversed(greedy_coefficients):
        if not cookies:
            break
        if gc <= cookies[-1]:
            cookies.pop()
            happy_children_counter += 1

    return happy_children_counter


def main():
    _ = int(input())
    greedy_coefficients = list(map(int, input().split()))
    _ = int(input())
    cookies = list(map(int, input().split()))
    print(get_happy_child_number(cookies, greedy_coefficients))


if __name__ == "__main__":
    main()
