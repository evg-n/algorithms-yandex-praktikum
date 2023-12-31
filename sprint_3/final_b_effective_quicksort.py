"""
-- ПРИНЦИП РАБОТЫ --
    Алгоритм опирается на принцип: разделяй и властвуй.
    
    Проблема на каждом шаге разделяется на две (в идеале равные, чтобы дерево
    вызовов не превосходило по глубине logN) до тех пор пока не выполняется
    условие базового случая (сортируемый участок не содержит элементов или
    содержит всего один элемент, сортировать нечего).

    Партицирование. 
    1. Выбор опорного элемента. Этот этап можно сильно корректировать,
    повышая вероятность того, что выбранный элемент окажется не в крайних 
    позициях текущей сортируемой подпоследовательности после выполнения функции. 
    Наша задача - свести вероятность худшего случая O(N*N) к минимуму.
    Подходы разные, всегда стоит обратить на исходные данные, если есть такая
    информация (количество дублей, наличие упорядоченных подпоследовательностей
    и их размер). Если порядок неизвестен, можно взять медиану из 3 или 9 элементов.
    (https://en.wikipedia.org/wiki/Quicksort#Choice_of_pivot)

    2. Перестановка элементов в соответствии с инвариантом.
    На этом мы должны разделить данные на три подмножества:
        - элементы, меньшие опорному элементу,
        - элементы, равные опорному элементу,
        - элементы, большие опорного элемента.
    Известных вариантов реализации несколько, они отличаются способом работы
    с дубликатами, и количеством совершаемых обменов (swaps).
    В нашем варианте мы используем два указателя (с левой и правой границ
    рассматриваемой подпоследовательности), последовательно сдвигая их друг
    к другу, и совершая обмены элементов, нарушающих требуемый порядок сортировки.
    Цикл выполняется до тех пор, пока они не пересекутся. Таким образом,
    мы не используем дополнительной памяти кроме хранения фиксированного набора
    вспомогательных индексов и других переменных, стека вызовов.


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
    В ходе работы алгоритм разделяет разделяет исходную проблему на две
    меньшего размера. Также на каждом шаге рекурсии определяется финальная
    позиция опорного (pivot) элемента. Базовый случай - это пустой массив или
    массив из одного элмента, они считаются отсортированными.

    Основная работа заключается в том как мы выполняем partition - разделение 
    данных. После его завершения должно выполняться условие - все элементы, 
    меньшие или равные опорного, должны находиться слева от него, и все бОльшие
    элементы - справа. Функция возвращает получившийся индекс опорного элемента,
    это и будет его окончательной позицией в отсортированной последовательности.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    В среднем случае - O(N*logN):
        - Глубина стека рекурсии log(N)
        - Каждый вызов рекурсии, кроме базового случая вызывает функцию partition O(N)
    В худшем случае - O(N*N):
        - Глубина стека рекурсии увеличивается из-за неудачного выбора Pivot
        элемента. За счет этого каждый рекурсивный вызов будет уменьшать исходную
        проблему только на 1 элемент. Стек вызовов - цепочка из (n - 1) вызовов
        partition, то есть квадратичная сложнось. 

    В нашем случае, выбор медианы из трех элементов позволяет нивелировать такой
    негативный сценарий, т.к. мы знаем особенности входных данных - они уникальны.
    
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Величина затрат памяти зависит от глубины стека вызовов нашей рекурсии.
        - В среднем случае - O(logN)
        - В худше случае - O(N)

    Алгоритм считывает N элементов (тратит на их хранение O(N)), сортировка 
    выполняется "на месте", не создавая временных списков или других структур 
    данных. Из дополнительных затрат по памяти можно отметить хранение стека 
    вызова рекурсии logN, в каждом из которых создается константное число 
    вспомогательных переменных.
"""
from typing import Tuple


StudentResult = Tuple[int, int, str]


# Reorder three elements (left, middle, right) and return the median index
def get_median_index(a, lo, hi, key):
    mid = (lo + hi) // 2

    if key(a[mid]) < key(a[lo]):
        a[lo], a[mid] = a[mid], a[lo]
    if key(a[hi]) < key(a[lo]):
        a[lo], a[hi] = a[hi], a[lo]
    if key(a[mid]) > key(a[hi]):
        a[hi], a[mid] = a[mid], a[hi]
    return mid


# Partition scheme https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
def partition(arr, left, right, key):
    mi = get_median_index(arr, left, right, key)
    median = arr[mi]

    i, j = left, right
    while True:
        while key(arr[i]) < key(median):
            i += 1
        while key(arr[j]) > key(median):
            j -= 1

        if i >= j:
            return j
        arr[j], arr[i] = arr[i], arr[j]


def quicksort(arr, left, right, key):
    if left >= right:
        return arr

    pi = partition(arr, left, right, key)
    quicksort(arr, left, pi - 1, key)
    quicksort(arr, pi + 1, right, key)


def read_contest_members():
    n = int(input())
    data = []
    for _ in range(n):
        name, score, penalty = input().split()
        data.append((name, int(score), int(penalty)))
    return data


def custom_key(item: StudentResult):
    return -item[1], item[2], item[0]


def main():
    contest_results = read_contest_members()
    quicksort(contest_results, 0, len(contest_results) - 1, key=custom_key)
    for result in contest_results:
        print(result[0])


if __name__ == "__main__":
    main()
