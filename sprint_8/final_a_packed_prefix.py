"""
-- ПРИНЦИП РАБОТЫ --
    Алгоритм состоит из двух шагов:
    1. "Разворачивание" закодированной строки. Посимвольно обходим
    закодированную строку, используя вспомогательный стек.

        - Если стек пуст и текущий символ - не число или скобка, записываем
        его сразу в ответ.
        - Если встретили число, сохраняем его в стеке множителей - "multiply".
        - Если встретили открывающуюся скобку, начинаем сохранять новую подстроку
        на вершине вспомогательного стека "stack".
        - Если встретили закрывающуюся скобку:
            * достаем из стеков множителей и основного стека значения с их вершин,
            выполняем копирование подстроки нужное число раз,
            * записываем получившуюся строку к крайней подстроке стека, если
            он не пустой, либо сразу к конечному результату.

    2. Последовательное сравнение подстрок развернутых запросов между собой,
        для нахождения максимального общего префикса.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(N * M), где
        N - количество строк-запросов,
        M - длина самой длинной строки.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(M), где M - длина самой длинной строки.
"""
from typing import List


def unwrap(query: str) -> List[str]:
    result = []
    multiply = []
    stack = []
    for ch in query:
        if ch.isnumeric():
            multiply.append(int(ch))
        elif ch == "[":
            # saving new substring on top of the stack
            stack.append([])
        elif ch == "]":
            multiplied_last_word = stack.pop() * multiply.pop()
            if stack:
                # extending previous stack value
                stack[-1].extend(multiplied_last_word)
            else:
                # extending end result
                result.extend(multiplied_last_word)

        elif not stack:
            # non-numeric character with empty stack -> safely added to result
            result.append(ch)
        else:
            # non-numeric character
            stack[-1].append(ch)

    return result


def get_common_prefix(prefix: str, query: str, limit: int) -> str:
    i = 0
    while i < limit and i < len(query) and prefix[i] == query[i]:
        i += 1
    return prefix[:i]


def main():
    n = int(input())

    prefix = unwrap(input())
    max_prefix_len = len(prefix)
    for _ in range(n - 1):
        prefix = get_common_prefix(
            prefix, unwrap(input()), limit=max_prefix_len
        )
        max_prefix_len = min(max_prefix_len, len(prefix))

    print("".join(prefix))


if __name__ == "__main__":
    main()
