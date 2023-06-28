"""
-- ПРИНЦИП РАБОТЫ --
    Алгоритм состоит из трех этапов.
    1. Поиск элемента, нарушающего сортировку по неубыванию. Этот элемент
    будет являться максимальным в нашем массиве и его индекс позволяет
    определить границы двух интервалов, из которых состоит наш исходный 
    "сломанный" массив. Каждый из этих двух интервалов отсортирован.

    2. Проверка, входит ли значение элемента, который мы хотим найти, в границы
    имеющихся двух отсортированных интервалов. Если нет, возвращаем -1. Иначе,
    переходим к шагу 3.

    3. Бинарный поиск элемента в одном из двух подмассивов, границы которых мы
    нашли на шаге 1.


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
    Искомая последовательность должна содержать элемент, после которого следует
    элемент с меньшим значением. Мы можем найти такой элемент не более чем за
    logN сравнений, опираясь на значение первого или последнего элемента
    последовательности. На каждом этапе этого поиска мы сокращаем интервал для
    поиска в два раза, до тех пор пока мы не нашли искомый элемент.

    Зная индекс этого элемента, мы можем сказать что это максимальный элемент.
    А следующий за ним - минимальный. Таким образом, мы имеем границы двух 
    интервалов, внутри которых может находиться искомый элемент. Также, мы
    можем сразу вернуть -1, если его значение не находится внутри одного из 
    найденных интервалов.

    Далее, выполняется классический бинарный поиск в одном из двух интервалов,
    на каждом этапе цикла рассматриваемый интервал сокращается в два раза.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    для N операций поиска - O(N*logN)
    Каждый поиск состоит из двух операций:
        - Бинарный поиск элемента, где сортировка нарушается - O(logN)
        - Обычный бинарный поиск элемента в одной из двух отсортированных
        подпоследовательностей исходного массива O(logN).
    
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(1)    
    Алгоритм считывает N элементов (тратит на их хранение O(N)). Операция поиска
    не требует дополнительных затрат памяти, кроме как на хранение постоянного
    числа вспомогательных временных переменных.
"""


# Find the index of the element after which non-increasing sorting order breaks
def find_max_element_index(nums) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        middle_index = (left + right) // 2
        middle_element = nums[middle_index]

        if middle_element > nums[middle_index + 1]:
            return middle_index
        elif middle_element < nums[-1]:
            right = middle_index - 1
        else:
            left = middle_index + 1


def binary_search(nums, left, right, target) -> int:
    while left <= right:
        middle_index = (left + right) // 2
        middle_element = nums[middle_index]

        if middle_element == target:
            return middle_index
        elif middle_element < target:
            left = middle_index + 1
        else:
            right = middle_index - 1
    return -1


def broken_search(nums, target) -> int:
    # Case when the length is 1 or nums are already sorted
    if nums[-1] >= nums[0]:
        return binary_search(nums, 0, len(nums) - 1, target)

    max_el_index = find_max_element_index(nums)

    # Search in range [nums[0], max_element]
    if nums[0] <= target <= nums[max_el_index]:
        return binary_search(nums, 0, max_el_index, target)
    # Search in range [min_element, nums[-1]]
    elif nums[max_el_index + 1] <= target <= nums[-1]:
        return binary_search(nums, max_el_index + 1, len(nums) - 1, target)

    # Target value is out of range
    return -1


def main():
    _ = int(input())
    k = int(input())
    broken_array = list(map(int, input().split()))

    print(broken_search(broken_array, k))


if __name__ == "__main__":
    main()
