"""
-- ПРИНЦИП РАБОТЫ --
    Используем принцип динамического программирования, храня в множестве dp уже
    вычисленные промежуточные суммы.
    
    Для решения задачи важно заметить, что нам нужно доказать, существует
    ли множество элементов в исходном массиве, чья сумма будет равна половине
    общей суммы всех элементов. При этом если сумма - нечетная, можно сразу
    вернуть False.

    1. Заполним множество dp исходными элементами.
    2. Для каждого из элементов последовательности:
        - обходим каждый элемент dp и добавляем к нему рассматриваемый элемент
        последовательности. 
            - Можем сразу выйти, если искомая полусумма найдена.
            - Если полученная сумма больше искомой, ее можно не добавлять в dp,
            таким образом оптимизируя расход памяти.
    3. Если искомая полусумма не обнаружена, в конце работы алгоритма просто
    возвращаем false.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(m * n), где m - половина суммы n элементов
    
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(m * n), где m - половина суммы n элементов
"""


def can_partition_into_two_equal_sums(a):
    total = sum(a)
    if total % 2:
        return False
    half_sum = total // 2

    dp = set(a)

    for item in a:
        new_set = set(a)
        for set_item in dp:
            new_sum = set_item + item
            if new_sum == half_sum:
                return True
            elif new_sum < half_sum:
                new_set.add(set_item + item)
        dp = new_set

    return False


def main():
    _ = input()
    a = list(map(int, input().split()))
    print(can_partition_into_two_equal_sums(a))


if __name__ == "__main__":
    main()
