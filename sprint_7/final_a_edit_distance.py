"""
-- ПРИНЦИП РАБОТЫ --
    Обозначим за N - длину строки s, и K - длину строки t.
    Используем принцип динамического программирования, храня в dp на каждом шаге
    промежуточные результаты - расстояние по Левенштейну (далее - РпЛ) для соответствующих
    префиксов строк s[0:i] и t[0:j].
    
    Базовый случай динамики:
    Если какая-то из строк пустая, РпЛ между двумя
    строками равен длине непустой строки. Для i=0, j=0: dp[j] = 0.

    Переход динамиики:
    - s[i] == t[j], текущие рассматриваемые символы равны. В этом случае мы
    просто берем уже вычисленное значение для префиксов s[i-1] и t[j-1].
    Ничего менять не нужно, на этом шаге РпЛ не меняется.
    - s[i] != t[j]. Берем минимальное из следующих уже рассчитанных значений РпЛ:
        - Добавляем t[j] символ в префикс s[i]: dp = temp[j - 1] + 1
        - Удаляем t[j] символ из префикса s[i]: dp = dp[j] + 1
        - Заменяем s[i] символ на t[j] символ: dp = dp[j - 1] + 1

    * Намного нагляднее с точки зрения объяснения выглядит решение с использованием
    N * K памяти и двумерного массива. В нашем случае используется немного
    оптимизированная его версия, т.к. можно заметить, что не все промежуточные
    значения нужны в ходе работы алгоритма.
        
    Порядок вычисления данных в массиве: 
    Можно идти по мере увеличению префикса любой из строк. В нашем случае, мы
    сначала считаем, что строка s состоит из одного символа, а строка t постепенно
    удлиняется. Потом удлиняем строку s и снова перебираем все возможные длины t.

    Где будет располагаться ответ на исходный вопрос?
    В последней ячейке dp[K].

    Идеи для решения - https://leetcode.com/problems/edit-distance/

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(N * K)
    Алгоритм проходит по всем комбинациям префиксов двух подстрок: N * K.
    
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(K)
    Храним только предыдущий и текущий массив для промежуточных результатов.
"""


def get_max_edit_distance(s, t):
    n = len(s)
    k = len(t)
    dp = list(range(k + 1))

    for i in range(1, n + 1):
        temp = [None] * (k + 1)
        temp[0] = i
        for j in range(1, k + 1):
            if s[i - 1] == t[j - 1]:
                temp[j] = dp[j - 1]
            else:
                temp[j] = min(temp[j - 1], dp[j - 1], dp[j]) + 1
        dp = temp

    return dp[k]


def main():
    s = input()
    t = input()
    print(get_max_edit_distance(s, t))


if __name__ == "__main__":
    main()