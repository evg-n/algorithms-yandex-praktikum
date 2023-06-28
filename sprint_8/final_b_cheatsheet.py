"""
-- ПРИНЦИП РАБОТЫ --
    Используем для решения задачи вспомогательную структуру данных Trie
    (В нашем случае - на основе вложенных хеш-таблиц dict).

    Далее, начиная со стартового индекса 0, получаем из Trie индексы next_indexes
    (каждый индекс - позиция в тексте T после нахождения соответствующего
    префикса из допустимых к использованию слов).

    Добавляем их в очередь проверок, постепенно обрабатывая ее и перемещаясь к 
    концу строки T.

    Используем множество visited_indexes чтобы избежать повторных проверок.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(max(T * T, N * M), где

        (N * M) - затраты на построение Trie. Где M - длина самого длинного
        слова из N допустимых к использованию слов.

        (T * T) - поиск и обработка вариантов разбиений строки T. 

        Худший случай - когда каждому символу строки T соответствует конец одного
        из допустимых слов на каждом этапе сравнения.
        Например:
        Текст T: АААААА
        Допустимые слова:
        А
        АА
        ААА
        АААА
        ААААА

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(N * M) - хранение Trie.
"""

from typing import Dict


def is_decompressible(s: str, trie: Dict):
    queue = [0]
    visited_indexes = set()

    while queue:
        current_start = queue.pop()
        next_indexes = get_next_indexes(s, current_start, trie)

        for next_index in next_indexes:
            if next_index == len(s):
                return True
            elif next_index not in visited_indexes:
                visited_indexes.add(next_index)
                queue.append(next_index)

    return False


def get_next_indexes(s: str, start: int, trie: Dict):
    results = []

    i = start
    while i < len(s) and s[i] in trie:
        trie = trie[s[i]]
        if "is_terminal" in trie:
            results.append(i + 1)
        i += 1

    return results


def add_to_trie(word: str, trie: Dict):
    for i, ch in enumerate(word):
        if ch not in trie:
            trie[ch] = {}
        trie = trie[ch]

        is_last = i == len(word) - 1
        if is_last:
            trie["is_terminal"] = True


def main():
    compressed_string = input()

    n = int(input())
    trie = {}
    for _ in range(n):
        add_to_trie(input(), trie)

    print("YES" if is_decompressible(compressed_string, trie) else "NO")


if __name__ == "__main__":
    main()
