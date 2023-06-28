"""
-- ПРИНЦИП РАБОТЫ --
    В основе пирамидальной сортировки лежит структура данных - куча.
    Это бинарное дерево, записанное в массив и отвечающее следующим требованиям:
    * для нашего случая рассмотрим max_heap, т.к. в задаче требуется вывести
    элементы по убыванию результатов в соревновании.
    
    - Ключ в любой вершине больше, чем значения ее потомков,
    - На i-том слое 2^i вершин, кроме последнего (свойство "почти полнота"),
    - Все слои, кроме последнего, уже полностью заполнены.

    Для соблюдения этих свойств, необходимо правильно реализовать вставку 
    и удаление элементов.

    - Вставка O(n*logn): sift_up.
    Вставка осуществляется путем добавления элемента в конец кучи. Затем
    значение элемента сравнивается со значением родительского элемента,
    выполняются обмены, если условие упорядоченности нарушено (в нашем случае,
    если родитель меньше вставляемого элемента). Данное сравнение выполняется
    рекурсивно до тех пор, пока условие не перестает нарушаться, либо мы дошли
    до корневого элемента (индекс - 1).
    - Удаление. O(n*logn): sift_down.
    Корневой (самый приоритетный, возвращаемый результат) элемент
    меняется местами с последним в куче. затем мы должны путем рекурсивного 
    сравнения значений текущего элемента со значениями левого и правого
    потомков, определить финальное положение текущего элемента.

    Сортировка с использованием такой структуры данных становится тривиальной -
    мы просто последовательно извлекаем самые приоритетные элементы из кучи
    (sift_down).

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(n*logn) величина складывается из:
    - Построение кучи из n элементов (n операций вставок - _sift_up): O(n*logn) в худшем/среднем случаях
    - Извлечение n элементов из кучи (n операций  - _sift_down): O(n*logn) в худшем/среднем случаях

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(n) - Все слои, кроме последнего, заполнены полностью, в них вообще нет дыр.
"""
from typing import Callable, Tuple


StudentResult = Tuple[int, int, str]


class CustomHeap:
    heap = [-1]
    size = 0
    _key = None

    def __init__(self, key: Callable = None):
        if key:
            self._key = key

    def heappush(self, x):
        self.heap.append(x)
        self.size += 1
        self._sift_up(self.size)

    def heappop(self):
        result = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self._sift_down(1)
        return result

    def _sift_up(self, idx: int) -> int:
        if idx == 1:
            return 1
        parent_idx = idx // 2
        if self._less(parent_idx, idx):
            self._swap(idx, parent_idx)
            return self._sift_up(parent_idx)
        return idx

    def _swap(self, idx1: int, idx2: int):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def _less(self, left: int, right: int) -> bool:
        return custom_key(self.heap[left]) > custom_key(self.heap[right])

    def _sift_down(self, idx: int) -> int:
        left_idx = idx * 2
        right_idx = idx * 2 + 1

        if left_idx > self.size:
            return idx

        largest_idx = (
            right_idx
            if right_idx <= self.size and self._less(left_idx, right_idx)
            else left_idx
        )

        if self._less(idx, largest_idx):
            self._swap(largest_idx, idx)
            return self._sift_down(largest_idx)
        return idx


def custom_key(item: StudentResult):
    return -item[1], item[2], item[0]


def main():
    n = int(input())
    heap = CustomHeap(key=custom_key)
    for _ in range(n):
        name, score, penalty = input().split()
        heap.heappush((name, int(score), int(penalty)))

    for _ in range(n):
        result = heap.heappop()
        print(result[0])


if __name__ == "__main__":
    main()
