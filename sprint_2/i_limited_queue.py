class QueueOverflowException(Exception):
    pass


class QueueIsEmptyException(Exception):
    pass


class MyQueueSized:
    max_size = None
    queue = []
    head = 0
    tail = 0
    current_size = 0

    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size

    def push(self, x):
        if self.size() == self.max_size:
            raise QueueOverflowException()
        self.current_size += 1
        self.queue[self.head] = x
        self.head = (self.head + 1) % self.max_size

    def pop(self):
        if not self.size():
            raise QueueIsEmptyException()
        self.current_size -= 1
        x = self.queue[self.tail]
        self.queue[self.tail] = None
        self.tail = (self.tail + 1) % self.max_size
        return x

    def peek(self):
        if not self.size():
            raise QueueIsEmptyException()
        return self.queue[self.tail]

    def size(self):
        return self.current_size


def process_commands(n, q):
    for _ in range(n):
        args = input().split()

        # push
        if len(args) == 2:
            try:
                q.push(int(args[1]))
            except QueueOverflowException:
                print("error")
            continue

        command = args[0]
        if command == "peek":
            try:
                print(q.peek())
            except QueueIsEmptyException:
                print(None)
        elif command == "size":
            print(q.size())
        else:
            try:
                print(q.pop())
            except QueueIsEmptyException:
                print(None)


if __name__ == "__main__":
    n = int(input())
    queue_max_size = int(input())
    q = MyQueueSized(queue_max_size)
    process_commands(n, q)
