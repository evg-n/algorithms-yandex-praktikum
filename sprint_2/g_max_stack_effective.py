# StackMaxEffective class
# O(1) for finding max element, standart stack interface support


class StackIsEmptyException(Exception):
    pass


class StackMaxEffective:
    max_el = None
    stack = []

    def push(self, x):
        if not self.stack:
            self.max_el = x
            self.stack.append(x)
        elif x <= self.max_el:
            self.stack.append(x)
        else:
            self.stack.append(x * 2 - self.max_el)
            self.max_el = x

    def pop(self):
        if not self.stack:
            raise StackIsEmptyException()

        y = self.stack.pop()
        if y <= self.max_el:
            return y

        current_max = self.max_el
        self.max_el = self.max_el * 2 - y
        return current_max

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def get_max(self):
        if not self.stack:
            raise StackIsEmptyException()

        return self.max_el


def process_input_commands(s):
    n = int(input())
    for _ in range(n):
        args = input().split()

        # push
        if len(args) > 1:
            s.push(int(args[1]))
            continue

        command = args[0]
        if command == "pop":
            try:
                s.pop()
            except Exception as e:
                print("error")
        else:
            try:
                print(s.get_max())
            except Exception as e:
                print(None)


if __name__ == "__main__":
    stack = StackMaxEffective()
    process_input_commands(stack)
