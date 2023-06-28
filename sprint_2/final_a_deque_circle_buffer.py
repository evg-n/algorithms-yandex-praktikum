"""
-- ПРИНЦИП РАБОТЫ --
Элементы хранятся в массиве, заполненым пустыми значениями по размеру n.
Важный инвариант: В любой момент времени указатели head_index и tail_index 
указывают на первый и последний элементы кольцевого буфера.

- При вставке в пустой буфер, мы не обновляем значения индексов, чтобы 
 инвариант не нарушался.
- Также, при удалении элемента (pop_back и pop_front), мы перестаем обновлять
 значения индексов, когда длина буфера становится равной единице, чтобы в этом
 случае head_index и tail_index одновременно указывали на единственный элемент
 (выполнялся исходный инвариант).


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Поддерживается заявленый интерфейс дека, формат ввода/вывода, ошибки. 
Данные в деке хранятся в массиве. С помощью индексов head/tail поддерживается извлечение/запись 
элементов как в прямом, так и в обратном порядке.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Добавление/Удаление из очереди с обоих концов выполняется за O(1).
Каждая операция - это опциональное обновление соответствующего индекса O(1), 
и получение/запись соответствующего элемента по индексу в списке data, что также имеет сложность - O(1).
Общая сложность программы, выполняющей n запросов к деку - O(n).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Класс не содержит более m элементов. Очередь потребляет O(m) для хранения исходных данных.
"""


class DequeOverflowError(Exception):
    pass


class DequeIsEmptyError(Exception):
    pass


class Deque:
    max_size = None
    current_size = 0
    data = []
    head_index = 0
    tail_index = 0

    def __init__(self, max_size):
        self.max_size = max_size
        self.data = [None] * max_size

    # backward circular buffer index update
    # e.g.: ... -> 1 -> 0 -> (max_size - 1) -> (max_size - 2) -> ...
    def __rotate_back(self, index):
        return index - 1 if index > 0 else self.max_size - 1

    # forward circular buffer index update
    # e.g.: ... -> (max_size - 2) -> (max_size - 1) -> 0 --> 1 --> ...
    def __rotate_front(self, index):
        return (index + 1) % self.max_size

    def push_back(self, value):
        if self.is_full():
            raise DequeOverflowError()

        # don't update tail when the deque is empty
        if self.size():
            self.tail_index = self.__rotate_back(self.tail_index)

        self.data[self.tail_index] = value
        self.current_size += 1

    def push_front(self, value):
        if self.is_full():
            raise DequeOverflowError()

        # don't update head when the deque is empty
        if self.size():
            self.head_index = self.__rotate_front(self.head_index)

        self.data[self.head_index] = value
        self.current_size += 1

    def pop_front(self):
        if not self.size():
            raise DequeIsEmptyError()

        value = self.data[self.head_index]
        if self.size() > 1:
            self.head_index = self.__rotate_back(self.head_index)

        self.current_size -= 1
        return value

    def pop_back(self):
        if not self.size():
            raise DequeIsEmptyError()

        value = self.data[self.tail_index]
        if self.size() > 1:
            self.tail_index = self.__rotate_front(self.tail_index)

        self.current_size -= 1
        return value

    def size(self):
        return self.current_size

    def is_full(self):
        return self.current_size == self.max_size


def process_input_commands(n, deque):
    for _ in range(n):
        args = input().split()

        command = args[0]
        try:
            if command == "push_front":
                deque.push_front(int(args[1]))
            elif command == "push_back":
                deque.push_back(int(args[1]))
            elif command == "pop_front":
                print(deque.pop_front())
            else:
                print(deque.pop_back())
        except (DequeIsEmptyError, DequeOverflowError) as _:
            print("error")


def read_input_params():
    commands_count = int(input())
    deque_max_size = int(input())
    return (commands_count, deque_max_size)


def main():
    commands_count, deque_max_size = read_input_params()
    my_deque = Deque(deque_max_size)
    process_input_commands(commands_count, my_deque)


if __name__ == "__main__":
    main()
