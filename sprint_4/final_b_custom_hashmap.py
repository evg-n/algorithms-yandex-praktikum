"""
Id успешной попытки - 82803833

-- ПРИНЦИП РАБОТЫ --
    На этапе инициализации экземпляра класса хеш-таблицы выделяется большой
    объем памяти, в котором будут хранится пары ключ-значение. Данные хранятся 
    в структуре данных namedtuple для наглядности, простоты получения ключа и
    значения.

    В ходе обработки обращений к таблице, главная сложность - найти индекс
    корзины, куда следует вставить новый элемент/заменить существующий, либо
    удалить или вернуть искомый.
    Все функции интерфейса класса опираются на внутренний метод __find_key,
    который в цикле с нужным шагом пробирования просматривает очередной элемент,
    выясняя - является ли он пустым (поиск закончен, ключ не найден), либо
    ключ очередного проверяемого элемента совпадает с тем, что мы ищем.


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
    Для хеширования входных чисел мы используем встроенную в Python функцию hash,
    она отвечает всем требованиям адекватной хеш фукнции.
    Разрешение коллизий происходит с помощью метода открытой адресации с
    квадратичным пробированием. Номер шага учавствует в сумме дважды, в итоге
    индексы следующих корзин будут отличаться в зависимости от того, на каком
    шаге пробирования мы находимся.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    В среднем сложность программы для n запросов - O(n), и в худшем случае
    - квадратичная O(n * n).

    Все операции в среднем выполняются за O(1). Так как отсутствует
    рехеширование и масштабирование таблицы, в случае неудачных
    последовательностей или высокого коэффициента заполненности таблицы,
    обработка коллизий методом открытой адресации может увеличивать сложность
    до линейной O(n).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Величина затрат памяти - O(n)

    Хеш-таблица, при создании, создает пустой массив ~(n * 2) размера, зная по
    условию задачи, что количество ключей в таблице не может превышать
    n = 10 ** 5.
    В ходе выполнения запросов к хеш-таблице, использование памяти константное,
    любой запрос не требует более чем O(1) памяти.
"""
from collections import namedtuple
import math


EmployeeSalary = namedtuple("EmployeeSalary", ["id", "salary"])


class CustomHashMap:
    max_size = None
    data = None

    def __init__(self, max_size):
        self.max_size = max_size
        self.data = [None] * max_size

    def __get_bucket(self, key):
        return hash(key) % self.max_size

    def __find_key(self, key):
        bucket_index = self.__get_bucket(key)
        i = 1
        while not self.data[bucket_index] is None and self.data[bucket_index].id != key:
            bucket_index = (bucket_index + i * i) % self.max_size
            i += 1
        return bucket_index

    def put(self, key, value):
        i = self.__find_key(key)
        self.data[i] = EmployeeSalary(key, value)

    def delete(self, key):
        i = self.__find_key(key)

        if self.data[i] is None:
            return None

        value = self.data[i].salary
        self.data[i] = None
        return value

    def get(self, key):
        i = self.__find_key(key)

        if self.data[i] is None:
            return None

        return self.data[i].salary


def main():
    MAX_POSSIBLE_KEYS = 10**5
    custom_map = CustomHashMap(math.floor(MAX_POSSIBLE_KEYS * 4 / 3))

    n = int(input())
    for _ in range(n):
        args = input().split()

        if args[0] == "get":
            print(custom_map.get(int(args[1])))
        elif args[0] == "put":
            custom_map.put(int(args[1]), int(args[2]))
        else:
            print(custom_map.delete(int(args[1])))


if __name__ == "__main__":
    main()
