class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class QueueIsEmptyException(Exception):
    pass


class LinkedListQueue:
    current_size = 0
    head = None
    tail = None

    def get(self):
        if not self.size():
            raise QueueIsEmptyException()
        x = self.tail.value
        self.tail = self.tail.next_item
        self.current_size -= 1
        return x

    def put(self, x):
        if not self.size():
            self.head = self.tail = Node(x)
            self.current_size += 1
            return
        new_node = Node(x)
        self.head.next_item = new_node
        self.head = new_node
        self.current_size += 1

    def size(self):
        return self.current_size


def process_commands(n, q):
    for _ in range(n):
        args = input().split()
        if len(args) > 1:
            q.put(int(args[1]))
        elif args[0] == "get":
            try:
                print(q.get())
            except QueueIsEmptyException:
                print("error")
        else:
            print(q.size())


if __name__ == "__main__":
    n = int(input())
    q = LinkedListQueue()
    process_commands(n, q)
